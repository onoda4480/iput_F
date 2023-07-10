#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import request, jsonify, Blueprint, url_for
from flask_cors import cross_origin
import json
import threading
import urllib.parse
from multiprocessing import Queue

from webapp_config import APP_URL_PREFIX
from webapp_event import notify_event, EVENT_TYPE
from webapp_log import app_log
from flask_util import support_jsonp, remote_host
import scheduler

blueprint = Blueprint("rasp-water-schedule", __name__, url_prefix=APP_URL_PREFIX)

schedule_lock = threading.Lock()
schedule_queue = None

WDAY_STR = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
WDAY_STR_JA = ["日", "月", "火", "水", "木", "金", "土"]


def init(config):
    global schedule_queue

    schedule_queue = Queue()
    scheduler.init()
    threading.Thread(
        target=scheduler.schedule_worker,
        args=(
            config,
            schedule_queue,
        ),
    ).start()


def wday_str_list(wday_list, lang="en"):
    wday_str = WDAY_STR
    if lang == "ja":
        wday_str = WDAY_STR_JA

    return map(
        lambda i: wday_str[i], (i for i in range(len(wday_list)) if wday_list[i])
    )


def schedule_entry_str(entry):
    return "{} 開始 {} 分間 {}".format(
        entry["time"], entry["period"], ",".join(wday_str_list(entry["wday"], "ja"))
    )


def schedule_str(schedule):
    str = []
    for entry in schedule:
        if not entry["is_active"]:
            continue
        str.append(schedule_entry_str(entry))

    if len(str) == 0:
        return "∅ 全て無効"

    return "、\n".join(str)


@blueprint.route("/api/schedule_ctrl", methods=["GET", "POST"])
@support_jsonp
@cross_origin()
def api_schedule_ctrl():
    cmd = request.args.get("cmd", None)
    data = request.args.get("data", None)
    if cmd == "set":
        with schedule_lock:
            schedule_data = json.loads(data)

            endpoint = urllib.parse.urljoin(
                request.url_root,
                url_for("rasp-water-valve.api_valve_ctrl"),
            )

            for entry in schedule_data:
                entry["endpoint"] = endpoint
            schedule_queue.put(schedule_data)

            # NOTE: 本来は schedule_worker の中だけで呼んでるので不要だけど，
            # レスポンスを schedule_load() で返したいので，ここでも呼ぶ．
            scheduler.schedule_store(schedule_data)

            notify_event(EVENT_TYPE.SCHEDULE)

            host = remote_host(request)
            app_log(
                "📅 スケジュールを更新しました。\n{schedule}\n{by}".format(
                    schedule=schedule_str(schedule_data),
                    by="by {}".format(host) if host != "" else "",
                )
            )

    return jsonify(scheduler.schedule_load())
