import json
import os

import requests
from flask import Flask

app = Flask(__name__)

ALLOWED_RELATED_SERVICES = {
    'a': 'localhost:8080',
    'b': 'localhost:8081'
}


@app.route("/")
def health_check():
    return "Hi from c service"


@app.route("/routes/<service_chain>")
def route_c(service_chain):
    root = {
        "c": f"hello from c"
    }

    return build_response(root, service_chain)


def build_response(root_message, service_chain):
    services_responses = dict()
    for service in service_chain:
        for service_name in ALLOWED_RELATED_SERVICES.keys():
            if service == service_name:
                try:
                    endpoint = ALLOWED_RELATED_SERVICES[service]
                    response = requests.get(f'http://{endpoint}/routes/{service}')
                    s_rs = json.loads(response.text)
                    services_responses[service] = s_rs[service]
                except:
                    print(f"Error during calling service {service}. Check the connection or port")

    return root_message | services_responses


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('listenport', 8082))
