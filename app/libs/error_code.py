from app.libs.error import APIExpection
class ClientTypeError(APIExpection):
    code = 400
    msg = 'client is invalid'
    error_code = 1006
class ParameterException(APIExpection):
    code=400
    msg=''
    error_code = 1000
class Success(APIExpection):
    code=201
    msg='ok'
    error_code = 0