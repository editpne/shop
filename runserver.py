from core import app
from views import product_view, about_view
from model import db

app.register_blueprint(product_view, url_prefix='/product')
app.register_blueprint(about_view, url_prefix='/about')


if __name__ == '__main__':
    app.run(debug=True)