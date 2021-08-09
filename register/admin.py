from django.contrib import admin




# Register your models here.
# 導入 model

from .models import *


#  設置 後台管理 注冊國家表
class Country_Admin(admin.ModelAdmin):
    #  顯示欄位 counrty_name
    list_display = ['id', 'Country_name']


#  設置後台管理 註冊國家表
class City_Admin(admin.ModelAdmin):
    #  顯式欄位 City_name
    list_display = ['id', 'City_name', 'Country']

# #  設置會員帳戶後台管理
class User_Member_Admin(admin.ModelAdmin):
    #  顯示會員資訊欄位
    list_display = [
        'id',
        'user_name',
        'realname',
        'email',
        'birthday',
        'user_age',
        'phone_number',
        'registered_time',
        'is_Active',
        'authority',
        'country',
        'city',
        ]


    # 會員新增資料只能讓用戶新增,管理員不得修改
    readonly_fields = [
        'id',
        'user_name',
        'realname',
        'email',
        'birthday',
        'phone_number',
        'registered_time',
        'is_Active',
        'authority',
        'country',
        'city',
        'password',
        'send_emaill_time',
        'check_emaill_time']

    # 篩選
    list_filter = ['realname', 'user_age', 'country', 'city', 'is_Active']

# 設置後台管理
admin.site.register(Country, Country_Admin)
admin.site.register(City, City_Admin)
admin.site.register(User_Member, User_Member_Admin)

