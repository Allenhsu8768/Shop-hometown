from django.contrib import admin

# Register your models here.
from .models import *


class Order_info_detail_Admin(admin.ModelAdmin):

    list_display = ['user',
                    'user_real_name',
                    'goods',
                    'goods_title',
                    'goods_img',
                    'goods_color',
                    'goods_color_img',
                    'goods_size',
                    'goods_amount',
                    'goods_price',
                    'goods_total_price',
                    'orders',
                    'order_time',]

    list_filter = ['user',
                   'order_time',
                   'orders',]

    readonly_fields = ['user',
                       'goods',
                       'goods_color',
                       'goods_size',
                       'goods_amount',
                       'goods_price',
                       'goods_total_price',
                       'orders',
                       'order_time',
                       'goods_img_url',]

class Order_info_Admin(admin.ModelAdmin):
    list_display = ['user',
                    'recipient_name',
                    'recipient_phone_number',
                    'recipient_address',
                    'pay',
                    'order_total_price',
                    'order_time',
                    'order_number',
                    'order_status',
                    'order_check_time',]

    list_filter = ['user',
                   'order_time',
                   'order_number',
                   'order_status']

    # 設置後台管理員不可以修改購物車內容 (只能透過用戶,在頁面操作新增刪除)
    readonly_fields = ['user',
                       'recipient_name',
                       'recipient_phone_number',
                       'recipient_address',
                       'pay',
                       'order_total_price',
                       'order_time',
                       'order_number',]


# 註冊應用
admin.site.register(Order_info_detail, Order_info_detail_Admin)
admin.site.register(Order_info, Order_info_Admin)