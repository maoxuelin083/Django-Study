from django.urls import path

from book import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add_book, name="add"),
    path('get/', views.get_book, name="get"),
]