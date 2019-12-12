from django.urls import path

from errors import views

app_name = 'errors'
urlpatterns = [
    path('403.html', views.view_403, name="403"),
    path('405.html', views.view_405, name="405"),
    path('404.html', views.view_404, name="404"),
]