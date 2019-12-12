from django.db import models

# Create your models here.


# 标签与文章是多对多的关系
class Tag(models.Model):
    name = models.CharField(max_length=100, null=False)
    articles = models.ManyToManyField("Article")
    # article.tag_set.add(tag)


class Article(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()



