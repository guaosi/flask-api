from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.enums import ScopeTypeEnum
from app.libs.error_code import NotFound, AuthFailed
from app.models.base import Base, db


class User(Base):
    id = Column(Integer,primary_key=True,autoincrement=True)
    email=Column(String(24),unique=True,nullable=False)
    nickname=Column(String(24),unique=True)
    _auth=Column('auth',SmallInteger,default=1)
    _password=Column('password',String(100))
    def keys(self):
        return ['id','email','nickname','auth']

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,raw):
        self._password=generate_password_hash(raw)
    @property
    def auth(self):
        return self._auth
    @auth.setter
    def auth(self,raw):
        self._auth=raw.value
    @staticmethod
    def create_user_by_email(niakname,account,secret):
        with db.auto_commit():
            user=User()
            user.nickname=niakname
            user.email=account
            user.password=secret
            db.session.add(user)
    @staticmethod
    def verify(account,secret):
        user = User.query.filter_by(email=account).first_or_404()
        if not user.check_password(secret):
            raise AuthFailed()
        try:
            auth=ScopeTypeEnum(user.auth)
        except  ValueError as e:
            raise e
        scope=ScopeTypeEnum.getScope(auth)
        return {'uid':user.id,'scope':scope}
    def check_password(self,raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)