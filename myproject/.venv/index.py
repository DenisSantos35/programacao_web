from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', Titulo= "PAGINA INICIAL")

@app.route("/login")
def login():
    return render_template('loginPage.html', Titulo = "Página Login") 

@app.route("/homePage", methods=["POST"] ) 
def initPage():
    user_login = request.form['name']
    user_senha = request.form['senha']    
    if user_login == 'admin' and user_senha == '123':
        return render_template('homePage.html', Titulo = "Home Page")
    else:
        return render_template('loginPage.html', Titulo = "Página Login", resposta = "Usuário ou senha incorretos") 
    
@app.route("/createUser")
def createUser():
    return render_template('createAcount.html', titulo = "CADASTRAR USUÁRIO") 

app.run()
    

