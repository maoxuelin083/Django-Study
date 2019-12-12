from datetime import datetime

from django.shortcuts import render

# Create your views here.


# def index(requets):
#     context = {
#         'value': '班华雄',
#         'times': datetime(year=2019, month=12, day=4, hour=12, minute=12, second=12)
#     }
#     return render(requets, 'index.html', context=context)


def test(request):
    context = {
        'x': ['1', '2', '3'],
        'y': [4, '5', '6']
    }
    return render(request, 'test.html', context=context)


def date(request):
    context = {
        'now': datetime.now()
    }
    return render(request, 'date.html', context=context)


def dafault1(request):
    context = {
        "default1": ""
    }
    return render(request, 'test.html', context=context)


def test_filter(request):
    context = {
        "value": test_filter("草你妈")
    }
    return render(request, 'date.html', context=context)


def escape(request):
    context = {
        'value': '<a href="http://www.baidu.com>百度</a>'
    }
    return render(request, 'test.html', context=context)