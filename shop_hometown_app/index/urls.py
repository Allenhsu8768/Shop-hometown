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
    #  首頁
    path('', index_views),

    # ajax_index_goods_data
    path('ajax_index_data/', ajax_index_data_goods_views),


    #  Woman 點選跳轉 woman 頁面
    path('Women/', include('woman.urls')),
    #  Men
    path('Men/', include('men.urls')),
    #  kid
    path('Kid/', include('kid.urls')),
    #  baby
    path('Baby/', include('baby.urls')),
    # sport
    path('Sport/', include('sport.urls')),
    # login
    path('login/', include('login.urls')),
    # register
    path('register/', include('register.urls')),
    # 會員留言
    path('shop_gbook/', include('shop_gbook.urls')),
    # 商城說明
    path('shop_description/', include('description.urls')),
    # cart
    path('shop_cart/', include('shop_cart.urls')),
    # shop_goods_detail
    path('shop_goods_detail/', include('shop_goods_detail.urls')),
    # order_system
    path('order_system/', include('order_system.urls')),

]
