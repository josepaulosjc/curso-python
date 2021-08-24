from flask import Flask, request, jsonify
from flask.helpers import make_response
app = Flask(__name__)

usuarios = {}

@app.route('/usuarios/<id>', methods=['GET'])
def get_usuario(id):
    if int(id) in usuarios:
        return jsonify({'id':id, 'email':usuarios[int(id)]})
    return jsonify({"status":'inexistente'}), 404

@app.route('/usuarios', methods=['POST'])
def add__usuario():
    usuario = request.json
    print('entrou no post')
    if not (usuario['id'] in usuarios):
        response = jsonify({'id':usuario['id'], 'email':usuario['email']})
        response.status_code = 201
        response.headers['location'] = f"/usuarios/{usuario['id']}"
        usuarios[usuario["id"]]=usuario['email']
        print(response.headers)
        return response
    print('nao entrou no if')
    response = jsonify({"status": f"usuario {usuario['id']} existe"})
    response.status_code = 422
    return response

@app.route('/usuarios/<id>', methods=['PUT'])
def replace_usuario(id):
    usuario = request.json
    if int(id) in usuarios:
        usuarios[int(id)]=usuario['email']
        return '', 204 # no content response
    response = make_response(jsonify({'status': 'Not found'}), 404)
    return response

@app.route('/usuarios/<id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = request.json
    if int(id) in usuarios:
        del usuarios[int(id)]
        return '', 204 # no content response
    response = make_response(jsonify({'status': 'Not found'}), 404)
    return response

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=8080)
