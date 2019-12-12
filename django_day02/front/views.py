from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse("前台首页")
    else:
        url_for = reverse("cms:login")   # 跳转到后台的cms/login页面
        print(url_for)
        return redirect(url_for)
        # return redirect("/login/")    # 重定向


def login(request):
    return HttpResponse("前台登陆页")