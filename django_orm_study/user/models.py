from django.db import models

# Create your models here.


class Users(models.Model):
    u_name = models.CharField(max_length=32)