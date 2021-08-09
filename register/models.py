from django.db import models

# Create your models here.


# 載入 時間模塊計算年齡
from datetime import date



#  設置 註冊國家 model 讓user可以選擇國家
class Country(models.Model):
    Country_name = models.CharField(max_length=40, verbose_name='國家')

    class Meta():
        # table_name
        db_table = 'Country'

        verbose_name = '國家表'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return '<國家名稱 % r >' % self.Country_name

    def __str__(self):
        return self.Country_name



# 設置 註冊國家的地區 model 關連到國家表 (連動國家出現表),根據國家顯示地區

class City(models.Model):
    #  外部關連到 國家的ID
    Country = models.ForeignKey(Country, verbose_name='國家', on_delete=models.CASCADE)

    #  城市名稱
    City_name = models.CharField(max_length=100, verbose_name='城市')

    class Meta():
        db_table = 'City'

        verbose_name = '國家地區'
        verbose_name_plural = verbose_name


    def __repr__(self):
        return '<城市名稱 %r>' % self.City_name

    def __str__(self):
        return self.City_name




# 設置 會員資訊 model
class User_Member(models.Model):
    #  會員帳號 (設置 唯一性 unique = True)
    #  前端會設置 驗證 是否重覆 帳號()
    user_name = models.CharField(max_length=20, verbose_name='會員帳號', unique=True)

    # 會員密碼 (因為會加密,所以設置 長度為 100)
    password = models.CharField(max_length=100, verbose_name='會員密碼')

    # 會員姓名
    realname = models.CharField(max_length=20, verbose_name='會員姓名')

    # 前端會設置 驗證 是否重覆 信箱()
    # 會員信箱 (設置 唯一性 unique = True)
    email = models.EmailField(max_length=50, verbose_name='會員信箱', unique=True)

    # 會員生日
    birthday = models.DateField(verbose_name='會員生日日期')

    # 會員年齡 (透過後端計算存入)
    user_age = models.IntegerField(verbose_name='年齡', null=True)

    # 手機號碼 (設置限制10碼)
    phone_number = models.CharField(max_length=10, verbose_name='會員電話')

    #  居住的國家
    country = models.ForeignKey(Country, verbose_name='國家', on_delete=models.CASCADE, null=True)

    #  居住的城市
    city = models.ForeignKey(City, verbose_name='城市', on_delete=models.CASCADE, null=True)

    # 是否信箱驗證成功 (預設是 False)
    is_Active = models.BooleanField(verbose_name='帳號是否驗證成功', default=False)

    # 註冊時間
    registered_time = models.DateTimeField(verbose_name='註冊時間', null=True)

    # 如果用戶沒收到,或是驗證時間超過,會透過重新發送驗證來變動時間
    send_emaill_time = models.DateTimeField(verbose_name='發送驗證信件時間', null=True)

    # 信箱驗證時間
    check_emaill_time = models.DateTimeField(verbose_name='信箱驗證成功時間', null=True, blank=True)

    # Authority 帳號權限 (管理員), 一般帳號用戶註冊設置為 False , 預設為 False
    authority = models.BooleanField(verbose_name='管理權限', default=False)


    class Meta():
        db_table = 'User_Member'

        verbose_name = '會員資訊'
        verbose_name_plural = verbose_name



    def __repr__(self):
        return '<會員姓名%r>' % self.user_name

    def __str__(self):
        return self.user_name


