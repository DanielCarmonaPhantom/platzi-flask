from flask import Flask, make_response, redirect, request, render_template
app = Flask(__name__)

todos = ['Comprar Cafe', 'Enviar solicitud de compra', 'Todo M3']

@app.route('/')
def index():
    user_ip = request.remote_addr 
    response = make_response(redirect('/hello'))
    response.set_cookie('user_id', user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_id')
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('index.html', **context)