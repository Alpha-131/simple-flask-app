from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_app.users.forms import Registration_form, Login_form
from flask_login import login_user, current_user, logout_user, login_required
from flask_app import db, bcrypt
from flask_app.models import User


users = Blueprint(name='users', import_name=__name__)

# Register route start
@users.route('/register', methods= ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = Registration_form()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)
# Register route end


# login route start
@users.route('/login', methods= ['GET', 'POST']) 
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = Login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Logged In successfully!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Unable to login. Please check email and password', 'danger')
            
    return render_template('login.html', title='Login', form=form)
# login route end


# submit route start
@users.route('/submit')
def submit():
    return render_template('submit_file.html')

