from django.urls import path
from django.views.generic import TemplateView

from front import views


app_name = 'front'
urlpatterns = [
    path('index/', views.index, name="index"),
    path('index2/', views.index2, name="index2"),
    path('index3/', views.index3, name="index3"),
    path('add_book/', views.add_book, name="add_book"),
    path('article_list/', views.BookAddListView.as_view(), name="article_list"),
    path('login/', views.login, name="login"),
    path('ProfileView/', views.ProfileView.as_view(), name="ProfileView"),
    # path('about/', TemplateView.as_view(template_name='template.html'))   # 不用写试图函数，直接展示静态页面
    path('template/', views.TemplateViewDemo.as_view(), name="template"),
    path('front_page/', views.front_page, name="front_page"),
    path('check_token/', views.check_token.as_view(), name="check_token")
]
