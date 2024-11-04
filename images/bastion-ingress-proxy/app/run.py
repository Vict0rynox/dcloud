import json
import os

import flask
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/", defaults={'path': ''})
@app.route("/<path:path>")
def catch_all(path):
    host = request.headers.get('Host')
    url = f"http://{host}/{path}"
    response = requests.request(method=request.method, url=url, headers=request.headers, data=request.get_data())
    return response.content, response.status_code, response.headers.items()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('listenport', 80))
