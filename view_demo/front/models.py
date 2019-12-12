from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)


class Articles(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE)