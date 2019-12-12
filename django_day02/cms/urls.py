from django.urls import path, reverse
from cms import views

app_name = 'cms'
urlpatterns = [
    path('', views.index, name="index"),
    path('singin/', views.login, name="login")
]


