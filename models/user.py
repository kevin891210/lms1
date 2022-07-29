from db import db
from sqlalchemy.sql import func


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(80))
    user_pass = db.Column(db.String(80))
    user_nicename = db.Column(db.String(50))
    user_email = db.Column(db.String(100))
    user_url = db.Column(db.String(200))
    user_registered = db.Column(db.DATETIME(), server_default=func.now())
    user_activation_key = db.Column(db.String(255))
    user_status = db.Column(db.String(5))
    display_name = db.Column(db.String(50))

    def __init__(self, user_login, user_pass):
        self.user_login = user_login
        self.user_pass = user_pass

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, user_login):
        return cls.query.filter_by(user_login=user_login).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
