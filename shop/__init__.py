from flask import Flask
from views import about_app, product_app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.register_blueprint(about_app)
app.register_blueprint(product_app)
