from flask import Flask
from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('test.html')
app.run(host="0.0.0.0")

@app.route('/run_python_code', methods=['POST'])
def run_python_code():
    
    return jsonify(message="Pythonコードが実行されました")

# if __name__ == "__main__":
#     app.run(debug=True)

