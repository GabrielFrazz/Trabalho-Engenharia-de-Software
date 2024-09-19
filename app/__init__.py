from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_projeto.db'
app.config['SECRET_KEY'] = 'minha_chave_secreta'
db = SQLAlchemy(app)

# Import models to ensure they are registered with SQLAlchemy
from app import models

# Import routes within the app context
with app.app_context():
    from app import routes

