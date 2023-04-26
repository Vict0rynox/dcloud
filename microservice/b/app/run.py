import json
import os

import requests
from flask import Flask

app = Flask(__name__)

rs = {
    "b": "hello from b"
}


@app.route("/b")
def b():
    return {
        "b": "hello from b"
    }


@app.route("/bc")
def bc():
    response = requests.get('http://c:8080/c')
    s_rs = json.loads(response.text)
    return {**rs, **s_rs}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('listenport', 8080))
