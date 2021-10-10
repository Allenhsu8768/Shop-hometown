from django.shortcuts import render

# Create your views here.

# 導入 HttpResponse
from django.http import HttpResponse, JsonResponse

#  導入 index 中的 model 模塊
from index.models import *
from login.models import *

# 將商品做序列化 把查找 的 QuerySet 處理成 json 字典格式字串
from django.core import serializers


#  kid 商品頁面
def kid_goods_views(request):
    return render(request, 'kid.html')


# #  點擊 kid 商品資訊處理 透過 前端的 ajax技術 ,將商品資訊及橫幅數據,傳給前端模板
def ajax_kid_goods_info_views(request):
    # 接收 根據用戶點擊不同的 商品樣式,回傳不同的資料頁面
    kid_goods_click_info = request.GET['GOODS']
    # 接收 根據用戶點擊不同的 商品樣式,回傳不同的資料頁面
    # 根據接收到的值傳數據給前端,ALL_GOODS 則表示 需要kid 全部商品的資料


    # 設置登入狀態顯示,(將愛心顯示)
    login_status = 0


    goods_msg_login_dict = {
        'login_status': login_status,
    }


    if 'user_name' in request.session and 'uid' in request.session:
        uid = request.session['uid'][0]
        user_track_goods = User_track_goods.objects.filter(users_id=uid)
        goods_msg_login_dict['login_status'] = 1
        goods_msg_login_dict['login_track_goods'] = [i.goods_id for i in user_track_goods]



    #  1. All Goods
    if kid_goods_click_info == 'ALL_GOODS':
        #  查找 kid 的所有商品 加入商品排序(根據 1.日期(大到小) 、 2.愛心數來排序(New 和 like))
        kid_info = Goods.objects.filter(GoodsType=3, is_Active=True).order_by('-goods_put_on', '-heart')
        # 將查找的 集合 做序列化
        kid_goods_json = serializers.serialize('json', kid_info)

    #  2. 'New_Arrival 所有商品(利用 filter 去篩選 Goods 的表(根據日期篩選))'
    elif kid_goods_click_info =='New_Arrival':
        kid_info = Goods.objects.filter(GoodsType=3, is_Active=True, goods_put_on__range=['2021-03-01', '2021-03-31'])
        kid_goods_json = serializers.serialize('json', kid_info)

    #  3. Top 的所有商品(利用 filter 去篩選 Goods 的表(篩選 愛心最多排序前25個商品))
    elif kid_goods_click_info == 'Top':
        kid_info = Goods.objects.filter(GoodsType=3, is_Active=True).order_by('-heart')[0:24]
        kid_goods_json = serializers.serialize('json', kid_info)


    #  4. 查詢 舊商品(且heart 不高的商品)
    elif kid_goods_click_info == 'Coat_Jackets':
        kid_info = Goods.objects.filter(GoodsType=3, GoodsType2=1, is_Active=True).order_by('heart', 'goods_put_on')[0:6]
        kid_goods_json = serializers.serialize('json', kid_info)

    # 5.
    elif kid_goods_click_info == 'Clothes':
        kid_info = Goods.objects.filter(GoodsType=3, GoodsType2=2, is_Active=True).order_by('heart', 'goods_put_on')[0:6]
        kid_goods_json = serializers.serialize('json', kid_info)

    # 6.
    elif kid_goods_click_info == 'Trousers':
        kid_info = Goods.objects.filter(GoodsType=3, GoodsType2=3, is_Active=True).order_by('heart', 'goods_put_on')[0:4]
        kid_goods_json = serializers.serialize('json', kid_info)


    elif kid_goods_click_info == 'Shirt':
        kid_info = Goods.objects.filter(GoodsType=3, GoodsType2=5, is_Active=True).order_by('heart', 'goods_put_on')[0:4]
        kid_goods_json = serializers.serialize('json', kid_info)

    goods_msg_login_dict['goods_msg'] = kid_goods_json

    return JsonResponse(goods_msg_login_dict)
