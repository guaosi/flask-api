from flask import Blueprint
from app.api.v1 import book,user,client,token
def create_blueprint():
    bp=Blueprint('v1',__name__)
    book.api.register(bp,url_prefix='/book')
    user.api.register(bp,url_prefix='/user')
    client.api.register(bp,url_prefix='/client')
    token.api.register(bp,url_prefix='/token')
    return bp