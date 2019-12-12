from django.urls import path

from manytomany import views

urlpatterns = [
    path('add/', views.add, name="add")
]