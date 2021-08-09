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
    # api 查詢訂單系統的紀律
    path('api_query_user_order/', api_query_user_order_view)
]
