from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserCaseform(FlaskForm):
    casename = StringField('Case Name', validators=[DataRequired()])
    precondition = StringField('Precondition', validators=[DataRequired()])
    usecasestep = StringField('Use Case Step', validators=[DataRequired()])
    preresult = StringField('Pre-Result', validators=[DataRequired()])
    usecasetype = StringField('Use Case Type', validators=[DataRequired()])
    usecasestatus = StringField('Use Case Status', validators=[DataRequired()])
    usecasepriority = StringField('Use Case Priority', validators=[DataRequired()])
    submit = SubmitField('Submit')