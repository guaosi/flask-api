from wtforms import StringField, IntegerField,ValidationError
from wtforms.validators import DataRequired, length, Email, Regexp
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form

class ClientForm(Form):
    account = StringField(validators=[DataRequired(),length(min=5,max=20)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self,field):
        try:
            client=ClientTypeEnum(field.data)
        except ValueError as e:
            raise e
        self.type.data=client
class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='邮箱格式不正确')])
    secret = StringField(validators=[DataRequired(),Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')])
    nickname=StringField(validators=[DataRequired(),length(min=2,max=22)])
    def validate_account(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError()
    def validate_nickname(self,field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError()