from flask import Flask


app = Flask(__name__)

@app.route('/aularodrig')
def index():
    return "OLa"



@app.route('/outrarora')
def outra():
    return "<h1>Outra Rota</h1>"

app.run()
