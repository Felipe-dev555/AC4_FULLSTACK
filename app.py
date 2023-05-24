from flask import Flask, jsonify, request, json
import mysql.connector

app = Flask(__name__)

bancoDeDados = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="db_Carros",
    port= 3306
) 

@app.route('/listarTodos', methods=['GET'])
def listarCarros():
    selectAllSql = "SELECT * FROM carro"
    cursor = bancoDeDados.cursor()
    cursor.execute(selectAllSql)
    resultado = cursor.fetchall()

    return jsonify(resultado)

@app.route('/cadastrarCarros', methods=['POST'])
def cadastrar():
    data = json.loads(request.data)
    marca = data.get("marca", None)
    modelo = data.get("modelo", None)
    data_carro = data.get("data_carro", None)
    query = "INSERT INTO carro (marca, modelo, data_carro) VALUES (%s, %s, %s)"
    val = (marca, modelo, data_carro)
    cursor = bancoDeDados.cursor()
    cursor.execute(query, val)
    bancoDeDados.commit()
    return "Cadastrado"

if __name__ == '__main__':
    app.run(port=5000, debug=True)