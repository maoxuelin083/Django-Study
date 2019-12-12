from django.db import models

# Create your models here.


class Categroy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "<Category>:(id:%s, name:%s)" %(self.id, self.name)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    # articles = models.ManyToManyField("Article", related_name="articles")
    articles = models.ManyToManyField("Article")


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey("Categroy", on_delete=models.CASCADE, null=True, related_name="categories")
    author = models.ForeignKey("frontuser.User", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "<Article>:(id:%s, title:%s, content:%s, category:%s, author:%s)" % (self.id, self.title, self.content, self.category, self.author)