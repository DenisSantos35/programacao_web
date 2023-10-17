from flask import Flask, render_template, request

app = Flask(__name__)

# ************** route pagina inicial ******************************
@app.route('/')
def initPage():
    return render_template('index.html', titulo = "PÁGINA INICIAL")

# **************** route pagina login ******************************
@app.route('/login')
def login():
    return render_template('login.html', titulo = 'LOGIN')

@app.route('/homePage', methods=['POST'])
def homePage():
    user = request.form['name']
    senha = request.form['senha']
    
    if user == 'admin' and senha == '123':
        return render_template('homePage.html', titulo = "HOME PAGE")
    else:
        return render_template('login.html', titulo = 'LOGIN', resposta = "Senha ou email incorretos, tente novamente!")
    
@app.route('/createAccount')
def createAccount():
    return render_template('createAccount.html', titulo = 'CADASTRAR USUÁRIO')

@app.route('/login', methods=['POST'])
def returnLogin():
    user = request.form['name']
    senha = request.form['senha']

    if user != "" and senha != "":
        return render_template('index.html', titulo = "PÁGINA INICIAL")
    else:
        return render_template('createAccount.html', titulo = "CADASTRAR USUÁRIO",resposta = 'Digite um nome e uma senha para cadastrar o usuário')

app.run()

