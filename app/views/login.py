from flask import  render_template, redirect, url_for, flash,request
from app.model.user import User
from app.forms.loginform import loginforms
from flask_login import login_user,login_required,logout_user
from app.init import create_app
app = create_app()



@login_required
def index():
    form = loginforms()
    return render_template('首页.html',form=form)

def login():
    form = loginforms()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user.username==form.username.data and user.password_hash==form.password.data:
              login_user(user)
              return redirect(url_for('index'))
            else:
                flash("用户名或密码错误")
    return render_template('login.html', title='Login', form=form)


@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

def pagetocreateuser():
    return render_template("adduser.html")
