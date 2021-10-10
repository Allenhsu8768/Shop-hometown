from django.db import models


#  因為 Goods 商品表設置在 index.model 所以要導入
from index.models import *

# 2. 導入模塊 mark_safe 讓後台顯示 商品顏色圖片
from django.utils.html import mark_safe




# Create your models here.
from Shop_hometown.settings import MEDIA_URL


#  商品顏色表
class Goods_color(models.Model):
    # 商品 id , 引用 Goods 關聯中的 Goods_id
    #  Django 2.0 版要設置 on_delete = models.CASCADE
    goods = models.ForeignKey(Goods, verbose_name='商品型號', on_delete=models.CASCADE, default=True)
    # 外部關聯商品主類別
    goods_type = models.ForeignKey(GoodsType, verbose_name='商品主類別', on_delete=models.CASCADE,default=True)
    # 外部關聯 商品樣式
    goods_type2 = models.ForeignKey(GoodsType2, verbose_name='商品樣式', on_delete=models.CASCADE, default=True)
    # 商品名稱
    goods_title = models.CharField(max_length=60, verbose_name='商品名稱')
    # 商品顏色_color 商品顏色
    goods_color = models.CharField(max_length=30, verbose_name='商品顏色')
    # 商品顏色小圖路徑
    goods_color_img = models.ImageField(upload_to='static/upload/images/goods_color', verbose_name='商品圖片顏色')


    #  最多存放 5 張圖片 顯示 (因為有些商品其他顏色展示圖較少,所以設置為可空白)
    #  圖片 1
    goods_color_img_1 = models.ImageField(upload_to='static/upload/images/goods_other_color_img', verbose_name='商品圖片1', null=True, blank=True)
    #  圖片 2
    goods_color_img_2 = models.ImageField(upload_to='static/upload/images/goods_other_color_img', null=True, verbose_name='商品圖片2', blank=True)
    #   圖片 3
    goods_color_img_3 = models.ImageField(upload_to='static/upload/images/goods_other_color_img', null=True, verbose_name='商品圖片3', blank=True)
    #   圖片 4
    goods_color_img_4 = models.ImageField(upload_to='static/upload/images/goods_other_color_img', null=True, verbose_name='商品圖片4', blank=True)
    #   圖片 5
    goods_color_img_5 = models.ImageField(upload_to='static/upload/images/goods_other_color_img', null=True, verbose_name='商品圖片5', blank=True)
    #
    # 設置 function 讓 後台系統多一個欄位顯示 圖片的資訊
    def image_goods_color(self):
        return mark_safe('<a href="%s%s"><img src="%s%s" width="40px;"></a>' % (MEDIA_URL, self.goods_color_img, MEDIA_URL, self.goods_color_img))

    # 主商品顯示欄位
    def image_goods(self):
        return mark_safe('<a href="%s%s"><img src="%s%s" width="80px;"></a>' % (MEDIA_URL, self.goods_color_img_1, MEDIA_URL, self.goods_color_img_1))

    # 主商品欄位顯示
    image_goods.short_description = '主商品圖'
    image_goods.allow_tags = True

    # 設置 後台顏色圖
    # 調用 imag_data 且且設置欄位的名稱為 "商品圖片", 利用 short_description 設置 新增的欄位 名稱
    image_goods_color.short_description = '商品顏色圖片'
    image_goods_color.allow_tags = True
    #
    # #  圖片 1
    def goods_img_1(self):
        if self.goods_color_img_1:
            return mark_safe('<a href="%s%s"><img src="%s%s" width="80px;"></a>' % (MEDIA_URL, self.goods_color_img_1, MEDIA_URL, self.goods_color_img_1))
        else:
            return mark_safe('')
    #  圖片 2
    def goods_img_2(self):
        if self.goods_color_img_2:
            return mark_safe('<a href="%s%s"><img src="%s%s" width="80px;"></a>' % (MEDIA_URL, self.goods_color_img_2, MEDIA_URL, self.goods_color_img_2))
        else:
            return mark_safe('')
    #  圖片 3
    def goods_img_3(self):
        if self.goods_color_img_3:
            return mark_safe('<a href="%s%s"><img src="%s%s" width="80px;"></a>' % (MEDIA_URL, self.goods_color_img_3, MEDIA_URL, self.goods_color_img_3))
        else:
            return mark_safe('')
    #  圖片 4
    def goods_img_4(self):
        if self.goods_color_img_4:
            return mark_safe('<a href="%s%s"><img src="%s%s" width="80px;"></a>' % (MEDIA_URL, self.goods_color_img_4, MEDIA_URL, self.goods_color_img_4))
        else:
            return mark_safe('')
    #  圖片 5
    def goods_img_5(self):
        if self.goods_color_img_5:
            return mark_safe('<a href="%s%s"><img src="%s%s" width="80px;"></a>' % (MEDIA_URL, self.goods_color_img_5, MEDIA_URL, self.goods_color_img_5))
        else:
            return mark_safe(''
                             '')
    #
    # # 設置 商品顏色圖片
    # # 調用 imag_data 且且設置欄位的名稱為 "商品圖片"


     # 商品圖片 1
    goods_img_1.short_description = '商品圖片1'
    goods_img_1.allow_tags = True

    # 商品圖片 2
    goods_img_2.short_description = '商品圖片2'
    goods_img_2.allow_tags = True

    # 商品圖片 3
    goods_img_3.short_description = '商品圖片3'
    goods_img_3.allow_tags = True

    # 商品圖片 4
    goods_img_4.short_description = '商品圖片4'
    goods_img_4.allow_tags = True

    # 商品圖片 5
    goods_img_5.short_description = '商品圖片5'
    goods_img_5.allow_tags = True


    class Meta():
        # 設置資料庫表名稱
        db_table = 'Goods_color'

        # 設置管理系統 表名稱 商品顏色表
        verbose_name = '商品顏色表'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return '<商品名稱:%r>' % self.goods_title

    def __str__(self):
        return str(self.id)



