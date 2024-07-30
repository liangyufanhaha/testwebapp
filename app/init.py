from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
db = SQLAlchemy()
def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:admin@localhost/user'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY']="test111220"
    csrf = CSRFProtect(app)
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    from app.model.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    return app
