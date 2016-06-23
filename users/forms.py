from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Optional, EqualTo, Email

class SignupForm(Form):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    user_email = StringField('user_email', validators=[DataRequired(), Email()])
    title = StringField('title', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password_check = PasswordField('password_check', validators=[DataRequired(), EqualTo('password')])
    
    
class LoginForm(Form):
    login_email = StringField('login_email', validators=[DataRequired(), Email()])
    login_password = PasswordField('login_password', validators=[DataRequired()])