from flask import Blueprint

view_application = Blueprint('about', __name__, url_prefix='/about')

@view_application.route('/')
def about_index():
    return 'About main page'


@view_application.route('/<int:pid>')
def about_info(pid):
    return 'This About is %s' % pid

