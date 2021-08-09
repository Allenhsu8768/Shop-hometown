from django.db import models

# Create your models here.

from Shop_hometown import settings


# 導入模塊
from index.models import *
from register.models import *


# 2. 導入模塊 mark_safe 讓後台顯示 商品顏色圖片
from django.utils.html import mark_safe


# user_track_goods(會員追蹤商品表)
class User_track_goods(models.Model):
    # user_id 外部關聯
    users = models.ForeignKey(User_Member, verbose_name='會員名稱',on_delete=models.CASCADE)

    # goods_id 外部關聯
    goods = models.ForeignKey(Goods, verbose_name='追蹤商品', on_delete=models.CASCADE)


    class Meta():
        db_table = 'user_track_goods'
        verbose_name = '會員追蹤清單表'
        verbose_name_plural = verbose_name


    # 設置追蹤的商品名稱
    def goods_title(self):
        return mark_safe('<b>%s</b>' % self.goods.title)
    goods_title.short_description = '主商品名稱'
    goods_title.allow_tags = True

    # 設置追蹤的商品圖片
    def goods_img(self):
        return mark_safe('<a href=%s%s><img src="%s%s" width="80px;"></a>' % (MEDIA_URL,self.goods.Images_url,MEDIA_URL,self.goods.Images_url))

    # 主商品欄位顯示
    goods_img.short_description = '主商品圖'
    goods_img.allow_tags = True



    def __str__(self):
        return self.users.realname

    def __repr__(self):
        return self.users.realname

