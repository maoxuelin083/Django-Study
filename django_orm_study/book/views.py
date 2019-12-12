from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import Authors, Books
from user.models import Users


def index(request):
    user = Users(u_name="zc")    # 读者
    user.save()
    author = Authors(name="施耐庵")     # 作者
    author.save()
    return HttpResponse("success")


def add_book(request):
    bookname = Books(b_name="红楼梦")
    author = Authors.objects.get(name="曹雪芹")
    user = Users.objects.get(u_name="zjr")
    bookname.b_author = author
    print(author)
    bookname.b_user = user
    print(user)
    bookname.save()
    return HttpResponse("add success")


def get_book(request):
    user = Users.objects.get(u_name='zjr')
    books = user.books_set.all()
    for book in books:
        print(book)
    return HttpResponse("get success")