from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
class loginforms(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 20)])
    password=PasswordField('密码', validators=[DataRequired(), Length(6, 20)])
    submit = SubmitField('Sign Up')