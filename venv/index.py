from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('initPage.html', titulo = 'INIT PAGE')

@app.route('/login')
def login():
    return render_template('login.html', titulo = 'LOGIN')

@app.route('/login/cliente')
def cliente():
    return render_template('cliente.html', titulo = 'PAGE CLIENT')

app.run()
