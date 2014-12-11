from flask import Blueprint
from shop.models.users import Users
__bluename__ = 'about'

view_application = Blueprint(__bluename__, __name__, url_prefix='/about')


@view_application.route('/')
def about_index():
    print Users.query.all()
    return 'About main page'


@view_application.route('/<int:pid>')
def about_info(pid):
    return 'This About is %s' % pid

