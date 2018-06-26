from flask import request, json
from werkzeug.exceptions import HTTPException


class APIExpection(HTTPException):
    code=500
    error_code=999
    msg='Sorry,we make a mistake'
    def __init__(self,code=None,error_code=None,msg=None,headers=None):
        if code:
            self.code=code
        if error_code:
            self.error_code=error_code
        if msg:
            self.msg=msg
        super(APIExpection,self).__init__(msg,None)
    def get_body(self, environ=None):
        data={
            'error_code':self.error_code,
            'msg':self.msg,
            # 返回格式  POST v1/client/register
            'request': request.method + ' ' + self.get_url_no_param()
        }
        return json.dumps(data)
    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]
    def get_url_no_param(self):
        full_path=str(request.full_path)
        main_path=full_path.split('?')
        return main_path[0]