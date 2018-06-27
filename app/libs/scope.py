class Scope():
    allow_api=[]
    allow_module=[]
    forbidden_api=[]
    # 运算符 + 重载
    def __add__(self,other):
        # 不能用+=，+=修改的是内存
        # 具体视图函数级别
        self.allow_api=self.allow_api+other.allow_api
        # 通过set自动去重，再转回list
        self.allow_api=list(set(self.allow_api))
        # 具体模块级别
        self.allow_module=self.allow_module+other.allow_module
        self.allow_module = list(set(self.allow_module))
        self.forbidden_api=self.forbidden_api+other.forbidden_api
        self.forbidden_api=list(set(self.forbidden_api))
        return self
class UserScope(Scope):
    allow_api = ['v1.A','v1.B']
    forbidden_api = ['v1.user+super_get_user']
    def __init__(self):
        self+SuperScope()
class AdminScope(Scope):
    allow_api=['v1.user+super_get_user']
class SuperScope(Scope):
    allow_module = ['v1.user']
def is_in_scope(scope,endpoint):
    scope=globals()[scope]()
    # endpoint-> v1.user+super_get_user
    splits=endpoint.split('+')
    module=splits[0]
    # 判断是否在禁止视图函数中
    if endpoint in scope.forbidden_api:
        return False
    # 判断是否在允许模块中
    elif module in scope.allow_module:
        return True
    # 判断是否在允许视图函数中
    elif endpoint in scope.allow_api:
        return True
    else:
        return False