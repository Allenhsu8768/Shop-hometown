# 設置類 Token, 產生一個用戶認證連結

# itsdangerous(序列化方法) 做加密 token 的動作 ,產生一個用戶認證連結
from itsdangerous import URLSafeSerializer as utsr
import base64
import re


class Token(object):
    #  設置 初始 security_key
    def __init__(self, security_key):
        self.security_key = security_key
        # 必須修改 setting 中的  SECURITY_KEY 轉為 字節 b'',才能透過 base64編碼
        self.salt = base64.encodebytes(security_key)

    # 進行加密效果(針對 username),針對使用者的名稱產生令牌
    def generate_validate_token(self, username):
        #  利用序列化方法 ,產生令牌
        serializer = utsr(self.security_key)
        return serializer.dumps(username, self.salt)

    # 根據點擊網址進行令牌解密,就會返為一個使用者名稱
    def confirm_validate_token(self, token):
        serializer = utsr(self.security_key)
        return serializer.loads(token, salt=self.salt)

