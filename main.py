from crypt import methods
from flask import Flask, make_response, redirect, request, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest

app = Flask(__name__)

bootstrap = Bootstrap4(app)

template_folder = './templates'
static_folder = './static'


app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Comprar Cafe', 'Enviar solicitud de compra', 'Todo M3']

class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error = error)


@app.route('/')
def index():
    user_ip = request.remote_addr 
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()

    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usuario registrado con exito')

        return redirect(url_for('index'))

    return render_template('hello.html', **context)