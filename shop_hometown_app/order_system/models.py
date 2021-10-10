from django.db import models

# Create your models here.

# 引入其他應用程式 model
from register.models import *
from shop_cart.models import *
from index.models import *



#  訂貨單
class Order_info(models.Model):
    # 會員id
    user = models.ForeignKey(User_Member, verbose_name='用戶名稱', on_delete=models.CASCADE)

    # 收件人姓名
    recipient_name = models.CharField(max_length=20, verbose_name='收件人姓名')

    # 收件人電話
    recipient_phone_number = models.CharField(max_length=100, verbose_name='收件人電話')

    # 收件人地址
    recipient_address = models.CharField(max_length=100, verbose_name='寄送地址')

    # pay 支付及寄送方式
    pay = models.ForeignKey(Pay_send, verbose_name='支付方式及運送方式', on_delete=models.CASCADE)

    # 訂單金額( 加 pay 的運費金額)
    order_total_price = models.IntegerField(verbose_name='訂單金額')

    # 訂單明細(和訂單明細為 一對一關係)
    # order_detial = models.OneToOneField(Order_info_detail, verbose_name='訂單明細', on_delete=models.CASCADE)

    # 訂單日期
    order_time = models.DateField(verbose_name='訂單日期')

    # 訂單編號
    order_number = models.CharField(max_length=30, verbose_name='訂單編號', null=True, blank=True)

    # 訂單處理狀態
    order_status = models.BooleanField(verbose_name='訂單處理狀態', default=False)
    # 訂單確認處理日期
    order_check_time = models.DateField(verbose_name='訂單確認日期', null=True)

    class Meta():
        db_table = 'Order_info'
        verbose_name = '用戶訂單'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.order_number

    def __str__(self):
        return self.order_number


#  訂單明細
class Order_info_detail(models.Model):
    # 會員 id
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

    # 9.訂單編號
    orders = models.ForeignKey(Order_info, verbose_name='訂單編號', on_delete=models.CASCADE, null=True)

    #10.訂單日期
    order_time = models.DateField(verbose_name='訂單日期', null=True)

    class Meta():
        db_table = 'Order_info_detail'
        verbose_name = '用戶訂單明細'
        verbose_name_plural = verbose_name

    # 設置透台顯示商品名稱
    def goods_title(self):
        return mark_safe('<b>%s</b>' % self.goods.title)

    goods_title.short_description = '商品名稱'
    goods_title.allow_tags = True

    #  商品圖片
    def goods_img(self):
        return mark_safe('<a href="%s%s"><img src="%s%s" width="80px"></a>' % (MEDIA_URL, self.goods_img_url, MEDIA_URL, self.goods_img_url))

    goods_img.short_description = '商品圖片'
    goods_img.allow_tags = True

    # 用戶名稱
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
        return '訂單明細編號: %d' % self.id

    def __str__(self):
        return '訂單明細編號: %d' % self.id