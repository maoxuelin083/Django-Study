from django.urls import path

from modelform_demo import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('add/', views.add_book, name="add"),
    path('add_user/', views.add_user, name="add_user")
]