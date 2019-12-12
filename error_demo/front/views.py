from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse


# Create your views here.


def index(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse("首页")
    else:
        return redirect(reverse("errors:403"))  # 在errors中的urls.py中写一个app_name='errors'


def index1(request):
    token = request.GET.get("token")
    if token:
        return HttpResponse("个人中心")
    else:
        return redirect(reverse("errors:404"))