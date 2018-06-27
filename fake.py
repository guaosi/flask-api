# 离线脚本，创建超级管理员
from app import create_app
from app.libs.enums import ScopeTypeEnum
from app.models.base import db
from app.models.user import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.nickname = 'admin'
        user.password = 'a123654'
        user.email = 'admin@guaosi.com'
        user.auth = ScopeTypeEnum.ADMIN
        db.session.add(user)
