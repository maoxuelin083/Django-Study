from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request):
    html = render_to_string("index.html")
    return HttpResponse(html)


# 模板 通过字典中的key访问对应的value
def test(request):
    return render(request, "test.html", context={"username": "mxl"})


# 通过对象访问，对象中的属性
class Person:
    def __init__(self, username):
        self.username = username


def person(request):
    p = Person("zzz")
    context = {
        "person": p
    }
    return render(request, "test.html", context=context)


# 访问字典中的key对应的value值
def test2(request):
    context = {
        'person': {
            "name": "小明",
            "age": 18
        }
    }
    return render(request, "test.html", context=context)


# 访问元祖或者列表   在页面中以为 . 的形式
def test3(request):
    context = {
        'tup1': (
            '小明',
            '小王',
            '小赵'
        )
    }
    return render(request, "test.html", context=context)