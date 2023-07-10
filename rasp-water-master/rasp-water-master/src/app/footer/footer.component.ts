import { Component, OnInit } from '@angular/core';
import { Inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import build from '../../build';

import * as moment from 'moment';

export interface SysinfoResponse {
    date: string;
    uptime: string;
    loadAverage: string;
}

@Component({
    selector: 'app-footer',
    templateUrl: './footer.component.html',
    styleUrls: ['./footer.component.scss'],
    standalone: true,
})
export class FooterComponent implements OnInit {
    buildDate = moment(build.timestamp).format('llll');
    buildDateFrom = moment(build.timestamp).fromNow();
    date = '';
    uptime = '';
    uptimeFrom = '';
    loadAverage = '';
    interval = 0;

    constructor(private http: HttpClient, @Inject('ApiEndpoint') private readonly API_URL: string) {}

    ngOnInit() {
        this.updateSysinfo();
        this.interval = window.setInterval(() => {
            this.updateSysinfo();
        }, 60000);
    }

    updateSysinfo() {
        this.http.jsonp<SysinfoResponse>(`${this.API_URL}/sysinfo`, 'callback').subscribe(
            (res: SysinfoResponse) => {
                const date = moment(res['date']);
                const uptime = moment(res['uptime']);
                this.date = date.format('llll');
                this.uptime = uptime.format('llll');
                this.uptimeFrom = uptime.fromNow();
                this.loadAverage = res['loadAverage'];
            },
            (error) => {
                // ignore
            }
        );
    }
}
