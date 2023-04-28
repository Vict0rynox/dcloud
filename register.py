import os
import sys
import re

# example: deployment/kubernetes/applications/b/
service_path = sys.argv[0]

if service_path is None:
    raise RuntimeError("No service path")

PUBLIC_KEY = os.getenv('DCLOUD_PUBLIC_KEY')
USER_EMAIL = os.getenv('DCLOUD_USER_EMAIL')
ISTIO_SERVICE_NAME = os.getenv('DCLOUD_ISTIO_SERVICE_NAME')

PATH = 'deployment/kubernetes/dcloud/balancer'

if PUBLIC_KEY is None or USER_EMAIL is None is None:
    raise RuntimeError("No local variables DCLOUD_PUBLIC_KEY or DCLOUD_USER_EMAIL found")

normalized_username = USER_EMAIL.split("@")[0]
matches = re.findall("[a-zA-Z]", normalized_username)
username = ''.join(matches)

files = os.listdir(PATH)
tmpl_files = [file for file in files if file.endswith('.tmpl')]

os.makedirs(f'{PATH}/autogenerated', exist_ok=True)

for file in tmpl_files:
    with open(f"{PATH}/{file}") as f:
        template = f.read()
        template = template.replace('$DCLOUD_PUBLIC_KEY', PUBLIC_KEY)
        template = template.replace('$DCLOUD_USER_EMAIL', USER_EMAIL)
        template = template.replace('$DCLOUD_USER', username)
        template = template.replace('$DCLOUD_ISTIO_SERVICE_NAME', ISTIO_SERVICE_NAME)

        file_yml = file.replace("tmpl", 'yml')
        with open(f'{PATH}/autogenerated/{file_yml}', 'w') as f:
            f.write(template)

os.system(f'bash register_cmd.sh {service_path}')