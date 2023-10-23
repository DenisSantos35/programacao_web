from flask import Flask, render_template, request
import mysql.connector





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
@app.route("/homePage")
def getHomePage():
    return render_template('homePage.html', Titulo = "Home Page")
    
@app.route("/createUser")
def createUser():
    return render_template('createAcount.html', titulo = "CADASTRAR USUÁRIO") 

@app.route("/createUser/insert", methods = ["POST"])
def saveDataBase():
    name = request.form['name']
    email =request.form['email']
    senha = request.form['senha']    
    
    newUserInsert(name, senha, email)      
    return render_template('homePage.html', Titulo = "Home Page", resposta = 'Deseja cadastrar cliente') 
    
@app.route("/createUser/cliente")
def createCliente():
    return render_template('cadastroCliente.html', titulo = 'Cadastrar Cliente', resposta = 'Cliente cadastrado com sucesso')

@app.route("/createUser/post", methods = ["POST"])
def searchCliente():
    name = request.form['name']
    cpf = request.form['cpf']
    email = request.form['email']
    endereco = request.form['endereco']
    bairro = request.form['bairro']
    cep = request.form['cep']
    cidade = request.form['cidade']
    
    print(name, cpf, email, endereco, bairro, cep, cidade)
    return render_template('homePage.html', Titulo = "Home Page", resposta ='Cliente cadastrado com sucesso' )


# Conecao com banco e um insert
def conn():
    return mysql.connector.connect(
        host = 'mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
        user = 'aluno_fatec',
        password = 'aluno_fatec',   
        database = 'meu_banco' 
    )
    
# insert no banco de dados
def newUserInsert(user, password, email):
    db = conn()
    myCursor = db.cursor()
    query = "INSERT INTO denis_TB_user (USUARIO, SENHA, EMAIL) VALUES (%s,%s, %s)"
    values = (user, password, email)
    myCursor.execute(query, values)
    db.commit()
    return "Dados salvo com sucesso"



   

app.run()
    

