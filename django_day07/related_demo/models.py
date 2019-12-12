from django.db import models

# Create your models here.


class UsersDemo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=100)
    sex = models.CharField(max_length=2)


class ArticleDemo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    users = models.ForeignKey("UsersDemo", on_delete=models.CASCADE)