from app.libs.redprint import Redprint
api=Redprint('book')

@api.route('/create')
def create_book():
    return 'create_book'
@api.route('/get')
def get_book():
    return 'get book'
