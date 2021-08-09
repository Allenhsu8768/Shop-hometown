from django.contrib import admin

# Register your models here.
from .models import *

class User_track_goods_Admin(admin.ModelAdmin):
    list_display = ['users',
                    'goods',
                    'goods_title',
                    'goods_img',]

    list_filter = ['users',
                   'goods',]


# 註冊後台應用
admin.site.register(User_track_goods,User_track_goods_Admin)