from flask import Flask, make_response, redirect, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr 
    response = make_response(redirect('/hello'))
    response.set_cookie('user_id', user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_id')
    return render_template('index.html', user_ip=user_ip)