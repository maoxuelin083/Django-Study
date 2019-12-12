from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse("后台个人中心")
    else:
        url_for = reverse("login")
        return redirect(url_for)


def login(request):
    return HttpResponse("后台登陆页")


# url标签
def book(request):
    return render(request, 'books_url.html')