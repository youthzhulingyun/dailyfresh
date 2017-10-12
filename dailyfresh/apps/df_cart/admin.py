from django.contrib import admin
from .models import *

# Register your models here.
class CartInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id', 'user','goods','count']

admin.site.register(CartInfo,CartInfoAdmin)
