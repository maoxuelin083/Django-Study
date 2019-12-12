from django.shortcuts import render, redirect
from django.db import connection

# Create your views here.
from django.urls import reverse


def get_cursor():
    return connection.cursor()


def index(request):
    cursor = get_cursor()
    cursor.execute("select * from book")
    books = cursor.fetchall()
    print(books)
    context = {
        'books': books
    }
    return render(request, 'index.html', context=context)


def add_book(request):
    print(request.method)
    if request.method == "GET":
        return render(request, 'add.html')
    else:
        name = request.POST.get("name")
        author = request.POST.get("author")
        print(name)
        cursor = get_cursor()
        cursor.execute("insert into book(id,name,author) values (null,'%s','%s')" % (name, author))
        return redirect(reverse('index'))


def book_detail(request, book_id):
    cursor = get_cursor()
    cursor.execute("select * from book where id=%s" % book_id)
    book = cursor.fetchone()
    print(book)
    context = {
        "book": book
    }
    return render(request, 'detail.html', context=context)


def book_modify(request, book_id):
    name = request.POST.get("name")
    author = request.POST.get("author")
    cursor = get_cursor()
    cursor.execute("update book set name='%s',author='%s' where id=%s" %(name,author,book_id))






