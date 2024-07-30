from views.login import index,login
from views.user import createuser,userlist,tocreaseusecasepage
from views.usecase import tousecasepage,addusecase,tocreateusecasepage
from app.init import create_app,db
from app.model.user import User
app=create_app()
app.add_url_rule('/index', 'index', index,methods=["POST","GET"])
app.add_url_rule('/login', 'login', login,methods=["POST","GET"])
app.add_url_rule('/user/userlist', 'userlist', userlist,methods=["POST","GET"])
app.add_url_rule('/user/userpage','createuserpage',tocreaseusecasepage,methods=["GET"])
app.add_url_rule('/user/add','add',createuser,methods=["POST"])
app.add_url_rule('/','login',login)
app.add_url_rule('/usecase','tousecasepage',tousecasepage,methods=["GET"])
app.add_url_rule('/usecase/addpage','tocreateusecasepage',tocreateusecasepage,methods=["GET"])
app.add_url_rule('/usercase/add','createusecase',addusecase,methods=["POST"])


def load_user(user_id):
    return User.get_by_id(user_id)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)