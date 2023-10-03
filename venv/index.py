from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('initPage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/cliente')
def cliente():
    return render_template('cliente.html')

app.run()
