from app.forms.loginform import loginforms
from app.model.user import User
from flask_login import login_required
from flask import  render_template, redirect, url_for, flash,request
from app.init import db

def createuser():
  form = loginforms()
  if request.method == 'POST':
     if form.validate_on_submit():
        user = User(username=form.username.data, password_hash=form.password.data)
        try:
          db.session.add(user)
          db.session.commit()
          print(user.username,user.password_hash)
          flash('Account created for {}!'.format(form.username.data))
          return redirect(url_for('userlist'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed: {}'.format(str(e)))
            return render_template('login.html', title='Register', form=form)
     else:
         print(form.errors)
     return render_template('login.html', title='Register', form=form)
  else:
      return render_template('login.html', title='Register', form=form)
@login_required
def userlist():
    users=User.query.all()
    data=[{"name":user.username} for user in users]
    return render_template('userlist.html', users=data)



def tocreaseusecasepage():
    return render_template("adduser.html")