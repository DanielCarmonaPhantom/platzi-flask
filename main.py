from flask import Flask, make_response, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr 
    response = make_response(redirect('/hello'))
    response.set_cookie('user_id', user_ip)
    return response

@app.route('/hello')
def hello():
    user_id = request.cookies.get('user_id')
    return f'Hola Mundo, Tu ip es {user_id}'