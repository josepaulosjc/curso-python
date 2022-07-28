import os
import json
from lambda_function import lambda_handler

envs = json.load(
    open("../infra/parameters-dev.json", encoding='utf-8')).get('Parameters')
[os.environ.setdefault(str(x), str(y)) for x, y in envs.items()]

event_data = json.load(
    open("src/resources/lambda_teste_event.json", encoding='utf-8')
)

response = lambda_handler(event_data, [])
print(json.dumps(response, indent=4))