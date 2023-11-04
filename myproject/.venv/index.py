from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)    


@app.route("/")
def home():
    return render_template('index.html', Titulo= "PAGINA INICIAL")

@app.route("/login")
def login():
    return render_template('loginPage.html', Titulo = "Página Login") 

@app.route("/homePage", methods=["POST"]) 
def initPage():
    user_login = request.form['name']
    user_senha = request.form['senha']   
    if user_login == 'admin' and user_senha == '123':
        return render_template('homePage.html', Titulo = "Home Page")
    else:
        return render_template('loginPage.html', Titulo = "Página Login", resposta = "Usuário ou senha incorretos") 
    
@app.route("/homePage")
def getHomePage():
    return render_template('homePage.html', Titulo = "Home Page", resultado = "")
    
@app.route("/createUser")
def createUser():
    resultado = getQuery()
    return render_template('createAcount.html', titulo = "CADASTRAR USUÁRIO", resultado = resultado) 

@app.route("/createUser/insert", methods = ["POST"])
def saveDataBase():
    name = request.form['name']
    email =request.form['email']
    senha = request.form['senha'] 
    
    try:
        if name == "" or email == "" or senha == "":
            return render_template('homePage.html', Titulo = "Home Page", resposta = "Dados invalidos, Digite algum dado para continuar")
                        
        queryInsert(name, senha, email)
    except:
        return render_template('homePage.html', Titulo = "Home Page", resposta = "Nome ja cadastrado")         
         
    return render_template('homePage.html', Titulo = "Home Page", resposta = "Dados cadastrados com sucesso") 
    
@app.route("/createClient", methods = ["GET"])
def createCliente():
    
    resultado = querySearchCliente()
        
    return render_template('cadastroCliente.html', titulo = 'Cadastrar Cliente', resultado = resultado)

@app.route("/createClient", methods = ["POST"])
def searchCliente():
    cpf = request.form['cpf']
    nome = request.form['name']    
    email = request.form['email']
    rua = request.form['rua']
    bairro = request.form['bairro']
    cep = request.form['cep']
    cidade = request.form['cidade']    
    
    if(not cpf or not nome or not email or not rua or not bairro or not cep or not cidade ):
        return render_template('cadastroCliente.html', titulo = 'Cadastrar Cliente', resposta= "Digite os dados corretamente")
    
    queryInsertCliente(cpf, nome, email, rua, bairro, cep, cidade)    
    return render_template('homePage.html', Titulo = "Home Page", resposta = "Dados cadastrados com sucesso") 

@app.route("/excluir_usuario/<resultado>")
def excluir_usuario(resultado):
    if resultado == "":
            return render_template('homePage.html', Titulo = "Home Page", resposta = "Dados invalidos, Digite algum dado para continuar")
    print(resultado)
    delete(resultado)
    return  render_template('homePage.html', Titulo = "Home Page", resposta = "Dado deletado com sucesso") 
    


# Conecao com banco e um insert
def conn():
    return mysql.connector.connect(
        host = 'mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
        user = 'aluno_fatec',
        password = 'aluno_fatec',   
        database = 'meu_banco' 
    )
#Excluir usuário 
def delete(user):
    db = conn()
    myCursor = db.cursor()
    query = "DELETE FROM denis_TB_user WHERE USUARIO = '" + user + "'"
    print(query)
    myCursor.execute(query)
    db.commit()
    return "Dados excluidos com sucesso"

#cricao de clientes
def queryInsertCliente(cpf, nome, email, rua, bairro, cep, cidade):
    db = conn()
    myCursor = db.cursor()
    query = "INSERT INTO denis_TB_cliente (CPF, NOME, EMAIL, RUA, BAIRRO, CEP,CIDADE) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (cpf, nome, email, rua, bairro, cep, cidade)
    myCursor.execute(query, values)
    db.commit()
    return "Dados salvos com sucesso"

#buscando todos os dados dos cliente
def querySearchCliente():
    db = conn()
    mycursor = db.cursor()
    query = 'SELECT * FROM denis_TB_cliente'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return resultado   
# insert no banco de dados
def queryInsert(name, senha, email):
    db = conn()
    myCursor = db.cursor()
    query = "INSERT INTO denis_TB_user (USUARIO, SENHA, EMAIL) VALUES (%s,%s, %s)"
    values = (name, senha, email)
    myCursor.execute(query, values)
    db.commit()  
    return "Dados salvos com sucesso"

def getQuery():
    db = conn()
    mycursor = db.cursor()
    query = 'SELECT USUARIO, EMAIL FROM denis_TB_user'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return resultado    
    

app.run()
    

