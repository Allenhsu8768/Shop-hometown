from django.contrib import admin


#  導入 models.py 的 實體類
from .models import *

# Register your models here.

#  1. GoodsType(商品主類別表)
#  創建 高級管理 定義一個 GoodsTypeAdmin
class GoodsTypeAdmin(admin.ModelAdmin):
    # 1.定義 顯示的欄位字段 (title)
    list_display = ['title']
    # 2.添加允許被搜索的欄位
    search_fields = ['title']


#  2.GoodsType2(商品樣式類別表)
class GoodsType2Admin(admin.ModelAdmin):
    # 1.定義 顯示的欄位字段(title,及主類別關聯(Women等...))
    list_display = ['title']
    # 2.添加被搜尋欄位
    search_fields = ['title']


#  3.Shop_Banner(商城橫幅表)
class ShopBannerAdmin(admin.ModelAdmin):
    # 1. 顯示 爛為字段
    list_display = ['title', 'GoodsType', 'Banner_Url', 'banner_img']



# 4.Goods(主商品表)
class GoodsAdmin(admin.ModelAdmin):
    # 1.定義 顯示欄位字段
    list_display = ['id', 'title', 'price', 's_desc', 'Images_url', 'imag_data', 'GoodsType', 'GoodsType2', 'heart', 'goods_put_on', 'goods_gender', 'goods_pattern','is_Active']

    # 2.添加被搜尋的欄位
    search_fields = ['title']

    # 3.根據上架時間篩選
    # date_hierarchy = 'goods_put_on'

    # 4.增加過濾器
    list_filter = ['GoodsType', 'GoodsType2', 'goods_gender','goods_put_on']


#註冊 應用 index , models.py 中的實體類

# 1. 商品主類別表 (一般、高級管理)
admin.site.register(GoodsType, GoodsTypeAdmin)

# 2.商品樣式類別表
admin.site.register(GoodsType2, GoodsType2Admin)


# 3.橫幅樣式表
admin.site.register(Shop_Banner, ShopBannerAdmin)

# 4.主商品表
admin.site.register(Goods,GoodsAdmin)


#  修改 django 後台管理標題
admin.site.site_title = 'Hometown後台系統'
admin.site.site_header = 'Hometown後台系統'