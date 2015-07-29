from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, DataRequired

class LoginForm(Form):
	username = StringField('Username', validators=[Required(), Length(3,16)])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Remember me')
	submit = SubmitField('Submit')

class CheckUserForm(Form):
	checkusername = StringField('Please enter userid', validators=[DataRequired(), Length(3,16)])
	submit = SubmitField('Submit')
