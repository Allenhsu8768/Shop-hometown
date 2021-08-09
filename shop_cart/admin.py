from django.contrib import admin


# Register your models here.
from .models import *

class Shop_user_cart_Admin(admin.ModelAdmin):
    #  user、商品id、商品名稱、商品顏色,商品圖片,商品尺寸,商品數量,商品價格,商品總價格
    list_display = ['user',
                    'user_real_name',
                    'goods',
                    'goods_title',
                    'goods_color',
                    'goods_color_img',
                    'goods_img',
                    'goods_size',
                    'goods_amount',
                    'goods_price',
                    'goods_total_price']

    # 設置後台管理員不可以修改購物車內容 (只能透過用戶,在頁面操作新增刪除)
    readonly_fields = ['user',
                       'goods',
                       'goods_color',
                       'goods_size',
                       'goods_img_url',
                       'goods_amount',
                       'goods_price',
                       'goods_total_price']


    list_filter = ['user', 'goods']








class Pay_send_Admin(admin.ModelAdmin):
    list_display = ['chose_pay', 'send_price']


# 註冊管理
admin.site.register(Shop_user_cart, Shop_user_cart_Admin)
admin.site.register(Pay_send,Pay_send_Admin)