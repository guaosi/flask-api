from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')
@api.route('/register', methods=['POST'])
def create_client():
    1/0
    form=ClientForm().validate_for_api()
    promise={
        ClientTypeEnum.USER_EMAIL:__register_user_by_email
    }
    promise[form.type.data]()
    return Success()

def __register_user_by_email():
    user_email_form=UserEmailForm().validate_for_api()
    User.create_user_by_email(user_email_form.nickname.data,user_email_form.account.data,user_email_form.secret.data)
