from django.views.decorators.csrf import csrf_exempt
from api.mudules.send_mess import play_fair
from api.mudules.get_key import ret_key
from api.mudules.projectsandusers import projects
from api.mudules.projectsandusers import members
from django.http import HttpResponse
import json


@csrf_exempt
def auth(request):
    if request.method == "POST":
        auth_this = json.loads(request.body)
        return HttpResponse(ret_key(auth_this['login'], auth_this['password'], auth_this['domain']))

    if request.method == "GET":
        return HttpResponse("{}")


@csrf_exempt
def send_mess(request):
    if request.method == "POST":
        play_fair(json.loads(request.body)['url_r'], json.loads(request.body)['key'])
        return HttpResponse('success')
    if request.method == "GET":
        return HttpResponse("{}")


@csrf_exempt
def load_projects(request):
    if request.method == "POST":
        p = json.dumps(projects(KEY=json.loads(request.body)['key'], url=json.loads(request.body)['url_r']))
        return HttpResponse(p)
    if request.method == "GET":
        return HttpResponse('1121')


@csrf_exempt
def load_members(request):
    if request.method == "POST":
        p = json.dumps(members(KEY=json.loads(request.body)['key'], proj_number=json.loads(request.body)['project_id'], url=json.loads(request.body)['url_r']),
                       ensure_ascii=False, default=str)
        return HttpResponse(p)


@csrf_exempt
def null_point(request):
    return HttpResponse('success')
