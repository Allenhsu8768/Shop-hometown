from django.db import models

# 2. 導入模塊 mark_safe 讓後台顯示圖片
from django.utils.html import mark_safe

#  導入 setting 中設置 的 media_url 讓後台系統去顯示圖片的路徑
from Shop_hometown.settings import MEDIA_URL



# Create your models here.

# 1. 商品主類別表 (GoodsType)
class GoodsType(models.Model):
    #  商品主名 (Woman、Men、Kid、Baby、Sport)
    title = models.CharField(max_length=30, verbose_name='主類別')

    # 設置內部類
    class Meta():
        #  表名稱
        db_table = 'GoodsType'

        # 設置管理系統 表名稱顯示為 主類別
        verbose_name = '商品主類別'
        verbose_name_plural = verbose_name

    #  設置 __str__
    def __str__(self):
        return self.title

    #  設置 __repr__
    def __repr__(self):
        return '<title%r>' % self.name
    # 增加一個函數方法, 將數據轉為字典
    def to_dict(self):
        dic = {
            'title': self.title,
        }
        return dic



# 2.商品樣式類別表 (GoodsType2)
class GoodsType2(models.Model):
    # 商品樣式
    title = models.CharField(max_length=50,verbose_name='商品樣式類別')

    # 設置內部類
    class Meta():
        # 表名稱
        db_table = 'GoodsType2'

        # 設置管理系統 表名稱 商品樣式類別
        verbose_name = '商品樣式類別'
        verbose_name_plural = verbose_name

    # 設置 __str__
    def __str__(self):
        return self.title

    # 設置 __repr__
    def __repr__(self):
        return '<title % s>' % self.title


#3. 橫幅圖片放置 (Shop_Banner)
class Shop_Banner(models.Model):
    # 橫幅名稱
    title = models.CharField(max_length=30, verbose_name='Banner名稱')
    # 圖片存放路徑
    Banner_Url = models.ImageField(upload_to='static/upload/images/Banners', verbose_name='Banner圖片路徑')
    # 外部關聯,橫幅主打的內容類別(Women、Men、Kid、Baby、Sport)
    GoodsType = models.ForeignKey(GoodsType, verbose_name='主類別', on_delete=models.CASCADE)


    def banner_img(self):
        return mark_safe('<a href="%s%s"><img src="%s%s" width="150px"></a>' % (MEDIA_URL, self.Banner_Url, MEDIA_URL, self.Banner_Url))

    banner_img.short_description = 'Banner廣告'
    banner_img.allow_tags = True

    # 設置內部類
    class Meta():
        # table name
        db_table = 'Shop_Banner'
        #  設置名稱
        verbose_name = '橫幅表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title



# 4.主商品表(關聯 商品樣式表) (多對多, (GoodsType、GoodsType2))
class Goods(models.Model):
    # 1.title 商品名稱
    title = models.CharField(max_length=50, verbose_name='商品名稱')
    # 2.price 商品價格 (最大位數 7 位, 小數位站2 位, 整數位5位
    price = models.DecimalField(max_digits=7, decimal_places=0, verbose_name='商品價格')
    # 3.desc 商品敘述 (先建立欄位,但先不使用,可空白) , 利用 blank 設置 CharField 可為空
    desc = models.CharField(max_length=200, verbose_name='商品敘述', null=True, blank=True)
    # 4.s_desc 商品簡述 (先建立欄位,但先不使用,可空白)
    s_desc = models.CharField(max_length=100, verbose_name='商品簡述', null=True, blank=True)
    # 5.image 圖片存放路徑 (主商品圖存放置 upload_to 中的 images/goods_min(主商品) )
    Images_url = models.ImageField(upload_to='static/upload/images/goods_min', verbose_name='商品圖片路徑')
    # 6. 外部關聯 GoodsType1(主類別表)
    # Django 2.0 版要設置 on_delete = models.CASCADE
    GoodsType = models.ForeignKey(GoodsType, verbose_name='主類別', on_delete=models.CASCADE)
    # 7. 外部關聯 GoodsType2 (商品樣式表)
    GoodsType2 = models.ForeignKey(GoodsType2, verbose_name='商品樣式類別', on_delete=models.CASCADE)
    # 8. 商品按讚次數
    heart = models.IntegerField(verbose_name='愛心次數')
    # 9. 商品上架日期
    goods_put_on = models.DateField(verbose_name='商品上架日期')

    # 10. 商品種類性別 (設置 choices 輸入的值為 M or F)
    #  設置 choices 的元組 (M or F)
    Gender_goods = (('M', 'M'), ('F', 'F'))
    goods_gender = models.CharField(max_length=1, verbose_name='商品種類性別', choices=Gender_goods, null=False)

    # 11. 商品型號 (關連到 商品其他規格樣式(顏色、尺寸))
    goods_pattern = models.CharField(max_length=20, verbose_name='商品型號',null=True, blank=True)

    # 12. 商品是否上架 (is_Active) , 預設值是 True
    is_Active = models.BooleanField(default=True, verbose_name='是否上架')

    # 設置 function 讓 後台系統多一個欄位顯示 圖片的資訊
    def imag_data(self):
        return mark_safe('<a href="%s%s"><img src="%s%s" width="80px"></a>' % (MEDIA_URL, self.Images_url, MEDIA_URL, self.Images_url))

    # 調用 imag_data 且且設置欄位的名稱為 "商品圖片"
    imag_data.short_description = '商品圖片'
    imag_data.allow_tags = True


    # 設置內部類
    class Meta():
        # 表名稱設置 Goods
        db_table = 'Goods'

        # 設置管理系統 表名稱 商品樣式類別
        verbose_name = '主商品表'
        verbose_name_plural = verbose_name



    # 設置 __repr__
    def __repr__(self):
        return '<title %s>' % self.title



    # 設置 __str__
    def __str__(self):
        return str(self.id)


