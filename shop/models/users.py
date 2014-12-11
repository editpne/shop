from . import db


class Users(db.Model):
    __tablename__ = 's_users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(35), default='')
    passwd = db.Column(db.String(32), default='')
    real_name = db.Column(db.String(35), default='')
    role = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=1)

    def __repr__(self):
        return '<User: %s>' % self.uname

