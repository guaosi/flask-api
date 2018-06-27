from werkzeug.exceptions import HTTPException
from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app=create_app()
# 定义全局异常处理
@app.errorhandler(Exception)
def framework_error(e):
    # 可预见的自定义异常
    if isinstance(e,APIException):
        return e
    # 不可预见的HTTPP异常
    if isinstance(e,HTTPException):
        code=e.code
        msg=e.description
        error_code=1007
        return APIException(code,error_code,msg)
    # 不可预见的非正常异常
    else:
        if app.config['DEBUG']:
            raise e
        else:
            return ServerError()
if __name__=='__main__':
    app.run(debug=app.config['DEBUG'],port=80)