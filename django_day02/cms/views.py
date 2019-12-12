from django.http import HttpResponse
from django.shortcuts import redirect
# from django.urls import reverse
from django.urls import reverse


def index(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse("后台首页")
    else:
        # url_for = reverse("front:login")   # 指定跳转到 前台的front/login登录页面  有一个对应关系
        # return redirect(url_for)
        # 实例命名空间
        current_namespace = request.resolver_match.namespace
        return redirect(reverse("%s login" % current_namespace))


def login(request):
    return HttpResponse("后台登陆页")