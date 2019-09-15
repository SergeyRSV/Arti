import requests
import json
import schedule
from threading import Thread
import time

from config import *
from getInfo import string

dev_team = {
    'Сергей': '@rezuevsv',
    'Влад': '@vl404',
    'Никита': '@nik.anikin.01',
    'Александр': '@damnik94',
    'Дмитрий': '@konchev.2013'
}


def post_message(INC_WEBHOOK, text, target_name):
    print("Message send")
    url = INC_WEBHOOK
    payload = {
        'text': text,
        'channel': target_name
    }
    n = json.dumps(payload)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    response = requests.request("POST", url, data=n, headers=headers)
    print(response.text)


def dm_end():
    INC_WEBHOOK = INC_WEBHOOK_config
    product_manager = product_manager_conf
    text = string + '\n''Очередной митинг завершен. Пожалуйста не забудьте написать протокол митинга. Хорошей работы!'
    post_message(INC_WEBHOOK, text, product_manager)


def before_dm():
    INC_WEBHOOK = INC_WEBHOOK_config
    product_manager = product_manager_conf
    link = link_conf
    text = 'Ссылка на сводку, статус, аналитику. ' + link
    post_message(INC_WEBHOOK, text, product_manager)


def before_dm_dev():
    for value in dev_team.values():
        print(value, end="\n")
        INC_WEBHOOK = INC_WEBHOOK_config
        link = link_conf
        text = 'Ссылка на сводку, статус, аналитику. ' + link
        post_message(INC_WEBHOOK, text, value)


# 1.1.1. Напоминание написать Daily meeting  -----------------
daily_meeting_end = "11:44"

schedule.every().monday.at(daily_meeting_end).do(dm_end)
schedule.every().tuesday.at(daily_meeting_end).do(dm_end)
schedule.every().wednesday.at(daily_meeting_end).do(dm_end)
schedule.every().thursday.at(daily_meeting_end).do(dm_end)
schedule.every().friday.at(daily_meeting_end).do(dm_end)

# ------------------------------------------------------------

# 1.1.3. Подготовка к Daily Meeting
before_daily_meeting = "09:45"

schedule.every().monday.at(before_daily_meeting).do(before_dm)
schedule.every().tuesday.at(before_daily_meeting).do(before_dm)
schedule.every().wednesday.at(before_daily_meeting).do(before_dm)
schedule.every().thursday.at(before_daily_meeting).do(before_dm)
schedule.every().friday.at(before_daily_meeting).do(before_dm)

# ------------------------------------------------------------

# 1.2.1. Подготовка к Daily Meeting (dev)
before_daily_meeting_dev = "10:14"

schedule.every().monday.at(before_daily_meeting_dev).do(before_dm_dev)
schedule.every().tuesday.at(before_daily_meeting_dev).do(before_dm_dev)
schedule.every().wednesday.at(before_daily_meeting_dev).do(before_dm_dev)
schedule.every().thursday.at(before_daily_meeting_dev).do(before_dm_dev)
schedule.every().friday.at(before_daily_meeting_dev).do(before_dm_dev)


# ------------------------------------------------------------

def schedule_func():
    while True:
        schedule.run_pending()
        time.sleep(30)


def time_count():
    while True:
        time.sleep(30)  # in seconds
        print(time.ctime())


if __name__ == '__main__':
    Thread(target=schedule_func).start()
    Thread(target=time_count).start()
