from django.shortcuts import render,redirect,HttpResponseRedirect

from django.http import HttpResponse,JsonResponse
# Create your views here.


# 導入 register 的 model 模塊 查找用戶資訊
from register.models import *

# 登入裝態直接查找 cart 中的商品,所以要引入應用 shop_cart model
from shop_cart.models import *
from .models import *

# 導入 index.model將用戶點擊追蹤的 Goods 表中的 heart + 1
from index.models import *


# 引入聚合函數 Sum , 將購物車的數量加總起來
from django.db.models import Sum


#  register 中 導入 django 對會員密碼加密的方法在, 所以在應用 login 中會引入 check_password 進行解密)
from django.contrib.auth.hashers import check_password

#  導入 djgno 內建模塊寄信給註冊用戶


#  必須到 setting 中設置,才能夠發信
from django.conf import settings
from django.core.mail import EmailMessage


# 導入 register.token 處理 user_name ,產生 token
from register.register_token import *
# 導入 setting
from Shop_hometown.settings import *

# 導入 time 重新更改發送驗證信時間
import time

# 導入寄信的樣式(模板)
from django.template.loader import render_to_string


# 將商品做序列化 把查找 的 QuerySet 處理成 json 字典格式字串
from django.core import serializers

# 導入 json
import json

#  登入頁面

def login_views(request):
    # 獲取點擊 login 前的頁面網址
    if request.method == 'GET':
        # 獲取 點擊前的 url
        url = request.META.get('HTTP_REFERER', '/')
        # 先判斷 session 存不存在, 如果存在則跳回原本頁面
        if 'uid' in request.session and 'user_name' in request.session:
            resp = HttpResponseRedirect(url)
            return resp
        # 沒有登入信息 session , 則檢查 cookie 的值
        else:
            # 如果 cookie 有值則取出來.存在 session 中
            if 'uid' in request.COOKIES and 'username' in request.COOKIES and 'user_real_name' in request.COOKIES:
                uid = request.COOKIES['uid']
                user_name = request.COOKIES['username']
                user_real_name = request.COOKIES['user_real_name']

                # 設置 session 的登入信息
                request.session['uid'] = [uid]
                request.session['user_name'] = [user_name]
                request.session['user_real_name'] = [user_real_name]

                # 建立對象,且將url 設置在 cookie 中
                resp = redirect(url)
                return resp
            else:
                resp = render(request, 'login.html')
                resp.set_cookie('url', url)
                return resp

    elif request.method == 'POST':
        try:
            # user_name 只會有一個,所以 用 get 查詢 (用戶如果存在,則動作下面的判斷)
            user_infor = User_Member.objects.get(user_name=request.POST['username'])
        except:
            # 如果用戶不存在,則捕捉錯誤給模板信息,讓 JS 設置的彈框跳出動作,msg1,用戶不存在
            msg1 = '用戶不存在,請前往註冊'
            resp = render(request, 'login.html', locals())
            return resp

        #  如果沒有錯誤被捕捉,則表示用戶存在做下判斷 (判斷用戶密碼)
        if (check_password(request.POST['password'], user_infor.password)):
            # 以下為登入成功狀態
            #  1. 點選記住密碼
            # 獲取點選登入時,存在 cookie 的 url
            url = request.COOKIES['url']
            # 判斷如果用戶有點點擊記住密碼,則要存取 session 和 cookie
            # 利用request.session['屬性名'] = [db值]
            request.session['uid'] = [user_infor.id]
            request.session['user_name'] = [user_infor.user_name]
            request.session['user_real_name'] = [user_infor.realname]

            resp = redirect(url)
            if 'is_saved' in request.POST:
                # 判斷如果用戶有點點擊記住密碼 cookie
                # 設置 cookie 的 username 和 user_id
                resp.set_cookie('uid', user_infor.id, 60*60*24*90)
                resp.set_cookie('username', user_infor.user_name, 60*60*24*90)
                resp.set_cookie('user_real_name', user_infor.realname, 60*60*24*90)

                # 再將原本的 存在url 刪除
                if 'url' in request.COOKIES:
                    resp.delete_cookie('url')
            return resp
        else:
            msg2 = '密碼輸入有誤,請檢查密碼!'
            resp = render(request, 'login.html', locals())
            return resp





# 點選登出, sign_out_view
def sign_out_view(request):
    # 必須要登入才會有登出的按鈕
    url = request.META.get('HTTP_REFERER', '/')
    # 設置對象 resp 清除 cookie 的
    resp = redirect(url)
    # 判斷 uid 、 user_name 、 real_name 是否存在
    if 'uid' in request.session and 'user_name' in request.session and 'user_real_name' in request.session:
        # 將 session 的值都清除
        request.session.flush()
        if 'uid' in request.COOKIES and 'username' in request.COOKIES and 'user_real_name' in request.COOKIES:
            resp.delete_cookie('uid')
            resp.delete_cookie('username')
            resp.delete_cookie('user_real_name')
            return resp
    return resp


