from flask import render_template, Blueprint

users = Blueprint(name='users', import_name=__name__)

@users.route('/register')
def register():
    return render_template('register.html')


@users.route('/login')
def login():
    return render_template('login.html')


@users.route('/submit')
def submit():
    return render_template('submit.html')

