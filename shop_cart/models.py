from django.db import models

# Create your models here.
# 引入 register 的 model (user_member)
from register.models import *
from index.models import *
from shop_goods_detail.models import *

# 新增後台欄位
# 2. 導入模塊 mark_safe 讓後台顯示 商品名稱
from django.utils.html import mark_safe


# 導入 setting 中的 meida 路徑
from Shop_hometown.settings import MEDIA_URL


# 設置 購物車欄位
class Shop_user_cart(models.Model):

    #  以下欄位設置都是根據用戶點擊加入購物車資訊
    # 1.用戶id,外部關連到 User_member (透過關聯查詢可以查詢到用戶的資訊)
    user = models.ForeignKey(User_Member, verbose_name='用戶名稱', on_delete=models.CASCADE)

    # 2.商品id,外部關連到 Goods
    goods = models.ForeignKey(Goods, verbose_name='商品編號', on_delete=models.CASCADE)

    # 3.商品顏色
    goods_color = models.CharField(max_length=20, verbose_name='商品顏色')

    # 4.商品尺寸
    goods_size = models.CharField(max_length=4, verbose_name='商品尺寸')

    # 5.選擇顏色的商品圖
    goods_img_url = models.CharField(max_length=100, verbose_name='商品圖')

    # 6.商品數量
    goods_amount = models.IntegerField(verbose_name='商品數量')

    # 7.商品價格
    goods_price = models.IntegerField(verbose_name='商品價格')

    # 8.商品總價格
    goods_total_price = models.IntegerField(verbose_name='商品總價格')



    #  設置 meta
    class Meta():
        # 設置欄位名
        db_table = 'Shop_user_cart'

        verbose_name = '用戶購物車商品表'
        verbose_name_plural = verbose_name


    # 設置透台顯示商品名稱
    def goods_title(self):
        return mark_safe('<b>%s</b>' % self.goods.title)

    goods_title.short_description = '商品名稱'
    goods_title.allow_tags = True

    # 設置後台用戶點擊顯示商品圖片


    def goods_img(self):
        return mark_safe('<a href="%s%s"><img src="%s%s" width="80px"></a>' % (MEDIA_URL, self.goods_img_url, MEDIA_URL, self.goods_img_url))

    goods_img.short_description = '商品圖片'
    goods_img.allow_tags = True


    def user_real_name(self):
        return mark_safe('<b>%s</b>' % self.user.realname)

    user_real_name.short_description = '姓名'
    user_real_name.allow_tags = True


    # 先設置好小圖顏色的 url
    def goods_color_img(self):
        return mark_safe('<a href="%s%s"><img src="%s%s" style="width:30px; height:30px; border-radius:15px; "></a>' % (
            MEDIA_URL, Goods_color.objects.get(goods_color=self.goods_color, goods_id=self.goods.id).goods_color_img,
            MEDIA_URL, Goods_color.objects.get(goods_color=self.goods_color, goods_id=self.goods.id).goods_color_img))

    goods_color_img.short_description = '商品顏色圖片'
    goods_color_img.allow_tags = True

    def __repr__(self):
        return '用戶名稱:%r' % self.user.realname

    def __str__(self):
        return self.user.realname


# 設置支付方式
class Pay_send(models.Model):
    # 選擇的付款方式及配送方式
    chose_pay = models.CharField(max_length=50, verbose_name='支付配送方式')

    # 運費
    send_price =models.IntegerField(verbose_name='運費金額')

    class Meta():
        db_table = 'Pay_Send'
        verbose_name = '支付方式表'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return '<支付方式 %r >' % self.chose_pay

    def __str__(self):
        return self.chose_pay


