from django.shortcuts import render
from django.http import HttpResponse


#  導入 index 中 model (做查詢)
from .models import *
#  導入 json 模塊 將字典轉為字符串
import json

# 將商品做序列化 把查找 的 QuerySet 處理成 json 字典格式字串
from django.core import serializers

from Shop_hometown.settings import MEDIA_ROOT

# Create your views here.

#  1.首頁頁面
def index_views(request):
    # 如果用戶 有點選記住密碼,則透過 cookiK 產生 session 呈現登入狀態
    if 'uip' in request.COOKIES and 'username' in request.COOKIES and 'user_real_name' in request.COOKIES:
        # 獲取 Cookie 的值
        uid = request.COOKIES['uid']
        user_name = request.COOKIES['username']
        user_real_name = request.COOKIES['user_real_name']

        request.session['uid'] = uid
        request.session['username'] = user_name
        request.session['user_real_name'] = user_real_name
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


#  首頁商品資訊處理 透過 前端的 ajax技術 ,將商品資訊及橫幅數據,傳給前端模板
def ajax_index_data_goods_views(request):
    # 設置一個列表組裝商品資訊
    all_list = []
    # 1. 查詢所有的商品類型(Women、Men、Kid、Baby、Sport)
    types = GoodsType.objects.all()
    # 2. 循環遍歷 type 的值
    for i in types:
        types_json = json.dumps(i.to_dict())
        # 1.獲取 Banner 數據
        goods_banner = i.shop_banner_set.all()
        #  將 goods_banner 中的數據 透過 serializers 轉為 json 格式字符串
        goods_banner_json = serializers.serialize('json',goods_banner)

        # 2.獲取 filter後 ,goods 數據
        # 獲取 type 類型下 愛心最多的 6 個數據 (因為是一(類別)對多(商品),利用goods_set,做關聯建立)
        goods_list = i.goods_set.filter(is_Active=True).order_by('-heart')[0:6]
        goods_json = serializers.serialize('json', goods_list)

        # 將上面查找獲取的數據奘入字典中
        dic = {
            # 1.商品類別
            "type": types_json,
            # 2.橫幅數據
            "banner": goods_banner_json,
            # 3.商品數據
            "goods": goods_json,
        }
        # 再將字典追加到 all_list 中
        all_list.append(dic)
    return HttpResponse(json.dumps(all_list))











