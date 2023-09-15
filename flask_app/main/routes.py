from flask import render_template, Blueprint

main = Blueprint(name='main', import_name=__name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')

