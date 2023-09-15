from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#registration form start
class Registration_form(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=2,max=15)])
    email = StringField(label='Email', validators=[Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(label='Confirm_password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Sign Up')
#registration form end


#login form start
class Login_form(FlaskForm):
    email = StringField(label='Email', validators=[Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    remember = BooleanField(label='Remember Me')
    submit = SubmitField(label='Log In')
#login form end
