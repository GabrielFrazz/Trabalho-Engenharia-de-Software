import os
from flask import Blueprint, jsonify, request, send_from_directory
from app.models import Cliente, Produto
from app.models import Sale
from app import app, db

api = Blueprint('api', __name__)


@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    clientes_list = [{"id": c.id, "name": c.name, "email": c.email, "cel": c.cel, "cep": c.cep, "logradouro": c.logradouro,
                      "numero": c.numero, "bairro": c.bairro, "cidade": c.cidade, "estado": c.estado} for c in clientes]
    return jsonify(clientes_list)


@app.route('/api/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    novo_cliente = Cliente(
        name=data['name'],
        email=data['email'],
        cel=data['cel'],
        cep=data['cep'],
        logradouro=data['logradouro'],
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
    cliente.name = data['name']
    cliente.email = data['email']
    cliente.cel = data['cel']
    cliente.cep = data['cep']
    cliente.logradouro = data['logradouro']
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


@app.route('/api/clientes/search', methods=['GET'])
def search_cliente():
    name = request.args.get('name')
    clientes = Cliente.query.filter(Cliente.name.ilike(f'%{name}%')).all()
    clientes_list = [{"id": c.id, "name": c.name, "email": c.email, "cel": c.cel, "cep": c.cep, "logradouro": c.logradouro,
                      "numero": c.numero, "bairro": c.bairro, "cidade": c.cidade, "estado": c.estado} for c in clientes]
    return jsonify(clientes_list)

# search by id


@app.route('/api/clientes/search_id', methods=['GET'])
def search_cliente_id():
    id = request.args.get('id')
    clientes = Cliente.query.filter(Cliente.id.ilike(f'%{id}%')).all()
    clientes_list = [{"id": c.id, "name": c.name, "email": c.email, "cel": c.cel, "cep": c.cep, "logradouro": c.logradouro,
                      "numero": c.numero, "bairro": c.bairro, "cidade": c.cidade, "estado": c.estado} for c in clientes]
    return jsonify(clientes_list)


# delete all clientes, route /api/clientes/delete_all
@app.route('/api/clientes/delete_all', methods=['DELETE'])
def delete_all_clientes():
    clientes = Cliente.query.all()
    for c in clientes:
        db.session.delete(c)
    db.session.commit()
    return jsonify({"message": "Todos os clientes foram deletados com sucesso!"})

# returns the number of clientes, route /api/clientes/count


@app.route('/api/clientes/count', methods=['GET'])
def count_clientes():
    count = Cliente.query.count()
    return jsonify({"count": count})


# SALES # ##########################################################################################################

@app.route('/api/sales', methods=['GET'])
def get_sales():
    sales = Sale.query.all()
    sales_list = [{"id": c.id, "cliente": c.cliente, "produto": c.produto, "amount": c.amount, "price": c.price, "date": c.date} for c in sales]
    return jsonify(sales_list)


@app.route('/api/sales', methods=['POST'])
def create_sale():
    data = request.get_json()
    nova_venda = Sale(
        cliente=data['cliente'],
        produto=data['produto'],
        amount=data['amount'],
        price=data['price'],
        date=data['date']
    )
    db.session.add(nova_venda)
    db.session.commit()
    return jsonify({"message": "Venda adicionada com sucesso!"}), 201


@app.route('/api/sales/<int:id>', methods=['PUT'])
def update_sale(id):
    venda = Sale.query.get_or_404(id)
    data = request.get_json()
    venda.cliente = data['cliente']
    venda.produto = data['produto']
    venda.amount = data['amount']
    venda.price = data['price']
    venda.date = data['date']
    db.session.commit()
    return jsonify({"message": "Venda atualizada com sucesso!"})


@app.route('/api/sales/<int:id>', methods=['DELETE'])
def delete_sale(id):
    venda = Sale.query.get_or_404(id)
    db.session.delete(venda)
    db.session.commit()

    return jsonify({"message": "Venda deletada com sucesso!"})


@app.route('/api/sales/search', methods=['GET'])
def search_sale():
    produto = request.args.get('produto')
    vendas = Sale.query.filter(Sale.produto.ilike(f'%{produto}%')).all()
    sales_list = [{"id": c.id, "cliente": c.cliente, "produto": c.produto, "amount": c.amount, "price": c.price, "date": c.date} for c in vendas]
    return jsonify(sales_list)

# search by id


@app.route('/api/sales/search_id', methods=['GET'])
def search_sale_id():
    id = request.args.get('id')
    vendas = Sale.query.filter(Sale.id.ilike(f'%{id}%')).all()
    sales_list = [{"id": c.id, "cliente": c.cliente, "produto": c.produto, "amount": c.amount, "price": c.price, "date": c.date} for c in vendas]
    return jsonify(sales_list)


# delete all vendas, route /api/sales/delete_all
@app.route('/api/sales/delete_all', methods=['DELETE'])
def delete_all_sales():
    vendas = Sale.query.all()
    for c in vendas:
        db.session.delete(c)
    db.session.commit()
    return jsonify({"message": "Todas as vendas foram deletadas com sucesso!"})

# returns the number of vendas, route /api/sales/count


@app.route('/api/sales/count', methods=['GET'])
def count_sales():
    count = Sale.query.count()
    return jsonify({"count": count})


# STOCK # ##########################################################################################################

@app.route('/api/produtos', methods=['POST'])
def create_produto():
    data = request.get_json()
    novo_produto = Produto(
        name=data['name'],
        preco=data['preco'],
        quantidade=data['quantidade']
    )
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({"message": "Produto adicionado com sucesso!"}), 201



