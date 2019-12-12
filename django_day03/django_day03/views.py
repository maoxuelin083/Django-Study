from datetime import datetime

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def index1(request):
    context = {
        'info': '<script>alert("666")</script>'
    }
    return render(request, 'index.html', context=context)


def add_view(request):
    context = {
        'x': ['1', '2', '3'],
        'y': [4, '5', '6']
    }
    return render(request, 'add.html', context=context)


def cut_view(request):
    # context = {
    #     'x': ['1', '2', '3'],
    #     'y': [4, '5', '6']
    # }
    return render(request, 'cut.html')


def date_view(request):
    context = {
        'today': datetime.now()
    }
    return render(request, 'date.html', context=context)


def default_view(request):
    context = {
        'value': None   # [] "" None
    }
    return render(request, 'default.html', context=context)
