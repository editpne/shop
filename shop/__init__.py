from flask import Flask

app = Flask(__name__, instance_relative_config=True)
from .views import about_app
from .views import product_app

app.register_blueprint(about_app, url_prefix='/about')
app.register_blueprint(product_app, url_prefix='/product')



