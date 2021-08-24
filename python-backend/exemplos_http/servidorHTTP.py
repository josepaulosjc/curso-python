from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/",methods=['GET'])
def raiz():
    return "<p>Raiz GET!</p>"

@app.route("/usuarios/<usuario>", methods=['GET'])
def usuario(usuario):
    return f"<p>Usuario = {usuario}</p>"

@app.route("/usuarios/incluir",methods=['POST'])
def incluir():
    return f"<p>{request.form['usuario']}, {request.form['senha']}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)