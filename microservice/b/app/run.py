import json
import os

import requests
from flask import Flask, request

app = Flask(__name__)

rs = {
    "b": "LOCAL b"
}


@app.route("/b")
def b():
    return rs


@app.route("/bc")
def bc():
    response = requests.get('http://c:8080/c', headers={"x-user-email": request.headers.get("x-user-email")})
    s_rs = json.loads(response.text)
    return {**rs, **s_rs}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('listenport', 18080))
