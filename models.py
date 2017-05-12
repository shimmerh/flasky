from flask_sqlalchemy import SQLAlchemy
from application import app


db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, index=True)
    password = db.Column(db.String(128), unique=True, index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)
