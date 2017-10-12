from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(verbose_name='用户名',max_length=20)
    upwd = models.CharField(verbose_name='密码',max_length=40)
    uemail = models.CharField(verbose_name='电子邮箱',max_length=30)
    uconsignee = models.CharField(verbose_name='收货人姓名',max_length=20,default="")
    uaddress = models.CharField(verbose_name='地址',max_length=100,default="")
    upostcode = models.CharField(verbose_name='邮编',max_length=6,default="")
    uphone =  models.CharField(verbose_name='电话',max_length=11,default="")
    def __str__(self):
        return self.uname
