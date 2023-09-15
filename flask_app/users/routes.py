from flask import render_template, Blueprint
from flask_app.users.forms import Registration_form, Login_form

users = Blueprint(name='users', import_name=__name__)

# Register route start
@users.route('/register')
def register():
    form = Registration_form()
    return render_template('register.html', form=form)
# Register route end


# login route start
@users.route('/login')
def login():
    form = Login_form()
    return render_template('login.html', form=form)
# login route end


# submit route start
@users.route('/submit')
def submit():
    return render_template('submit_file.html')

