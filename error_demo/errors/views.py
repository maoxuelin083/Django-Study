# encoding:utf-8
from django.shortcuts import render


def view_403(request):
    return render(request, 'errors/403.html', status=403)   # 先要注册进入settings


def view_405(request):
    return render(request, 'errors/405.html', status=405)


def view_404(request):
    return render(request, 'errors/404.html', status=404)