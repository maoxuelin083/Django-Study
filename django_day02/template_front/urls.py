from django.urls import path

from template_front import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('test/', views.test, name="test"),
    path('person/', views.person, name="person"),
    path('test2/', views.test2, name="test2"),
    path('test3/', views.test3, name="test3")
]

