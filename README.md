扩展重写Flask API,更好地支持接口编写,可作为API部分的demo
===============
> 🚀 可作为项目构建初期API部分的参考，扩展重构了API常用部分功能

# 特性

- 基于蓝图创建红图,更好细分模块与视图函数

- 重构创建APIException异常，更适用于API异常

- 重构WtForm,参数自校验,更适用于验证层抛出API异常

- 创建全局异常捕捉,统一全局异常返回格式

- 使用HTTPBasicAuth来自动验证token

- 重写 get_or_404 与 first_or_404

- 重写jsonify，使其支持模型序列化为dict返回json

- 使用Enum枚举类来表示状态，更具可读性

- 制作scope权限，可灵活分配权限

- 简单，开箱即用

> Python的运行环境要求3.6以上。


# 要求

| 依赖 | 说明 |
| -------- | -------- |
| Python| `>= 3.6` |
| Flask| `>= 1.0.2` |
| cymysql| `>= 0.9.10` |
| Flask-Login |`>= 0.4.1`|
| Flask-Mail |`>= 0.9.1`|
| Flask-SQLAlchemy  |`>= 2.3.2`|
| itsdangerous |`>= 0.24`|
| Jinja2 |`>= 2.10`|
| requests |`>= 2.18.4`|
| SQLAlchemy  |`>= 1.2.8`|
| urllib3 |`>= 1.22`|
| Werkzeug |`>= 0.14.1`|
| WTForms |`>= 2.2`|


# 注意
1. 数据库在运行ginger.py自动生成,请手动将每个数据表的引擎改为Innodb,默认为MyISAM,无事务功能。

2. 需要在app目录下创建secure.py文件。

3. **flask扩展需要自行安装**

# 安装

1. 通过[Github](https://github.com/guaosi/flask-api),fork到自己的项目下
```
git clone git@github.com:<你的用户名>/flask-api.git
```
2. 在app目录下创建secure.py文件
```
DEBUG=True  #是否开启Dubug
HOST='0.0.0.0' #0.0.0.0表示访问权限为全网
PORT=80 #访问端口号

# mysql连接，比如 SQLALCHEMY_DATABASE_URI='mysql+cymysql://root:root@localhost:3306/ginger'
SQLALCHEMY_DATABASE_URI='mysql+cymysql://用户名:用户名@ip地址:mysql端口号/数据库名'

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
```
3. 执行根目录下的 fake.py文件，生成管理员账户


## 相关依赖
最好在pipenv的虚拟环境中安装，避免全局污染,确保pipFile文件存在。
```
pipenv install
```

## 运行

> `python ginger.py`

# 项目中的使用

## 在项目中注册路由

API部分已经用红图代替了蓝图，在 app/api/v1 下构建 视图.py文件后，需要到app/api/v1/\_\_init.py\_\_文件中进行注册。比如
```
def create_blueprint():
    bp=Blueprint('v1',__name__)
    book.api.register(bp,url_prefix='/book')
    return bp
```
如果 视图.py文件中注册是视图函数route是
```
from app.libs.redprint import Redprint
api=Redprint('book')
@api.route('/create')
def create_book():
    return 'create_book'
```
此时API接口地址应为
> http://localhost/v1/book/create

## 在项目中使用参数验证

已经重写了Form,继承BaseForm即可。
BaseForm中自动获取请求参数并且验证，自动抛出异常。
在视图函数中直接调用BaseForm().validate_for_api()即可。比如
```
form=ClientForm().validate_for_api()
```

## 在项目中使用统一格式自动异常

已经重写了HTTPException,继承APIException即可。正常抛出继承APIException异常的异常类即可。

## 在项目中返回json

重写了jsonify，项目中jsonify(obj)可以直接返回模型序列化结果，比如
```
book=Book.query.filter_by(isbn=isbn).first_or_404()
return jsonify(book)
```

## 在项目中使用scope

自行修改app/libs/scope.py文件
scope类使用了运算符重载，可以快速增加或删除权限。支持基于视图函数，基于模块级别，排除视图函数级别的权限控制。

## 在项目中使用hide和append动态决定模型返回字段

重写了SQLAlchemy的db.Model类。模型中的构造函数可以指定返回字段结果。同时视图函数中，对orm模型可以使用append跟hidden动态决定返回字段.比如
```
 books=[book.hide('summary').append('page') for book in books]
 return jsonify(books)
```