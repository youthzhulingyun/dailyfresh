from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class TypeInfo(models.Model):
  ttitle = models.CharField(verbose_name='商品类型名',max_length=20)
  isDelete = models.BooleanField(default=False)
  def __str__(self):
    return self.ttitle

class GoodsInfo(models.Model):
  gtitle = models.CharField(verbose_name='商品名',max_length=20)
  gpic = models.ImageField(verbose_name='商品图片',upload_to='df_goods')
  gprice = models.DecimalField(verbose_name='商品价格',max_digits=5,decimal_places=2)
  gunit = models.CharField(verbose_name='商品规格',max_length=20,default='500g')
  gclick = models.IntegerField(verbose_name='点击量')
  gkucun = models.IntegerField(verbose_name='商品库存',)
  gcontent = HTMLField(verbose_name='描述')
  isDelete = models.BooleanField(verbose_name='是否删除',default=False)
  gtype = models.ForeignKey(TypeInfo,verbose_name='商品类型')
  def __str__(self):
    return self.gtitle
