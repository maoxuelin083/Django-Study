from django.urls import path

from front import views

urlpatterns = [
    path('add/', views.add, name="add"),
    path('index1/', views.index1, name="index1"),
    path('index2/', views.index2, name="index2")
]