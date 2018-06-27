from flask import current_app, jsonify
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import AuthFailed, Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, TokenForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

api=Redprint('token')
@api.route('',methods=['POST'])
def get_token():
    form=ClientForm().validate_for_api()
    promise={
        ClientTypeEnum.USER_EMAIL:User.verify
    }
    identify=promise[form.type.data](form.account.data,form.secret.data)
    expiration=current_app.config['TOKEN_EXPIRE_TIME']
    token=generate_token(identify['uid'],form.type.data,identify['scope'],expiration)
    t={
        'token':token.decode('utf-8')
    }
    return jsonify(t),201
# 验证一个令牌是否过期，获得令牌信息
@api.route('/secret',methods=['POST'])
def get_token_info():
    form=TokenForm().validate_for_api()
    token=form.token.data
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        # return_header=True 可以让返回结果多一些信息，比如创建时间和过期时间
        data = s.loads(token.encode('utf-8'),return_header=True)
    except BadSignature:
        # token无法解密的异常
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        # token时间过期的异常
        raise AuthFailed(msg='token is expired', error_code=1003)
    r={
        'scope':data[0]['scope'],
        'create_at':data[1]['iat'],
        'expire_in':data[1]['exp'],
        'uid':data[0]['uid']
    }
    return jsonify(r)
def generate_token(uid,ac_type,scope=None,expiration=7200):
    s=Serializer(current_app.config['SECRET_KEY'],expiration)
    return s.dumps({
        'uid':uid,
        'type':ac_type.value,
        'scope':scope
    })