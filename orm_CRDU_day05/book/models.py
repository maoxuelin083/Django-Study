from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=32, null=False)
    price = models.FloatField(default=0)

    def __str__(self):
        return "<Book>:(id:%s, name:%s, author:%s, price:%s)" % (self.id, self.name, self.author, self.price)

    class Meta:
        db_table = 'books'
        ordering = ['price']  # 正序    ['-price'] 倒序





