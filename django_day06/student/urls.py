from django.urls import path

from student import views

urlpatterns = [
    path('index1/', views.index1, name="index1"),
    path('index2/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3'),
    path('index4/', views.index4, name='index4'),
    path('index5/', views.index5, name='index5'),
    # path('index6/', views.index6, name='index6'),
    # path('index7/', views.index7, name='index7'),
    # path('index8/', views.index8, name='index8'),
    # path('index9/', views.index9, name='index9'),
    # path('index10/', views.index10, name='index10'),
    # path('index11/', views.index11, name='index11'),
    # path('index12/', views.index12, name='index12'),
    # path('index13/', views.index13, name='index13'),
    # path('index14/', views.index14, name='index14'),
    # path('index15/', views.index15, name='index15'),
]