# 處理 check_login 路由
def check_login_view(request):
    #  登入資訊和購物車數量一起查詢,傳給前端
    if 'user_name' in request.session and 'uid' in request.session:
        # 如果存在的話,查找透過 request.session['user_id'] 用 id 查找 user訊息
        uid = request.session['uid'][0]

        #  1. 登入資訊
        # id 是唯一性,所以用 get 方式搜尋

        user_info = User_Member.objects.get(id=uid)
        user_real_name = user_info.realname

        # # Login_Status = 1 表示存在
        Login_Status = 1

        #  2.購物車商品 (django 聚合函數必須先引入 Count)
        user_cart_info = Shop_user_cart.objects.filter(user_id=uid).aggregate(goods_sum=Sum('goods_amount'))

        #  查詢 user 的追蹤商品清單
        user_track_goods_msg = User_track_goods.objects.filter(users_id=uid)
        user_track_goods_msg_list = []
        for i in user_track_goods_msg:
            user_track_goods_msg_list.append(i.goods_id)


        # 先設定 user_cart_count 的數量 = 0, 如果 上面query 查詢的值為null,則傳給前端 數量 = 0
        user_cart_count = 0

        if user_cart_info['goods_sum'] != None:
            #  如果有值則,user_cart_count 取數量的值
            user_cart_count = user_cart_info['goods_sum']



        # 組數據 傳給前端
        login_msg = {
            'Login_Status': Login_Status,
            'user_real_name': user_real_name,
            'user_cart_count': user_cart_count,
            'user_track_goods_id': json.dumps(user_track_goods_msg_list),
        }
    else:
        login_msg = {
            'Login_Status': 0,
        }
    return HttpResponse(json.dumps(login_msg))


# 將商品新增到追蹤名單
def api_add_track_goods(request):
    if request.method == 'GET':
        if 'user_name' in request.session and 'uid' in request.session:

            # 獲取 uid
            uid = request.session['uid'][0]
            # 獲取用戶點擊的 id
            track_goods_id = request.GET['goods_id']

            # 查找第1筆資料 (兩個 filter , 一個用會對一個商品只能追蹤一次)
            user_track_msg = User_track_goods.objects.filter(users_id=uid, goods_id=track_goods_id)

            # 查找關聯表 GOODS (根據用戶點擊,做加減)
            Goods_heart_change = Goods.objects.filter(id=track_goods_id)[0]

            if user_track_msg:
                # 如果存在就將商品刪除
                user_track_msg.delete()

                # 因為存在所已是第二次點擊,要刪除 heart 的數量 -1
                Goods_heart_change.heart = Goods_heart_change.heart - 1
                Goods.save(Goods_heart_change)

                # 如果存在,第二次點擊就要移除對商品的追蹤, msg = 2, 表示已經追蹤過,點及第二次將商品刪除
                return JsonResponse({'status': '200', 'msg': '2'})
            else:
                # 建立對象
                user_track_goods = User_track_goods(users_id=uid, goods_id=track_goods_id)
                # 保存數據
                User_track_goods.save(user_track_goods)

                # 因為是第一次點擊,將heart 增加 + 1
                Goods_heart_change.heart = Goods_heart_change.heart + 1
                Goods.save(Goods_heart_change)

                # msg = 1 表示尚未將商品加入追蹤清單,將數據新增
                return JsonResponse({'status': '200', 'msg': '1'})
        else:
            return redirect('/')
    else:
        return redirect('/')



# 會員中心點擊頁面(新品展示)
def user_member_center_views(request):
    if request.method == 'GET':
        #  登入資訊和購物車數量一起查詢,傳給前端
        if 'user_name' in request.session and 'uid' in request.session:
            # 點擊 會員中心,一開始輸出頁面為,近期新品
            # 1.查詢 近期新增的商品
            #   1.Women's
            women_goods_msg = Goods.objects.filter(GoodsType=1).order_by('-goods_put_on')[:3]
            #   2.Men's
            men_goods_msg = Goods.objects.filter(GoodsType=2).order_by('-goods_put_on')[:3]
            #   3.Kid's
            kid_goods_msg = Goods.objects.filter(GoodsType=3).order_by('-goods_put_on')[:3]
            #   4.baby's
            baby_goods_msg = Goods.objects.filter(GoodsType=4, GoodsType2=1).order_by('goods_put_on')[:3]
            #   5.sport's
            sport_goods_msg = Goods.objects.filter(GoodsType=5).order_by('-goods_put_on')[:3]

            return render(request, 'user_login_member_center.html', locals())
        else:
            return redirect('/')
    else:
        return redirect('/')


