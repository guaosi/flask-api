from json import JSONEncoder as _JSONEncoder
import uuid
from flask._compat import text_type
from datetime import date, datetime
from flask import Flask as _Flask

# 继承重写jsonify方法
from werkzeug.http import http_date

from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        # default是会被循环调用的，如果一个对象的变量里还是一个对象，依旧会再次调用default方法
        if hasattr(o,'keys') and hasattr(o,'__getitem__'):
            return dict(o)
        # 特殊处理某些特殊的对象转换
        if isinstance(o, datetime):
            return http_date(o.utctimetuple())
        if isinstance(o, date):
            return http_date(o.timetuple())
        if isinstance(o, uuid.UUID):
            return str(o)
        if hasattr(o, '__html__'):
            return text_type(o.__html__())
        raise ServerError()
class Flask(_Flask):
    json_encoder = JSONEncoder

