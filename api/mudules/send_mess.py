from celery import shared_task
import requests
import json
from api.mudules.forming import proj_all


@shared_task
def play_fair(url_r, api_key):
    url = 'https://mm.software-academy.ru/hooks/qrc9k3w7t7f1jfx7up8fyu8n3c'
    payload = {'text': proj_all(url_r, api_key)}
    n = json.dumps(payload)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    response = requests.request("POST", url, data=n, headers=headers)
    print('works')
    return 'success'
