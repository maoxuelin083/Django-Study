from django.db import models

# Create your models here.


class ManyArticle(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


class ManyTag(models.Model):
    tags = models.CharField(max_length=32)
    articles = models.ManyToManyField("ManyArticle")
