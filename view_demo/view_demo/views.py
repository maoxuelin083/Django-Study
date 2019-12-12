
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.template.loader import get_template


def index1(request):
    response = HttpResponse("<h1>kangbazi</h1>", content_type='text/plain;charset=utf-8')
    response.status_code = 404
    return response


def json_view(request):
    persons = [
        {
            'username': 'mxl',
            'password': '123456',
            'age': 18,
            'sex': 0
        },
        {
            'username': 'zzz',
            'password': '123456',
            'age': 20,
            'sex': 1
        }
    ]
    response = JsonResponse(persons, safe=False)   # 要加上 safe=False
    return response


def csv_demo(request):
    response = HttpResponse(content_type='text/csv')
    response['Content_Disposition'] = 'attachment:filename="someone2.csv;charset=utf-8"'
    content = {
        'rows': [
            ['username', 'password', 'age'],
            ['zhang', '123', '0'],
            ['li', '123', '1']
        ]
    }
    template = loader.get_template('mxl')
    template_csv = template.render(content)
    response.content = template_csv
    return response




