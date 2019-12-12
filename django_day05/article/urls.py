from django.urls import path

from article import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('one_to_one_view/', views.one_to_one_view, name="one_to_one_view"),
    path('many_to_many_view/', views.many_to_many_view, name="many_to_many_view"),
]





