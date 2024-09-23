from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    rua = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Cliente({self.nome}, {self.email}, {self.telefone}, {self.cep}, {self.rua}, {self.numero}, {self.bairro}, {self.cidade}, {self.estado})'

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'Produto({self.nome}, {self.descricao}, {self.preco}, {self.quantidade})'
    
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

    
#class Venda(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    produto = db.Column(Produto(db.Intege,db.String(100),db.Float), nullable=False)
#    data = db.Column(db.DateTime, nullable=False)