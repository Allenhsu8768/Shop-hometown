"""Shop_hometown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#  index (Shop_hometown 首頁)
from django.contrib import admin
from django.urls import path, include

# 導入試圖處理模塊
from .views import *


urlpatterns = [
    #  cart 頁面
    path('', cart_views),

    #  商品頁面 your cart 串接資料 api
    #  用戶點及新增至購物車的 api
    path('add_goods_in_cart/', api_add_goods_in_cart),
    #  用戶加入購物車商品數據 api
    path('query_goods_in_cart/', api_query_user_goods),
    #  用戶點擊刪除商品數據 api
    path('delete_goods_in_cart/', api_delet_user_goods),
    #  購物車頁面結帳 api 傳接資料
    path('cart_goods_check/', api_cart_goods_check),
    #  購物車頁面, 進行數量的操作
    path('cart_goods_amount_change/', api_goods_amount_change),

    #  結帳支付方式數據
    path('cart_goods_pay_send', api_cart_pay_send),

]
