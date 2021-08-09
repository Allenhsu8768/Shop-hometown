from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse

# Create your views here.

import json

#  導入 model
from .models import *
from order_system.models import *

# 載入 serializer 做數據的序列化
from django.core import serializers

# 載入 Sum 加總 ,購物車商品數量和數據
from django.db.models import Sum,Q

# 導入 time 模塊
import time

#  購物車及結帳頁面
def cart_views(request):
    if request.method == 'GET':
        # 如果是 get 請求,則判斷用戶是否登入
        if 'uid' in request.session and 'user_real_name' in request.session:
                resp = render(request, 'shop_cart.html')
                return resp
        #  如果未登入,訪問則返回首頁
        else:
            return redirect('/')
    #  提交購物車資訊 POST 請求數據
    elif request.method == 'POST':
        if 'uid' in request.session and 'user_real_name' in request.session:
            uid = request.session['uid'][0]
            # 查找購物車內的商品 (購物車商品數量已連動修改價格,所以不需要比對價格,直接新增到訂單明細中)
            user_cart_msg = Shop_user_cart.objects.filter(user_id=uid)

            # 1.收件人姓名
            name = request.POST['recipient_name']
            # 2.收件人號碼
            phone_number = request.POST['recipient_phone_number']
            # 3.收件人地址
            address = request.POST['recipient_address']

            # 4.處理訂單購物車總金額
            # 計算訂單購物車總金額 (購物車商品內金額 + 運費)
            user_total_price = user_cart_msg.aggregate(total_price=Sum('goods_total_price'))
            # 透過 user 選擇的 付款方式,運費加總
            user_pay_msg = Pay_send.objects.get(chose_pay=request.POST['send_pay'])
            # 加總後金額
            order_total_price_count = user_total_price['total_price'] + user_pay_msg.send_price

            # 5.處理訂單流水號 訂單編號為當天日期+秒 (年、月、時、分、秒)
            create_order_number_date = time.localtime()
            crete_order_number = str(time.strftime('%Y%m%d%H%M%S', create_order_number_date))

            # 6.訂單日期
            create_order_date = time.strftime('%Y-%m-%d', create_order_number_date)

            # 透過上面建立的對象,進行存儲
            add_Order_info = Order_info(
                user_id=uid,
                recipient_name=name,
                recipient_address=address,
                recipient_phone_number=phone_number,
                order_total_price=order_total_price_count,
                order_number=crete_order_number,
                order_time=create_order_date,
                pay_id=user_pay_msg.id,
            )
            Order_info.save(add_Order_info)

            # 獲取 id , 關聯 add_Order_info_detiel
            # 按照 id 排序,獲取最大的id,且新增 訂單明細中
            Order_info_id = Order_info.objects.filter(user_id=uid).order_by('-id')[0]


            for i in user_cart_msg:
                # 建立對象
                add_Order_info_detiel = Order_info_detail()
                # 透過遍歷結果,將數據填入 Order_info_detail 、和 Order_info 中
                # 查找上面保存的訂單編號
                add_Order_info_detiel.user_id = uid
                add_Order_info_detiel.goods_id = i.goods_id
                add_Order_info_detiel.goods_color = i.goods_color
                add_Order_info_detiel.goods_size = i.goods_size
                add_Order_info_detiel.goods_img_url = i.goods_img_url
                add_Order_info_detiel.goods_amount = i.goods_amount
                add_Order_info_detiel.goods_price = i.goods_price
                add_Order_info_detiel.goods_total_price = i.goods_total_price
                add_Order_info_detiel.orders_id = Order_info_id.id
                add_Order_info_detiel.order_time = create_order_date

                #  將數據保存
                Order_info_detail.save(add_Order_info_detiel)

            # 新增完成後將購物車內的物品刪除
            user_cart_msg.delete()


            # 商品新增訂單成功訊息
            resp = render(request, 'shop_cart.html', {'order_msg': 'order add is ok!', 'order_number': crete_order_number})
            return resp
        else:
            return redirect('/')
    else:
        return redirect('/')