# 1. api 會員資料查詢
def api_user_member_views(request):
    if request.method == 'POST':
        if 'user_name' in request.session and 'uid' in request.session:
            # 獲取 uid 查找,User資料
            uid = request.session['uid'][0]

            user_member_msg = User_Member.objects.filter(id=uid)

            if user_member_msg:
                user_member_msg_dic = {}
                for i in user_member_msg:
                    user_member_msg_dic['user_name'] = i.user_name
                    user_member_msg_dic['realname'] = i.realname
                    user_member_msg_dic['email'] = i.email
                    user_member_msg_dic['birthday'] = i.birthday
                    user_member_msg_dic['phone_number'] = i.phone_number
                    user_member_msg_dic['is_Active'] = i.is_Active
                    user_member_msg_dic['registered_time'] = i.registered_time
                    user_member_msg_dic['country'] = i.country.Country_name
                    user_member_msg_dic['city'] = i.city.City_name

                return JsonResponse({'status':'200','msg':'成功!','user_member_msg_dic':user_member_msg_dic})
            else:
                return JsonResponse({'status': '400', 'msg': 'not fund data!'})
        else:
            return redirect('/')
    else:
        return redirect('/')


# 2. 點選重新發送驗證信 (user 如果信箱尚未驗證,才會出現此按鈕,啟用此api)
def api_send_user_mail(request):
    if request.method == 'GET':
        #  登入資訊和購物車數量一起查詢,傳給前端
        if 'user_name' in request.session and 'uid' in request.session:
            get_user_name = request.GET['user_name']
            get_user_email = request.GET['user_email']
            get_real_name = request.GET['user_real_name']

            # 獲取 User_member 的訊息,修改信箱驗證時間
            user_msg = User_Member.objects.filter(user_name=get_user_name,email=get_user_email,realname=get_real_name)[0]




            # 產生 token, 透過 Shop_hometown.setting 的 SECRET_KEY
            #  建立對象
            create_token = Token(SECRET_KEY)
            # 將 user_name 傳入,產生 token
            token = create_token.generate_validate_token(get_user_name)



            # # 寄送驗證信(設置參數給模板傳送,讓用戶認證)
            check_user_msg = {
                'username': get_user_name,
                'check_url': 'http://127.0.0.1:8000/register/active_user/',
                'token': token,
                'real_name': get_real_name
            }

            # 信箱模板樣式
            email_template = render_to_string('accounts/signup_success_email.html', check_user_msg)

            # 發送信件
            send_email = EmailMessage('註冊通知成功信', email_template, settings.EMAIL_HOST_USER, [get_user_email])
            send_email.fail_silently = False
            send_email.send()

            # 重新修改,驗證信發送時間
            user_msg.send_emaill_time = time.strftime('%Y-%m-%d %H:%M:%S')
            User_Member.save(user_msg)


            return JsonResponse({'status':'200'})
        else:
            return redirect('/')
    else:
        return redirect('/')


# 4. 點選用戶追蹤的商品資料
def api_user_track_goods_view(request):
    if request.method == 'GET':
        # 判斷登入狀態獲取資訊
        if 'user_name' in request.session and 'uid' in request.session:
            uid = request.session['uid'][0]
            # 透過 uid 查找 實體關聯 user_track_goods 追蹤的商品資料
            user_track_msg = User_track_goods.objects.filter(users_id=uid)


            # 組字典數據傳給前端處理
            user_track_all_goods_dic = {
                'user_track_goods_msg_status': 0,
            }



            # 判斷用戶是否有追蹤的商品
            if user_track_msg:

                # 將字典狀態職修改
                user_track_all_goods_dic['user_track_goods_msg_status'] = 1

                # 設置列表,新增查找到的 goods_id 資訊
                user_track_list = []

                # 將filter 到的商品,放置列表中
                for i in user_track_msg:
                    user_track_list.append(i.goods_id)


                # 建立實體類對象 # 再透過 filter(欄位__in) 的方式查找good 資訊
                user_track_goods_msg = Goods.objects.filter(id__in=user_track_list)


                # 建立一個 所有 商品字典資訊的 list
                user_track_goods_msg_list = []

                # 透過遍歷 QuerySet 取值,組數據
                for i in user_track_goods_msg:
                    # 建立單件商品資訊的 list ,設置在循環內
                    user_track_goods_color_list = []

                    # 建立字典取值,組數據
                    user_track_goods_dic = {
                        'goods_id': i.id,
                        'goods_name': i.title,
                        'goods_price': int(i.price),
                        'goods_img': str(i.Images_url),
                        'goods_heart':i.heart,
                    }
                    # 透過外部關聯的方式 goods_color_set (查找 i.id 的商品 顏色資訊)
                    for j in i.goods_color_set.filter(goods_id=i.id):

                        # 將組好的 (商品顏色資訊,新增到 user_track_goods_color_list 中)
                        user_track_goods_color_list.append({j.goods_color: str(j.goods_color_img)})

                    # 在將 建立單件商品資訊的 list 存在 user_track_goods_dic 中
                    user_track_goods_dic['goods_color_img_color'] = user_track_goods_color_list

                    # 將 user_track_goods_msg_list 新增 user_track_goods_dic 的值
                    user_track_goods_msg_list.append(user_track_goods_dic)

                # 在新增追蹤的商品清單到 user_track_all_goods_dic 中
                user_track_all_goods_dic['user_track_goods_msg'] = json.dumps(user_track_goods_msg_list)

            # 透過 JsonResponse 返回給前端處理資訊
            return JsonResponse(user_track_all_goods_dic)

        else:
            return redirect('/')
    else:
        return redirect('/')







