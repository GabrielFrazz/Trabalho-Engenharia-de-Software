from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import check_password_hash, generate_password_hash
from app import app, db
from app.models import Cliente, Produto
from app.engine.security import Admin

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        admin = Admin()
        username = request.form['username']
        password = request.form['password']
        
        # Verificando a senha com check_password_hash
        if admin.check_username(username) and admin.check_password(password):
            # flash('Login realizado com sucesso!', 'success') # Não é necessario e ja remove a necessidade de desaparecer com o flassh
            return redirect(url_for('index')) 
        else:
            flash('Usuário ou senha incorretos!', 'error')
    return render_template('login.html')


@app.route('/update_credentials', methods=['POST'])
def update_credentials():
    admin = Admin()
    new_username = request.form['username']
    new_password = request.form['password']
    admin.update_credentials(new_username, new_password)
    flash('Credentials updated successfully!')
    return redirect(url_for('index'))

@app.route('/add_cliente', methods=['GET'])
def add_cliente_form():
    return render_template('add_cliente.html')

@app.route('/add_cliente', methods=['GET', 'POST'])
def add_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        
        # Criando um novo cliente
        novo_cliente = Cliente(nome=nome, email=email, telefone=telefone, endereco=endereco)
        try:
            db.session.add(novo_cliente)
            db.session.commit()
            flash('Cliente adicionado com sucesso!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocorreu um erro: {e}', 'danger')
            return redirect(url_for('add_cliente'))
    return render_template('add_cliente.html')


@app.route('/api/help')
def api_help():
    return render_template('api_documentation.html')

