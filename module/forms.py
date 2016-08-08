from flask_wtf import Form
from wtforms import StringField
from wtforms import PasswordField
from wtforms.validators import import DataRequired

class SignUpForm(Form):
    email_id = StringField('email_id', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])
