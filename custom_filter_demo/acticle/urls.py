from django.urls import path

from acticle import views

urlpatterns = [
    path("test/", views.test, name="test"),
    path("date/", views.date, name="date"),
    path("default1/", views.dafault1, name="default1"),
    path("test/", views.test_filter, name="test"),
    path("escape/", views.escape, name="escape")
]
