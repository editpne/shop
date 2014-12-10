from core import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


from .users import Users
