from django.shortcuts import render,redirect


#  導入模塊 httpResponse
from django.http import HttpResponse, Http404

# 導入 serialize 將數據做序列化,返回給前端
from django.core.serializers import serialize

#  導入 json 模塊做字典數據的處理
import json

# 導入 django 對會員密碼加密的方法 make_password (在應用 login 中會引入 check_password 進行解密),將 cookie 的值進行加密
from django.contrib.auth.hashers import make_password

# 導入model
from .models import *


#  導入 djgno 內建模塊寄信給註冊用戶
#  必須到 setting 中設置,才能夠發信
from django.conf import settings
from django.core.mail import EmailMessage

# 導入寄信的樣式(模板)
from django.template.loader import render_to_string

# Create your views here.

# 導入 自己設置的 token 的類
from .register_token import *

from Shop_hometown.settings import *


# 導入時間,新增資料時顯示註冊時間
import time
from datetime import date, datetime
import json

#  註冊頁面
def register_views(request):
    #  註冊頁面 判斷 GET 方法 還是 POST 方法
    if request.method == 'GET':
        url = request.META.get('HTTP_REFERER','/')
        # 如果用戶已經登入 uid 存在 session , 阻擋用戶訪問
        if 'uid' in request.session and 'user_name' in request.session:
        #  (紀錄是從哪一個路徑過來註冊會員資訊,成功後返回原頁面)先設置 url = request.META.get('HTTP_REFERER','/') , //如果沒有則返回首夜
            resp = redirect(url)
            return resp
        else:
            return render(request, 'register.html')

    elif request.method == 'POST':
        # 接收會員的資訊 POST 數據請求
        #  模板已設置 該有的 crsf
        user_name = request.POST['user_name']
        # 獲取密碼後 需要對密碼進行加密的動作
        pswd = request.POST['pswd']

        # 利用導入的函數,會返回加密後的密碼 new_pswd
        new_pswd = make_password(pswd)

        user_realname = request.POST['user_realname']
        email = request.POST['user_email']
        # 整理 birthday 格式 1992/11/15 改為 1992-11-15 才能存入 db 中
        user_birthday = request.POST['user_birthday'].replace('/', '-')
        user_phone_number = request.POST['user_phone_number']

        country_id = request.POST['country']
        city_id = request.POST['city']

        # 新增一個 Token 附加在網址後面(根據,username base64 + itsdangerous(序列化方法) 進行設置)
        create_token = Token(SECRET_KEY)
        token = create_token.generate_validate_token(user_name)

        #  處理 user_birthday才能夠計算 (轉為 年 月 天), 透過 datetime.strptime 轉為 時間格式做以下計算
        #  在將處理過後的 user_age_count 給user_infor 新增
        user_birthday_datetime = datetime.strptime(user_birthday, "%Y-%m-%d")
        user_age_count = int((datetime.now()-user_birthday_datetime).total_seconds()//(60*60*24*365))


        # # 建立 user_infro 對象(新增帳號)
        user_infor = User_Member(user_name=user_name,
                                 password=new_pswd,
                                 realname=user_realname,
                                 email=email,
                                 birthday=user_birthday,
                                 phone_number=user_phone_number,
                                 # 註冊時間
                                 registered_time=time.strftime('%Y-%m-%d %H:%M:%S'),
                                 # 發送驗證信時間
                                 send_emaill_time=time.strftime('%Y-%m-%d %H:%M:%S'),
                                 country_id=country_id,
                                 city_id=city_id,
                                 #  將當下時間,減掉生日日期,總秒數 除以 (60*60*24*365)
                                 user_age=user_age_count,
                                 )

        # 保存到 實體類中
        User_Member.save(user_infor)


        # 寄送驗證信(設置參數給模板傳送,讓用戶認證)
        check_user_msg = {
            'username': user_name,
            'check_url': 'http://127.0.0.1:8000/register/active_user/',
            'token': token,
            'real_name': user_realname
        }

        # 信箱模板樣式
        email_template = render_to_string('accounts/signup_success_email.html', check_user_msg)

        # 發送信件
        send_email = EmailMessage('註冊通知成功信', email_template, settings.EMAIL_HOST_USER, [email])
        send_email.fail_silently = False
        send_email.send()


        # 重定向回註冊前的頁面(上面通過 request.POST['source_url'] 獲取到 前一個頁面的值)
        # 獲取 url 註冊前一個頁面的值
        source_url = json.dumps(request.POST['source_url'])
        msg = '請至信箱進行驗證!'

        # 根據用戶信箱開頭
        # 查找 @ 後面一個單字,到字典中查詢哪一個信箱
        chose_mail = email[email.index('@')+1]

        # 將有信箱的值打印
        mail_dict = {
            'g': 'google',
            'y': 'yahoo',
        }
        # 如果符合,則給 check_email 賦值 , 傳給前端跳轉連接
        for i in mail_dict:
            if chose_mail == i:
                check_email = json.dumps(mail_dict[i])

        register_dict = {
            'msg': msg,
            'check_emaill': check_email,
            'source_url': source_url,
        }

        # 註冊成功 存取 session 和 cookie
        # 利用request.session['屬性名'] = [db值]
        # id 透過 以存儲的 user_name 查找
        request.session['uid'] = [user_infor.id]
        request.session['user_name'] = [user_infor.user_name]
        request.session['user_real_name'] = [user_infor.realname]

        resp = render(request, 'register.html', register_dict)
        # 此處還須設置 cookie、session
        return resp





# 處理 前端 國家 數據請求,後端處理,返回給前端
def ajax_country_msg_resp(request):
    country_msg = Country.objects.all()
    # 將(Query_set) 數據做序列化返回給前端
    country_msg_json = serialize('json', country_msg)

    return HttpResponse(country_msg_json)

# 處理 前端 選擇 國家後 對應的 地區,後端處理數據,返回給前端
def ajax_city_try_msg_resp(request):

    #  接收用戶點擊的 Counrty_id
    Country_id = request.GET['Country']

    # 查找 用戶點擊的國家對應的地區
    city_msg = City.objects.filter(Country_id=Country_id).all()

    # 將(Query_set)數據做序列化返回給前端
    city_msg_json = serialize('json', city_msg)
    return HttpResponse(city_msg_json)

# 驗證前端帳號資訊是否存在
def post_user_name_msg_resp(request):
    #  查找 是否存在 用戶資訊

    check_user_name = request.POST['user_name']

    user_name = User_Member.objects.filter(user_name=check_user_name)

    # 根據查找做以下判斷
    if user_name:
        for i in user_name:
            # 根據 user_name 做大小寫判斷,因為只會查到一筆資料
            if i.user_name.upper() == check_user_name.upper():
                Status = 1
                msg = 'exist'
    # 如果不存在,則表示用戶可以註冊
    else:
        Status = 0
        msg = 'notexist'


    # 組數據,傳送給前端
    user_msg = {
        'Status': Status,
        'msg': msg,
    }
    return HttpResponse(json.dumps(user_msg))

# 查找信箱資訊是否存在
def post_user_email_msg_resp(request):
    # 查找 信箱資訊
    user_email = User_Member.objects.filter(email=request.POST['user_email'])

    # 根據查詢做判斷
    if user_email:
        Status = 1
        msg = 'exist'
    else:
        Status = 0
        msg = 'notexist'

    user_msg = {
        'Status' : Status,
        'msg':msg,
    }

    return HttpResponse(json.dumps(user_msg))





# 註冊用戶信箱認證
def check_user_info(request, token):
    # 建立 check_token obj
    check_token = Token(SECRET_KEY)
    # 將網址點擊的token 進行反序
    # 利用 try 捕捉錯誤反為驗證失敗
    try:
        user_name = check_token.confirm_validate_token(token)
    except:
        return HttpResponse('驗證帳號有誤!!,請至會員中心重新發送驗證信!')

    # 如果token轉驛成功做以下動作
    try:
        # 用戶註冊時,帳號只有一個所以只會有一個 user_name 所以用 get 查找,且確認用戶 is_Active 尚未驗證 = False
        user_info = User_Member.objects.get(user_name=user_name)

        # 查詢註冊時間和,當下驗證時間是否超過30分鐘 如果超過則做以下判斷 check_mail_time > 30
        check_mail_time = (datetime.now() - user_info.send_emaill_time).total_seconds() // 60

    # 如果 user_name 不存在 ,怎捕捉錯誤,response 訊息給用戶,(因為是 get 所以查詢不到會error,用 try 來捕捉錯誤)
    except:
        return HttpResponse('對不起,您驗證的使用者不存在,請重新註冊!')

    # 判斷如果重複驗證(因為還未設置token 時間,所以沒有失效設置),所以在db 做 is_Active
    # 待修改設置 Token 的時間(時效)
    if user_info.is_Active == True:
        return HttpResponse('已驗證成功過,請直接訪問首頁 127.0.0.1:8000/')
    # 驗證成功將 is_Active 修改為 True

    # 判斷 如果 註冊時間,和信箱驗證時間超過 30分鐘,則需要到會員中心重新發送驗證
    elif check_mail_time > 30:
        return HttpResponse('信箱驗證時間已超過30分鐘,請至會員中心重新發送一次驗證信箱!')

    else:
        # 激活帳號,修改 is_Active = True
        user_info.is_Active = True
        user_info.check_emaill_time = time.strftime('%Y-%m-%d %H:%M:%S')
        # 保存數據
        User_Member.save(user_info)



        msg = '註冊成功!'
        # 將參數傳給模板,讓模板渲染知道 註冊成功!
        resp = render(request, 'index.html', locals())

        return resp

