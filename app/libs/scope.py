class Scope():
    allow_api=[]
    # 运算符 + 重载
    def __add__(self,other):
        # 不能用+=，+=修改的是内存
        self.allow_api=self.allow_api+other.allow_api
        # 通过set自动去重，再转回list
        self.allow_api=list(set(self.allow_api))
        return self

class UserScope(Scope):
    allow_api = ['v1.A','v1.B']
class AdminScope(Scope):
    allow_api=['v1.super_get_user']
    def __init__(self):
        self + UserScope()
        print(self.allow_api)
class SuperScope(Scope):
    allow_api=['v1.C','v1.D']
    def __init__(self):
        self + UserScope + AdminScope()
        print(self.allow_api)
AdminScope()
SuperScope()

def is_in_scope(scope,endpoint):
    print(endpoint)
    scope=globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False