#  1.以下是 商品頁面 的 your cart api 資料串接
#  用戶點及新增至購物車的 api
def api_add_goods_in_cart(request):
    # 不能直接訪問,如果訪問就跳轉前一頁面
    if request.method == 'GET':
        url = request.META.get('HTTP_REFERER', '/')
        resp = redirect(url)
        return resp
    elif request.method == 'POST':
        # 判斷 登入狀態才可以送出表單,否則返回登入
        url = request.META.get('HTTP_REFERER', '/')
        if 'uid' in request.session and 'user_real_name' in request.session:
            uid = request.session['uid'][0]
            count = request.POST['goods_count']
            color = request.POST['goods_filter']
            gid = request.POST['gid']
            price = request.POST['goods_price']
            img_url = request.POST['goods_img_url']
            size = request.POST['size']

            # 查找是否已將商品加入過購物車,必須要多 filter size 欄位,用戶可能買不同尺寸
            user_cart_info = Shop_user_cart.objects.filter(user_id=uid, goods_id=gid, goods_size=size, goods_color=color)

            # 如果,以上 filter 存在 , 則只需要更改 商品的數量,和總價格
            if user_cart_info:
                # 將商品數量加上,上面接收新增的數量
                user_cart_amount_price = user_cart_info[0]
                #  原本數量 加上 新增的數量

                #  1. 先加總數量 (db 購物車的數量 + 用戶再次點選購買的數量)
                user_total_amount = user_cart_amount_price.goods_amount + int(count)
                #  2. 再算出總價 (總數量 * 價錢)
                user_total_price = user_total_amount * int(price)


                #  1.修改數量
                user_cart_amount_price.goods_amount = user_total_amount
                #  2.修改總價錢 ()
                user_cart_amount_price.goods_total_price = user_total_price

                # 再將它保存
                user_cart_amount_price.save()

                # 將 返回原先頁面
                resp = redirect(url)
                return resp

            else:
                # 計算單次總價格
                # 計算 商品總金額,存入對象 , 商品金額 * 商品數量
                total_price = int(price) * int(count)
                # # 建立 shop_cartinfo 對象,保存user 儲存的 新增購物車資訊
                shop_cart_info = Shop_user_cart(
                    #  user_id 用戶資訊
                    user_id=uid,
                    #  goods_id 商品資訊
                    goods_id=gid,
                    #  goods_img_url 商品圖
                    goods_img_url=img_url,
                    #  goods_color 商品顏色
                    goods_color=color,
                    #  goods_size 商品尺寸
                    goods_size=size,
                    #  goods_price 商品價格
                    goods_price=price,
                    #  goods_amount 商品數量
                    goods_amount=count,
                    #  goods_total_price 商品總價格
                    goods_total_price=total_price,
                )
                Shop_user_cart.save(shop_cart_info)
                resp = redirect(url)
                return resp

        #  如果未登入,直接跳轉 login 頁面
        else:
            # 如果 uid 和 real_name , 不存在則跳到燈入頁面
            #  login 登入後有設置 url , 登入後頁面會在自己跳轉到商品詳細頁面
            resp = redirect('/login')
            return resp

# 處理用戶購物車的數據
def api_query_user_goods(request):
    # 獲取前一頁面的url ,防止用戶直接訪問
    if request.method == 'POST':
        # 確認是否登入狀態
        if 'uid' in request.session and 'user_name' in request.session:
            # 1.獲取用戶的id 去查找購物車的商品
            uid = request.session['uid'][0]

            # id 由大到小排序,購物車商品由新到舊
            user_cart_info = Shop_user_cart.objects.filter(user_id=uid).order_by('-id')

            #  根據 query 的資訊,設置狀態,讓前端判斷購物車是否有數量,來組元素資訊
            # 設置變量,如果user_cart_status = 0 , 表式購物車沒有商品
            user_cart_status = 0
            user_cart_msg = 0

            #  如果 user_cart_info 存在
            if user_cart_info:
                # 則將 user_cart_status 的狀態改為 1
                user_cart_status = 1
                # 將查詢到的數據,利用 serializer 序列化組數據,返回給用戶
                user_cart_msg = serializers.serialize('json', user_cart_info)

            # 組數據
            user_cart_dic = {
                'user_cart_status': user_cart_status,
                'user_cart_msg': user_cart_msg
            }
            return HttpResponse(json.dumps(user_cart_dic))
        else:
            # 如果未登入狀態,則前端要將購物車的拉框隱藏
            user_cart_dic = {
                'user_cart_status': 2,
            }
            return HttpResponse(json.dumps(user_cart_dic))
    else:
        return redirect('/')

