from flask import Blueprint

view_application = Blueprint('product', __name__, url_prefix='/product')

@view_application.route('/')
def product_index():
    return 'Product main page'


@view_application.route('/<int:pid>')
def product_info(pid):
    return 'This Product is %s' % pid

@view_application.url_value_preprocessor
def get_profile_owner(enpoint, values):
    print enpoint
    print values

