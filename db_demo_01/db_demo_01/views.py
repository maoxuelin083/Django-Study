from django.db import connection
from django.shortcuts import render

class Book:
    def __init__(self, b_id, b_name, b_book):
        self.b_id = b_id
        self.b_name = b_name
        self.b_book = b_book


def index(request):
    cursor = connection.cursor()
    # cursor.execute("insert into book(name, author) values ('金瓶梅','鲁智深')")
    cursor.execute("select id,name,author from book")
    rows = cursor.fetchall()    # 是一个tuple对象
    context = {
        'rows1': rows[0],
        'rows2': rows[1]
    }
    return render(request, 'index.html', context=context)








