import json

from redminelib import Redmine


def ret_key(name, password, domain):
    redmine = Redmine(domain, username=name, password=password).auth()
    api = redmine.api_key
    return json.dumps({'api_key': api, 'name': redmine},
                      ensure_ascii=False, default=str)


# print(ret_key('admin', 'P@ssword123', 'http://192.168.111.74:3718'))
