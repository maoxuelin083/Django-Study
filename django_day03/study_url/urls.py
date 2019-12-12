from django.urls import path

from study_url import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('singin/', views.login, name="login"),
]