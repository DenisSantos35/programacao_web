from flask import Flask, render_template

app = Flask(__name__)

@app.route('/aula1')
def index():
    return render_template('aula1.html')



@app.route('/outrarora')
def outra():
    return "<h1>Outra Rota</h1>"\
        "<p>Olha a tag html do paragrafo aqui </p>"\
        "<img src = 'https://picsum.photos/200/300'>"

app.run()
