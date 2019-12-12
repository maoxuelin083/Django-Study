from django.http import HttpResponse
from django.shortcuts import render, redirect

# url 命名空间
# def index(request):
#     username = request.GET.get("username")   # request.GET["xxx"]
#     if username:
#         return HttpResponse("个人中心")
#     else:
#         return redirect('/login/')
#
#
# def login(request):
#     return HttpResponse("前台登陆页")

# 应用命名空间
from django.urls import reverse
#
# app_name = 'front'
# def index(request):
#     username = request.GET.get("username")
#     if username:
#         return HttpResponse("前台个人中心")
#     else:
#         url_for = reverse('login')
#         return redirect(url_for)
#
#
# def login(request):
#     return HttpResponse("前台登陆页")


def index(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse("前台个人中心")
    else:
        url_for = reverse('cms:login')
        return redirect(url_for)


def login(request):
    return HttpResponse("前台登陆页")


