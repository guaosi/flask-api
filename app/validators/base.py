from flask import request
from wtforms import Form
from app.libs.error_code import ParameterException
class BaseForm(Form):
    def __init__(self):
        data=request.json
        super(BaseForm,self).__init__(data=data)
    def validate_for_api(self):
        validate = super(BaseForm, self).validate()
        if not validate:
            raise ParameterException(msg=self.errors)
        return self