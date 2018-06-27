from enum import Enum
class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101
    #微信类
    USER_MINA = 200
    USER_WX = 201
class ScopeTypeEnum(Enum):
    USER = 1
    ADMIN = 2
    @classmethod
    def getScope(cls,auth):
        key_map={
            cls.USER:'UserScope',
            cls.ADMIN:'AdminScope'
        }
        return key_map[auth]
