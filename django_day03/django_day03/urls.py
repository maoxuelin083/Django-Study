"""django_day03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django_day03 import views
from article import arc_views

urlpatterns = [
    path('', include("study_url.urls")),
    path('cms/', include("study.urls")),
    # path('index/', views.index, name="index"),
    # path('index1/', views.index1, name="index1"),
    # path('add/', views.add_view, name="add"),
    # path('cut/', views.cut_view, name="cut"),
    # path('date/', views.date_view, name="date"),
    # path('default/', views.default_view, name="default"),
    # path('article/', arc_views.index, name="index"),
    # path('school/', arc_views.school, name="school"),
    # path('company/', arc_views.company, name="company"),
    # path('book/', arc_views.book, name="book")
]
