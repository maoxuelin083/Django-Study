from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View, TemplateView

from front.models import Article


def index(request):
    response = HttpResponse('<h1>你好</h1>', content_type='text/html;charset=utf-8')
    response.status_code = 404
    return response


def index2(request):
    persons = [
        {
            'msg': 'login success',
            'status': 200,
            'data':{
                'username': 'mxl',
                'password': '123'
            }
        },
        {
            'msg': 'login fail',
            'status': 400
        }
    ]
    response = JsonResponse(persons, safe=False)
    response.status_code = 400   # 设置状态相应码
    return response


def index3(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment:filename="index.csv"'
    context = {
        'rows': [
            ['username', 'password', 'age'],
            ['zzz', '123', '0'],
            ['aaa', '321', '0'],
        ]
    }
    template = loader.get_template('mxl.txt')
    csv_template = template.render(context)
    response.content = csv_template
    return response


class TemplateViewDemo(TemplateView):

    template_name = 'template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['phone'] = 123883923
        return context


def add_book(request):
    articles = []
    for x in range(200):
        article = Article(title='标题:%s' % x, content='内容:%s' % x)
        print(article)
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse("成功")


class BookAddListView(ListView):
    model = 'Article'
    template_name = 'ListViews.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'create_time'
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        context = super(BookAddListView, self).get_context_data()
        return context

    # 如果你不想要全部数据 只要部分数据 那么 需要重写
    # get_queryset方法
    def get_queryset(self):
        return Article.objects.filter(id__lte=100)


# 装饰器1 判断有没有token   不用去views.py中注册
def check_login(func):
    def wrapper(request, *args, **kwargs):
        token = request.GET.get("token")
        if not token:
            return redirect(reverse('front:front_page'))
        return func(request, *args, **kwargs)
    return wrapper


def front_page(request):
    return HttpResponse("首页")


@method_decorator([check_login], name='dispatch')
class check_token(View):
    def get(self, request):
        return HttpResponse("登陆成功")


# 装饰器
def login_required(func):
    def wrapper(request, *args, **kwargs):
        username = request.GET.get("username")
        if not username:
            return redirect(reverse('front:login'))  # url 标签
        return func(request, *args, **kwargs)
    return wrapper


def login(request):
    return HttpResponse("登录页")


@method_decorator([login_required], name='dispatch')
class ProfileView(View):
    def get(self, request):
        return HttpResponse("个人中心")

