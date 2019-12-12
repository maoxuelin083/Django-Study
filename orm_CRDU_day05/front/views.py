from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from front.models import Category, Article


def index(request):
    category = Category(name='国产')
    category.save()
    article = Article(title='论母猪的产后抚养', content='遇见你的时候你是傻逼')
    article.category = category
    article.save()
    return HttpResponse("首页")


def index1(request):
    article = Article.objects.get(pk=1)
    print(article)
    return HttpResponse("index1")








