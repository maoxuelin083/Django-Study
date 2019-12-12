from django.core import validators
from django.db import models

# Create your models here.


class BookDemo(models.Model):
    title = models.CharField(max_length=100)
    page = models.IntegerField()
    price = models.FloatField(validators=[validators.MaxValueValidator(limit_value=1000)])


class UserDemo(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    telephone = models.CharField(max_length=11, validators=[validators.RegexValidator(r'1[3456789]\d{9}')])
