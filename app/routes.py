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


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/sales', methods=['GET'])
def sales():
    return render_template('sales.html')


@app.route('/payment', methods=['GET'])
def payment():
    return render_template('payment.html')


@app.route('/graphics', methods=['GET'])
def graphics():
    return render_template('graphics.html')


@app.route('/feedback', methods=['GET'])
def feedback():
    return render_template('feedback.html')


@app.route('/temp1', methods=['GET'])
def temp1():
    return render_template('temp1.html')


@app.route('/update_credentials', methods=['POST'])
def update_credentials():
    admin = Admin()
    new_username = request.form['username']
    new_password = request.form['password']
    admin.update_credentials(new_username, new_password)
    flash('Credentials updated successfully!')
    return redirect(url_for('index'))
