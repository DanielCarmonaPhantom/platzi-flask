from flask import Flask, make_response, redirect, request, render_template, session
from flask_bootstrap import Bootstrap4

app = Flask(__name__)

bootstrap = Bootstrap4(app)

template_folder = './templates'
static_folder = './static'


app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Comprar Cafe', 'Enviar solicitud de compra', 'Todo M3']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error = error)


@app.route('/')
def index():
    user_ip = request.remote_addr 
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('hello.html', **context)