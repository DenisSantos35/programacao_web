from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html', titulo = 'LOGIN')

@app.route('/login', methods=['POST'])
def login():
    login_user = request.form['login']
    senha = request.form['senha']
    if login_user == 'admin' and senha == '123':
        return render_template('cliente.html', titulo = 'PAGE CLIENT')
    else:
        return render_template('login.html', titulo = 'LOGIN', resposta = 'Usuario ou senha')
    

@app.route('/login/cliente')
def cliente():
    return 

app.run()
