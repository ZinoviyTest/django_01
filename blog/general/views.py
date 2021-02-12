# from django.shortcuts import render
from django.http import HttpResponse
import datetime


def current_datetime_stop(request):
    now = '21:00'
    html = f'<html><body>Time: {now}</body></html>'
    return HttpResponse(html)


def current_datetime_now(request):
    now = datetime.datetime.now()
    html = f'<html><body>Time: {now}</body></html>'
    return HttpResponse(html)
