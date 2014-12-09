from flask import Flask
from views import product_view, about_view
app = Flask(__name__)

app.register_blueprint(product_view, url_prefix='/product')
app.register_blueprint(about_view, url_prefix='/about')


if __name__ == '__main__':
    app.run(debug=True)