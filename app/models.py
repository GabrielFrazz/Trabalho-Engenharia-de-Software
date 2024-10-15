from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cel = db.Column(db.String(20), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    logradouro = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Cliente({self.name}, {self.email}, {self.cel}, {self.cep}, {self.logradouro}, {self.numero}, {self.bairro}, {self.cidade}, {self.estado})'
        
    @staticmethod
    def add_cliente(name, email, cel, cep, logradouro, numero, bairro, cidade, estado):
        novo_cliente = Cliente(
            name=name, 
            email=email, 
            cel=cel, 
            cep=cep, 
            logradouro=logradouro, 
            numero=numero, 
            bairro=bairro, 
            cidade=cidade, 
            estado=estado
        )
        try:
            db.session.add(novo_cliente)
            db.session.commit()
            return True, "Cliente adicionado com sucesso!"
        except Exception as e:
            db.session.rollback()
            return False, f"Ocorreu um erro: {e}"
        
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    
    def __repr__(self):
        return f'Produto({self.name}, {self.price}, {self.amount}, {self.description})'
    
    @staticmethod
    def add_produto(name, price, amount, description):
        novo_produto = Produto( 
            name=name,
            price=price, 
            amount=amount,
            description=description
        )
        try:
            db.session.add(novo_produto)
            db.session.commit()
            return True, "Produto adicionado com sucesso!"
        except Exception as e:
            #print(e)
            db.session.rollback()
            return False, f"Ocorreu um erro: {e}"


#classe de vendas, extends Cliente
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.Integer, nullable=False)
    produto = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f'Venda({self.cliente}, {self.produto}, {self.amount}, {self.price}, {self.date})'
    
    @staticmethod
    def add_venda(cliente, produto, amount, price, date):
        nova_venda = Sale(
            cliente=cliente, 
            produto=produto,
            amount=amount, 
            price=price, 
            date=date 
        )
        try:
            db.session.add(nova_venda)
            db.session.commit()
            return True, "Venda adicionado com sucesso!"
        except Exception as e:
            #print(e)
            db.session.rollback()
            return False, f"Ocorreu um erro: {e}"

class Capital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atual = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'Capital({self.data}, {self.valor})'
        
    @staticmethod
    def get_capital():
        return Capital.query.first()
    
    @staticmethod
    def set_initial_capital():
        if not Capital.query.first():
            capital = Capital(id=1, atual=100000.00)
            db.session.add(capital)
            db.session.commit()
    
class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    paymentValue = db.Column(db.Float, nullable=False)
    paymentDate = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'Worker({self.name}, {self.birth}, {self.position}, {self.paymentValue}, {self.paymentDate})'
    
    @staticmethod
    def add_worker(name, birth, position, paymentValue, paymentDate):
        novo_trabalhador = Worker( 
            name = name,
            birth = birth, 
            position = position,
            paymentValue = paymentValue,
            paymentDate = paymentDate,
        )
        try:
            db.session.add(novo_trabalhador)
            db.session.commit()
            return True, "Trabalhador adicionado com sucesso!"
        except Exception as e:
            #print(e)
            db.session.rollback()
            return False, f"Ocorreu um erro: {e}"

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    workerid = db.Column(db.Integer, nullable=False)
    whenDone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'Payment({self.value}, {self.workerid}, {self.whenDone})'
    
    @staticmethod
    def add_payment(value, workerid, whenDone):
        novo_pagamento = Worker( 
            value = value,
            workerid = workerid, 
            whenDone = whenDone
        )
        try:
            db.session.add(novo_pagamento)
            db.session.commit()
            return True, "Trabalhador adicionado com sucesso!"
        except Exception as e:
            #print(e)
            db.session.rollback()
            return False, f"Ocorreu um erro: {e}"
    
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f'Feedback({self.name}, {self.date}, {self.message})'
    
    
class MasterUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'MasterUser({self.username}, {self.password})'
    
    @staticmethod
    def get_master_user():
        return MasterUser.query.first()
    
    @staticmethod
    def set_initial_admin():
        if not MasterUser.query.first():
            hashed_password = generate_password_hash('admin')
            admin = MasterUser(username='admin', password=hashed_password)
            db.session.add(admin)
            db.session.commit()

    
class Meses (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mes = db.Column(db.String(10), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'Meses({self.mes}, {self.valor})'
    
    