# 處理用戶購物車的數據刪除
def api_delet_user_goods(request):
    if request.method == 'POST':
        #  判斷用戶是否登入狀態
        if 'uid' in request.session and 'user_real_name' in request.session:
            # 1. 獲取用戶的值 和 uid
            uid = request.session['uid'][0]
            # 2. 用戶要刪除的資訊
            color = request.POST['color']
            gid = request.POST['goods_id']
            size = request.POST['size']

            # 設置刪除狀態 delet_user_goods_status
            delete_user_goods_status = 0

            # 獲取資料後 到關聯實體類 Shop_user_cart 中查找資訊刪除
            user_delet_info = Shop_user_cart.objects.filter(user_id=uid, goods_color=color, goods_id=gid, goods_size=size)
            # 如果查找商品存在
            if user_delet_info:
                delete_user_goods_status = 1
                # 透過實體類 ,刪除查詢到的商品
                user_delet_info.delete()

            #  重新獲取數量和價格,返回給前端
            user_cart_total = Shop_user_cart.objects.filter(user_id=uid).aggregate(amount=Sum('goods_amount'), price=Sum('goods_total_price'))


            # 將狀態數據返回
            delete_status_dic = {
                'delete_user_goods_status': delete_user_goods_status,
                'user_cart_total_amount': user_cart_total['amount'],
                'user_cart_total_price': user_cart_total['price'],
            }
            # 將刪除狀態返回給前端做回應
            return HttpResponse(json.dumps(delete_status_dic))
        else:
            return redirect('/')
    else:
        return redirect('/')




# 2.以下是確認結帳購物車商品頁面加載數據,傳給前端
def api_cart_goods_check(request):
    if request.method == 'POST':
        # 判斷用戶是否登入狀態,才能夠請求購物車數據
        if 'uid' in request.session and 'user_real_name' in request.session:
            # 獲取用戶的 user_id 查找,購物車商品
            uid = request.session['uid'][0]

            # 透過 uid filete 查找 實體類 Shop_cart
            user_cart_info = Shop_user_cart.objects.filter(user_id=uid).order_by('-id')

            # 獲取總數量、總價格
            user_cart_total = Shop_user_cart.objects.filter(user_id=uid).aggregate(amount=Sum('goods_amount'), price=Sum('goods_total_price'))

            user_goods_total_amount = user_cart_total['amount']
            user_goods_total_price = user_cart_total['price']


            # 查找用戶購物車是否有商品的狀態
            user_cart_status = {
                'user_cart_info_status': 0,
                'user_cart_msg_list': [],
                'user_cart_total_amount': user_goods_total_amount,
                'user_cart_total_price': user_goods_total_price,
            }


            if user_cart_info:
                user_cart_status['user_cart_info_status'] = 1
                for i in user_cart_info:
                    # 利用關聯類 GoodsType 獲取 商品 的 type
                    goods_msg = i.goods.GoodsType

                    # 獲取顏色小圖片 url
                    goods_color_img_url = i.goods.goods_color_set.filter(goods_color=i.goods_color)

                    user_cart_info_dic = {
                        'goods_type': goods_msg.title,
                        'goods_title': i.goods.title,
                        'goods_id': i.goods.id,
                        'goods_color': i.goods_color,
                        'goods_size': i.goods_size,
                        'goods_img_url': i.goods_img_url,
                        'goods_amount': i.goods_amount,
                        'goods_price': i.goods_price,
                        'goods_total_price': i.goods_total_price,
                        'goods_color_img_url': [str(i.goods_color_img) for i in goods_color_img_url][0],
                    }

                    user_cart_status['user_cart_msg_list'].append(user_cart_info_dic)

            # for i in goods_color_img_url:
            #     print(i.goods_color_img)

            return HttpResponse(json.dumps(user_cart_status))
    else:
        # 如果未登入則返回首頁
        return redirect('/')

