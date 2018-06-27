from flask import request
from wtforms import Form
from app.libs.error_code import ParameterException
class BaseForm(Form):
    def __init__(self):
        #获取的json数据
        data=request.json
        #获取的get，post数据
        args=request.args.to_dict()
        # 获取的post数据
        # args1=request.form.to_dict()
        super(BaseForm,self).__init__(data=data,**args)
    def validate_for_api(self):
        validate = super(BaseForm, self).validate()
        if not validate:
            raise ParameterException(msg=self.errors)
        return self