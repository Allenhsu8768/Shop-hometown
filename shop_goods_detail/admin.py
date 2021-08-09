from django.contrib import admin

# Register your models here.

# 導入 model 中的 類
from .models import *

class Goods_color_Admin(admin.ModelAdmin):
    # 顯示的欄位
    list_display = ['goods', 'goods_type','goods_type2','goods_title','image_goods','goods_color','image_goods_color', 'goods_img_1', 'goods_img_2', 'goods_img_3', 'goods_img_4', 'goods_img_5']

    list_display_links = ['goods_title','goods']
    # 設置可搜尋的欄位
    search_fields = ['goods_title']

    # # 增加過濾器 (把顏色加入過濾器中)
    list_filter = ['goods_type', 'goods_type2', 'goods']


# 設置新增後台管理的類
admin.site.register(Goods_color, Goods_color_Admin)
