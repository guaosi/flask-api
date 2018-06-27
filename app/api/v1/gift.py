from flask import g

from app.libs.error_code import DuplicateGift, Success
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.book import Book
from app.models.gift import Gift

api=Redprint('gift')
@api.route('/<int:isbn>')
@auth.login_required
def create(isbn):
    uid=g.user.uid
    with db.auto_commit():
        Book.query.filter_by(isbn=isbn).first()
        gift=Gift.query.filter_by(uid=uid,isbn=isbn,launched=False).first()
        if gift:
            raise DuplicateGift()
        gift=Gift()
        gift.uid=uid
        gift.isbn=isbn
        db.session.add(gift)
    return Success()