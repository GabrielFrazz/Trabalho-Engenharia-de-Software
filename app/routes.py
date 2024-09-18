from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import check_password_hash, generate_password_hash
from app import app, db
from app.models import Cliente, Produto
from .engine.security import *

admin = Admin()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Verifique aqui a autenticação
        
        # Verificando a senha com check_password_hash
        if admin.check_username(username) and admin.check_password(password):
            # flash('Login realizado com sucesso!', 'success') # Não é necessario e ja remove a necessidade de desaparecer com o flassh
            return redirect(url_for('index')) 
        else:
            flash('Usuário ou senha incorretos!', 'error')
    return render_template('login.html')

