from sqlalchemy import Column, Integer, String, orm
from app.models.base import Base
class Book(Base):
    id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(String(60),nullable=False)
    author=Column(String(30),default='佚名')
    binding=Column(String(20))
    publisher=Column(String(50))
    price=Column(String(20))
    page=Column(Integer)
    pubdate=Column(String(20))
    isbn=Column(String(15),unique=True,nullable=False)
    summary=Column(String(1000))
    image=Column(String(100))

    #因为sqlalchemy创建模型对象是通过元类的方法，不会执行__init__构造函数
    #使用orm.reconstructor装饰器可以让构造函数执行
    @orm.reconstructor
    def __init__(self):
        # 这里只能将field作为实例变量，因为Flask运行后，已经生成的实例，类变量等都保存到内存中
        # 类变量变成了共用的，如果将类变量进行修改，那么在服务器生命周期内，都会受到影响
        self.field=['id','title','author','binding','publisher','price','pubdate','isbn','summary','image']
    def keys(self):
        return self.field