#  購物車頁面進行數量操作
def api_goods_amount_change(request):
    if request.method == 'POST':
        if 'uid' in request.session and 'user_real_name' in request.session:
            #  獲取 post 請求數據
            uid = request.session['uid'][0]
            color = request.POST['color']
            gid = request.POST['gid']
            size = request.POST['size']
            action = request.POST['action']

            # 到實體類中 Shop_user_cart 中查找,購物車商品
            user_cart_msg = Shop_user_cart.objects.filter(user_id=uid, goods_id=gid, goods_color=color, goods_size=size)[0]
            #  如果 user_cart_msg 存在則作以下數量動作
            if user_cart_msg:
                #  減少數量
                if action == 'decreases':
                    #  如果數量 小於 1, 則要刪除商品
                    if user_cart_msg.goods_amount == 1:
                        user_cart_msg.delete()
                    else:
                        #  將 商品數量 - 1
                        user_cart_msg.goods_amount = user_cart_msg.goods_amount - 1
                        #  商品的總價格也必須要減去 1 個
                        user_cart_msg.goods_total_price = user_cart_msg.goods_total_price - user_cart_msg.goods_price
                        #  在保存到資料庫中
                        Shop_user_cart.save(user_cart_msg)
                #  增加數量
                elif action == 'increase':
                    user_cart_msg.goods_amount = user_cart_msg.goods_amount + 1
                    user_cart_msg.goods_total_price = user_cart_msg.goods_total_price + user_cart_msg.goods_price
                    Shop_user_cart.save(user_cart_msg)

                #  直接修改 input 數量
                elif action == 'input_change':
                    # 獲取修改的數量
                    amount = request.POST['amount']

                    #  如果 user 輸入的 amount = 0 ,刪除商品
                    if amount == '0':
                        user_cart_msg.delete()

                    #    如果 user 輸入 amount 空白 返回 狀態 400
                    elif amount == '':
                        return JsonResponse({'status': '400', 'messages': 'goods_amount is not null'})

                    #   如果 user 輸入 amount 正常,則計算 db 內的值並且保存
                    else:
                        # 直接修改購物車商品數量
                        user_cart_msg.goods_amount = int(amount)
                        user_cart_msg.goods_total_price = int(amount) * user_cart_msg.goods_price
                        Shop_user_cart.save(user_cart_msg)

                #  處理數據總和返回給前端
                #  獲取總數量 和 總價格
                user_cart_total = Shop_user_cart.objects.filter(user_id=uid).aggregate(amount=Sum('goods_amount'), price=Sum('goods_total_price'))

                user_goods_total_amount = user_cart_total['amount']
                user_goods_total_price = user_cart_total['price']

                if user_goods_total_amount == None and user_goods_total_price == None:
                    user_goods_total_amount = 0
                    user_goods_total_price = 0

                # 將數據組合返回給前端,做總價的處理
                user_cart_total_dic = {
                    'status': '200',
                    'messages':'成功',
                    'user_cart_total_amount': user_goods_total_amount,
                    'user_cart_total_price': user_goods_total_price,
                }
                return JsonResponse(user_cart_total_dic)
            else:
                return JsonResponse({'status': '400', 'messages': 'data is not found'})
        else:
            return redirect('/')
    else:
        return redirect('/')


# 支付方式數據
def api_cart_pay_send(request):
    if request.method == 'GET':
        if 'uid' in request.session and 'user_real_name' in request.session:
            pay_send = Pay_send.objects.filter()
            pay_send_list = []
            for i in pay_send:
                pay_send_dic ={
                    'chose_pay_send':i.chose_pay,
                    'send_price': i.send_price,
                }
                pay_send_list.append(pay_send_dic)

            return HttpResponse(json.dumps(pay_send_list))
        else:
            return redirect('/')
    else:
        return redirect('/')
