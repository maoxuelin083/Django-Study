from django.urls import path

from study import views

app_name = 'cms'   #一定要加载urls上  才能进行再外面包中的加载
urlpatterns = [
    path('index/', views.index, name="index"),
    path('singin/', views.login, name="login"),
    path('book/<id>/', views.book, name="book")
]