import os

from flask import Flask

app = Flask(__name__)


@app.route("/c")
def c():
    return {
        "c": "hello from c"
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('listenport', 8080))
