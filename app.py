from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Bem-vindo ao restaurante!"

@app.route("/menu")
def menu():
    return "Hoje temos: sopa, frango, sobremesa."

app.run(debug=True)