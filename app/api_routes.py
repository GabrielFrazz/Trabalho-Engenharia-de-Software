import os
from flask import Blueprint, jsonify, request, send_from_directory
from app.models import Cliente
from app import app, db

api = Blueprint('api', __name__)

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    clientes_list = [{"id": c.id, "nome": c.nome, "email": c.email, "telefone": c.telefone, "cep": c.cep, "rua": c.rua, "numero": c.numero, "bairro": c.bairro, "cidade": c.cidade, "estado": c.estado} for c in clientes]
    return jsonify(clientes_list)

@app.route('/api/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    novo_cliente = Cliente(
        nome=data['nome'], 
        email=data['email'], 
        telefone=data['telefone'], 
        cep=data['cep'], 
        rua=data['rua'], 
        numero=data['numero'], 
        bairro=data['bairro'], 
        cidade=data['cidade'], 
        estado=data['estado']
    )
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify({"message": "Cliente adicionado com sucesso!"}), 201

@app.route('/api/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    data = request.get_json()
    cliente.nome = data['nome']
    cliente.email = data['email']
    cliente.telefone = data['telefone']
    cliente.cep = data['cep']
    cliente.rua = data['rua']
    cliente.numero = data['numero']
    cliente.bairro = data['bairro']
    cliente.cidade = data['cidade']
    cliente.estado = data['estado']
    db.session.commit()
    return jsonify({"message": "Cliente atualizado com sucesso!"})

@app.route('/api/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({"message": "Cliente deletado com sucesso!"})



# delete all clientes, route /api/clientes/delete_all
@app.route('/api/clientes/delete_all', methods=['DELETE'])
def delete_all_clientes():
    clientes = Cliente.query.all()
    for c in clientes:
        db.session.delete(c)
    db.session.commit()
    return jsonify({"message": "Todos os clientes foram deletados com sucesso!"})



