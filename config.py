import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Configurações do banco de dados
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'meu_banco.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'minha_chave_secreta'
