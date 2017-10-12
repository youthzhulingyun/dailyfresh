from django.contrib import admin
from .models import *

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id', 'uname']

admin.site.register(UserInfo,UserInfoAdmin)
