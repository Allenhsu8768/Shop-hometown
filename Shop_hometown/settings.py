"""
Django settings for Shop_hometown project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = b'l*o6^d22l_hfqg&p#9sw^*x*zhgc^0sm)wo_-l@k()4bi!rp!6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 後台管理模板
    'simpleui',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # for (shop_hometown-app)
    'index',
    'woman',
    'men',
    'kid',
    'baby',
    'sport',
    'login',
    'register',
    'shop_gbook',
    'description',
    'shop_cart',
    'shop_goods_detail',
    'order_system',
]




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Shop_hometown.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Shop_hometown.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop_hometown',
        'USER':'root',
        'PASSWORD':'xxxxxxx',
        'HOST':'xxxxxxx',
        'PORT':3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# DEBUG = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


#  設置 MEDIA_ROOT 、 MEDIA_URL 讓 admin 後台管理系統可以讀取靜態媒體圖片資料 media/static/upload/goodmain/xxx.png 檔案
MEDIA_ROOT = BASE_DIR
MEDIA_URL = '/media/'


#  設置載入的文件地址 (CSS,JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

#  設置 SMTP Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  #SMTP伺服器
EMAIL_PORT = 587  #TLS通訊埠號
EMAIL_USE_TLS = True  #開啟TLS(傳輸層安全性)
EMAIL_HOST_USER = 'notbook7787@gmail.com'  #寄件者電子郵件
EMAIL_HOST_PASSWORD = 'azhuuexmlnalufgh'  #Gmail應用程式的密碼






#  設置 session 的配置 (一天過後,刪除)
SESSION_COOKIE_AGE = 60*60*24

#  瀏覽器關閉的時候 , session 清空
SESSION_EXPIRE_AT_BROWSER_CLOSE = True