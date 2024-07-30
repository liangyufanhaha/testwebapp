from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.init import db


class User(UserMixin,db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

class UseCase(db.Model):
   __table_name__="usercase"
   id = db.Column(db.Integer, primary_key=True)
   casename=db.Column(db.String(80),nullable=False)
   precondition=db.Column(db.String(100))
   usecasestep=db.Column(db.String(1000))
   preresult=db.Column(db.String(1000))
   usecasetype=db.Column(db.String(10))
   usecasestatus=db.Column(db.String(10))
   usecasepriority=db.Column(db.String(4))
   def __repr__(self):
          return f'<UseCase {self.casename}>'