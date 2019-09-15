from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def auth(request):
    return render(request, 'main_static/auth.html')


@csrf_exempt
def main_page(request):
    return render(request, 'main_static/main.html')
