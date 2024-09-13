from app import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Cliente({self.nome}, {self.email}, {self.telefone}, {self.endereco})'

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'Produto({self.nome}, {self.descricao}, {self.preco}, {self.quantidade})'
    
