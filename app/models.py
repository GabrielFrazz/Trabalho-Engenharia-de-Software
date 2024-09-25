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
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'Produto({self.name}, {self.descricao}, {self.preco}, {self.quantidade})'

#classe de vendas, extends Cliente
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    produto = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f'Venda({self.cliente}, {self.data}, {self.valor})'

class Capital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atual = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'Capital({self.data}, {self.valor})'
    
class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth = db.Column(db.DateTime, nullable=False)
    position = db.Column(db.String(100), nullable=False)
    paymentValue = db.Column(db.Float, nullable=False)
    paymentDate = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'Worker({self.name}, {self.birth}, {self.position}, {self.paymentValue}, {self.paymentDate})'

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    whenDone = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'Payment({self.worker})'
    
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

    
