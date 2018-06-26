from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.models.base import Base, db


class User(Base):
    id = Column(Integer,primary_key=True,autoincrement=True)
    email=Column(String(24),unique=True,nullable=False)
    nickname=Column(String(24),unique=True)
    auth=Column(SmallInteger,default=1)
    _password=Column('password',String(100))

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,raw):
        self._password=generate_password_hash(raw)

    @staticmethod
    def create_user_by_email(niakname,account,secret):
        with db.auto_commit():
            user=User()
            user.nickname=niakname
            user.email=account
            user.password=secret
            db.session.add(user)

