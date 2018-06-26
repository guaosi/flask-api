from collections import namedtuple

from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from app.libs.error_code import AuthFailed

auth=HTTPBasicAuth()
User=namedtuple('User',['uid','ac_type','scope'])
@auth.verify_password
def verify_password(token,password):
    user_info=verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user=user_info
        return True
def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token.encode('utf-8'))
    except BadSignature:
        # token无法解密的异常
        raise AuthFailed(msg='token is invalid',error_code=1002)
    except SignatureExpired:
        # token时间过期的异常
        print(345)
        raise AuthFailed(msg='token is expired',error_code=1003)
    uid=data['uid']
    ac_type=data['type']
    return User(uid,ac_type,'')