from django.shortcuts import render
from django.views.generic import View


class BookListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class BookList(View):
    pass

