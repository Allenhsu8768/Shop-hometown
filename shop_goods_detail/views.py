from django.shortcuts import render, redirect



from django.http import HttpResponse
# Create your views here.

# 將商品做序列化 把查找 的 QuerySet 處理成 json 字典格式字串
from django.core import serializers
#  引入 model
from .models import *

#  引入 index 主商品表
from index.models import *

#  商品詳細內容頁面
def detail_goods_views(request):
    #  獲取 USER 點擊的商品 ID

    pid = request.GET['GOODS_ID']

    # 設置組裝商品資訊列表
    goods_detial_msg_list = []
    # 先查找 Goods 主商品表的資訊
    goods_detial_info = Goods.objects.get(id=pid)
    #  透過一對多關聯, 透過 goods_color_set 查找 商品顏色資訊
    goods_color_infos = goods_detial_info.goods_color_set.all()

    # 如果點擊購物車有將顏色傳入,則查找此顏色的圖片
    if 'GOODS_COLOR' in request.GET:
        user_goods_color = request.GET['GOODS_COLOR']
        goods_detial_info = Goods_color.objects.filter(goods_id=pid, goods_color=user_goods_color)[:1]
    else:
        # 如果沒有則表示單存點擊主要商品
        # 此查詢是點選商品後根據 goods_id 來查找商品的資訊(只查找一件)
        goods_detial_info = Goods_color.objects.filter(goods_id=pid)[:1]

    # 透過 local 封裝 字典, 讓模板渲染字典的值
    return render(request, 'shop_goods_detail.html', locals())



# 前端透過 $.get 方法 前台發送處理數據方法 將顏色更換後的查找的資訊傳回前端
def ajax_goods_color_change(request):


    #  獲取用戶點擊的顏色值
    goods_id = request.GET['Goods_id']
    color = request.GET['color']

    # 查找顏色表資訊的值
    goods_color_msg = Goods_color.objects.filter(goods_id=goods_id, goods_color=color)
    goods_color_msg_json = serializers.serialize('json', goods_color_msg)

    # 將值返回給,點擊的顏色資訊 response 給前端去做整理
    return HttpResponse(goods_color_msg_json)


