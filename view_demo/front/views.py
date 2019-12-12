from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from front.models import Articles, Author


def add(request):
    article = Articles(title="嘻嘻嘻", content="三顾哈哈哈茅庐")
    author = Author(name="罗贯中")
    author.save()
    article.author = author  # 保存
    article.save()
    return HttpResponse("success")


# 查询该作者的所有文章
def index1(request):
    author = Author.objects.first()
    articles = author.articles_set.all()  # 查看author下的所有文章
    print(articles)
    return HttpResponse("index1")


# 在多的一方使用select_related()
def index2(request):
    articles = Articles.objects.select_related().get(pk=1)
    print(articles)
    # for a in articles:
    #     print(a.title)
    #     print(a.content)
    return HttpResponse("index2")