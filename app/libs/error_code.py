from app.libs.error import APIException
class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006
class ServerError(APIException):
    code=500
    error_code=999
    msg='Sorry,we make a mistake'
class ParameterException(APIException):
    code=400
    msg=''
    error_code = 1000
class Success(APIException):
    code=201
    msg='ok'
    error_code = 0
class DeleteSuccess(Success):
    code=202
    error_code = -1
class NotFound(APIException):
    code=404
    msg='The Source is not found'
    error_code = 1001
class AuthFailed(APIException):
    code=401
    msg='authorization failed'
    error_code = 1005
class Forbidden(APIException):
    code = 403
    msg='forbidden,not in scope'
    error_code = 1004