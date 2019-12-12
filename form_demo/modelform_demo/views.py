from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from modelform_demo.forms import AddBookForm, AddUserDemo


def index(request):
    return HttpResponse("首页")


def add_book(request):
    form = AddBookForm(request.POST)
    print(form)
    if form.is_valid():
        title = form.cleaned_data.get("title")
        page = form.cleaned_data.get("page")
        price = form.cleaned_data.get("price")
        print("title:%s,page:%s,price:%s" %(title, page, price))
        form.save()
        return HttpResponse("success")
    else:
        # print(form.errors.get_json_data())
        print(form.get_errors())
        return HttpResponse("fail")


def add_user(request):
    form = AddUserDemo(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        telephone = form.cleaned_data.get("telephone")
        print("username:%s,password:%s,telephone:%s" % (username, password, telephone))
        form.save()
        return HttpResponse("success")
    else:
        print(form.get_errors())
        return HttpResponse("fail")
