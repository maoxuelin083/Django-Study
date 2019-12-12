from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import Book


def index(request):
    # book = Book(name='三国演义', author='罗贯中', price=100)
    # book.save()

    # 查询   1.get(pk=???)   2.filter().first() 第一个  .all()全部
    # book = Book.objects.get(pk=1)
    # print(book)
    # book = Book.objects.filter(name='三国演义').first()
    # print(book)

    # 改
    # book = Book.objects.get(pk=1)
    # book.name = '红楼梦'
    # book.author = '曹雪芹'
    # book.price = 102
    # book.save()

    # 删除
    book = Book.objects.get(pk=1)
    book.delete()
    return HttpResponse("首页")