from django.db import models

# Create your models here.
class OrderInfo(models.Model):
    oid = models.CharField(verbose_name='订单编号',max_length=20,primary_key=True)
    user = models.ForeignKey('df_user.UserInfo',verbose_name='订单用户')
    odate = models.DateTimeField(verbose_name='订单时间',auto_now=True)
    oIsPay = models.BooleanField(verbose_name='订单是否支付',default=False)
    ototal = models.DecimalField(verbose_name='订单总价',max_digits = 6,decimal_places=2)
    oaddress = models.CharField(verbose_name='订单地址',max_length=150)
    def __str__(self):
        return self.oid

class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodsInfo',verbose_name='商品')
    order = models.ForeignKey('OrderInfo',verbose_name='订单')
    price = models.DecimalField(verbose_name='订单价格',max_digits = 4,decimal_places=2)
    count = models.IntegerField(verbose_name="数量")
    def __str__(self):
        return self.goods.gtitle