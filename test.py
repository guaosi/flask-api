class People:
    name='张三'
    age=18
    def __init__(self):
        self.sex='男'
    def keys(self):
        return ('name','age','sex')
    def __getitem__(self, item):
        return getattr(self,item)
obj=People()
print(dict(obj))