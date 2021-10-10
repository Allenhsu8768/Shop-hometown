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
    # #  register 頁面
    path('', register_views),

    #  以下為前端發送請求,後端處理數據,response 給前端訊息
    # 透過 前端發送數據請求,後端處理數據,返回 response 國家數據信息給前端
    path('ajax_country_msg/', ajax_country_msg_resp),

    # 透過 前端發送數據請求,後端處理數據,返回 response 地區數據信息給前端
    path('ajax_city_msg/', ajax_city_try_msg_resp),

    # 透過 前端發送的帳號訊息,進行驗證是否存在
    path('post_user_name_msg/', post_user_name_msg_resp),

    # 透過 前端發送的信箱信息,進行驗證是否存在
    path('post_user_email_msg/', post_user_email_msg_resp),

    # 註冊用戶信箱驗證
    path('active_user/<str:token>', check_user_info),

]
