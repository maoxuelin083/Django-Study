from django.urls import path

from front import views


app_name = 'front'
urlpatterns = [
    path('', views.index, name="index"),
    path('singin/', views.login, name="login"),   # 通过reverse=('login')与login联系起来，前端页面返回的就是singin
]


