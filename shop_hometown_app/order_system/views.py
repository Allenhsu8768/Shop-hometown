from django.shortcuts import render,redirect

from django.http import JsonResponse

# Create your views here.

import json

# 導入 model
from .models import *


# 用戶查詢,訂單資料
def api_query_user_order_view(request):
    if request.method == 'POST':
        if 'user_name' in request.session and 'uid' in request.session:
            uid = request.session['uid'][0]
            user_order_number = request.POST['order_number']
            user_order_date_begin = request.POST['order_date_begin']
            user_order_date_end = request.POST['order_date_end']


            #  根據前端發送的值做判斷查詢(如果沒有 user_order_number ,則直接查詢日期的區間)
            if user_order_number == '':
                #  1.多筆查詢
                user_order_msg = Order_info.objects.filter(user_id=uid, order_time__range=(user_order_date_begin, user_order_date_end)).order_by('-id')
            else:
                #  2.查詢單筆
                # 如果有 user_order_number 則只要查詢 訂單編號即可
                user_order_msg = Order_info.objects.filter(user_id=uid, order_number=user_order_number)



            # 組數據給前端設置頁面
            user_order_msg_dict = {
                'user_order_status': 0,
            }


            # 設置 user_order_msg_list 來組 訂單數據格式
            user_order_msg_list = []

            # 如果 user_order_msg 存在,則表示有數據
            if user_order_msg:
                #  將 user_order_msg 狀態 改為 1
                user_order_msg_dict['user_order_status'] = 1

                for i in user_order_msg:
                    user_order_info_dic = {
                        'recipient_name': i.recipient_name,
                        'recipient_phone_number': i.recipient_phone_number,
                        'recipient_address': i.recipient_address,
                        'order_total_price': i.order_total_price,
                        'order_number': i.order_number,
                        'order_time': i.order_time,
                        'order_status': i.order_status,
                        'order_check_time': i.order_check_time,
                        'order_pay_chose_pay': i.pay.chose_pay,
                        'order_pay_send_price': i.pay.send_price,
                        'user_order_info_detail': [],
                    }
                    for j in i.order_info_detail_set.filter(orders_id=i.id):
                        user_order_info_dic['user_order_info_detail'].append({
                            'goods_id': j.goods_id,
                            'goods_name': j.goods.title,
                            'goods_img_url': j.goods_img_url,
                            'goods_color': j.goods_color,
                            'goods_color_img': str(Goods_color.objects.filter(goods_id=j.goods_id, goods_color=j.goods_color)[0].goods_color_img),
                            'goods_size': j.goods_size,
                            'goods_amount': j.goods_amount,
                            'goods_price': j.goods_price,
                            'goods_singo_total_price': j.goods_total_price,
                        })

                    user_order_msg_list.append(user_order_info_dic)

                user_order_msg_dict['user_order_info_msg'] = user_order_msg_list
            return JsonResponse(user_order_msg_dict)

        else:
            return redirect('/')
    else:
        return redirect('/')