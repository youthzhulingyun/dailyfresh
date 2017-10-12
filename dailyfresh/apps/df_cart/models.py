from django.db import models

# Create your models here.
class CartInfo(models.Model):
    user = models.ForeignKey('df_user.UserInfo',verbose_name='用户名')
    goods = models.ForeignKey('df_goods.GoodsInfo',verbose_name='商品',)
    count = models.IntegerField(verbose_name='数量')
    def __str__(self):
        return self.user.uname
