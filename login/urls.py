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
    #  login 頁面
    path('', login_views),



    # 前端 請求數據,檢查 session 和 cookie 的值判斷是否登入
    # 路由 check_login
    path('check_login/', check_login_view),

    # 點選登出 sign_out
    path('sign_out/', sign_out_view),

    # add goods_heart and track_goods
    path('api_track_goods/', api_add_track_goods),

    #  會員中心介面 api
    # user_member_center,點擊會員中心 將新品展示
    path('user_member_center/', user_member_center_views),

    # 1.api 會員資料查詢
    path('api_user_member_msg/', api_user_member_views),

    # 2.重新發送驗證信
    path('api_send_user_mail/', api_send_user_mail),

    # 3.修改會員資料

    # 4.追蹤商品清單查詢
    path('api_user_track_goods_msg/',api_user_track_goods_view),
    # 5.訂單記錄查詢
]
