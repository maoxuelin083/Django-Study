from django.db import models

# Create your models here.


class Authors(models.Model):
    name = models.CharField(max_length=32, null=False)


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    b_name = models.CharField(max_length=128, null=False)
    b_author = models.ForeignKey("Authors", on_delete=models.CASCADE)
    b_user = models.ForeignKey("user.Users", on_delete=models.CASCADE)   # 元素删除models.CASCADE  不会造成任何影响
    def __str__(self):
        return "<Book>:id:%s,b_name:%s,b_author:%s,b_user:%s" % (self.id,self.b_name,self.b_author,self.b_user)
