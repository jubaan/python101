from flask import Flask, jsonify

app = Flask(__name__, static_url_path="")

@app.route('/json', methods=['GET'])
def ejemplo_json():
    contenido = { "id": 1, "name": "julio", "last_name": "Anoveros"}
    segundo = { "id": 1, "name": "julio", "last_name": "Anoveros"}
    lista = [contenido, segundo]

    return jsonify(lista)

@app.route('/', methods=['GET'])
def hola_mundo_con_flask():
    return 'Hola Mundo'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
