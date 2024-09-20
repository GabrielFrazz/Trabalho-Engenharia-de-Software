import os
from flask import Blueprint, app, jsonify, request, send_from_directory
from app.models import Cliente
from app import app, db

api = Blueprint('api', __name__)

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    clientes_list = [{"id": c.id, "nome": c.nome, "email": c.email, "telefone": c.telefone, "endereco": c.endereco} for c in clientes]
    return jsonify(clientes_list)

@app.route('/api/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    novo_cliente = Cliente(nome=data['nome'], email=data['email'], telefone=data['telefone'], endereco=data['endereco'])
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
    cliente.endereco = data['endereco']
    db.session.commit()
    return jsonify({"message": "Cliente atualizado com sucesso!"})

@app.route('/api/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({"message": "Cliente deletado com sucesso!"})

