from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "<User>:(id:%s, name:%s)" %(self.id, self.name)


class UserExtendsion(models.Model):
    school = models.CharField(max_length=100)
    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name="extendsion")

    def __str__(self):
        return "<UserExtendsion>:(id:%s, school:%s, user:%s)" %(self.id, self.school, self.user)