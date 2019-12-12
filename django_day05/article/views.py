from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from article.models import Article, Categroy, Tag
from frontuser.models import User, UserExtendsion


def index(request):
    user = User(name="小红")
    user.save()
    category = Categroy(name='中国古典文学')
    category.save()
    return HttpResponse("success")


def one_to_one_view(request):
    articel = Article(title='西游记', content='作者：吴承恩')
    user = User.objects.get(pk=3)   # 拿到发表者的第一条信息
    print(user)
    categroy = Categroy.objects.first()  # 拿到第一个标签
    print(categroy)
    articel.category = categroy
    articel.author = user
    articel.save()
    return HttpResponse("success")


def many_to_many_view(request):
    # article = Article.objects.get(pk=6)  # 找到主键id=3 的用户的文章
    # tag = Tag(name="经典作品")    # 设置标签的name
    # tag.save()
    # # tag.articles.add(article)  # 这是在Tag模型下设置了  related_name="articles"
    # article.tag_set.add(tag)  # 这是没有在Tag模型下设置   related_name="articles"
    tag = Tag.objects.get(pk=3)   # 根据主键id=3 查找到tag所对应的
    articles = tag.articles.all()
    for article in articles:
        print(article)
    return HttpResponse("success")
