from django.contrib import admin
from .models import *

# Register your models here.
class OrderInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['oid', 'user']

class OrderDetailInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id', 'order','goods']

admin.site.register(OrderInfo,OrderInfoAdmin)
admin.site.register(OrderDetailInfo,OrderDetailInfoAdmin)
