from flask import render_template, redirect, url_for, request, flash, session
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from app import app, db
from app.models import Cliente, Produto, Sale
from app.engine.security import Admin


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('landingPage'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def landingPage():
    return render_template('landingPage.html')


@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        admin = Admin()
        username = request.form['username']
        password = request.form['password']

        if admin.check_username(username) and admin.check_password(password):
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('Usuário ou senha incorretos!', category=['errorlogin'])
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('landingPage'))


@app.route('/register', methods=['GET'])
@login_required
def register():
    return render_template('register.html')


@app.route('/sales', methods=['GET'])
@login_required
def sales():
    return render_template('sales.html')


@app.route('/payment', methods=['GET'])
@login_required
def payment():
    return render_template('payment.html')


@app.route('/graphics', methods=['GET'])
@login_required
def graphics():
    return render_template('graphics.html')


@app.route('/feedback', methods=['GET'])
@login_required
def feedback():
    return render_template('feedback.html')


@app.route('/temp1', methods=['GET'])
@login_required
def temp1():
    return render_template('temp1.html')


@app.route('/temp2', methods=['GET'])
@login_required
def temp2():
    return render_template('temp2.html')


@app.route('/payment_template', methods=['GET'])
@login_required
def payment_template():
    return render_template('payment_template.html')


@app.route('/searchRegister')
@login_required
def search_register():
    id = request.args.get('id')
    cliente = Cliente.query.filter(Cliente.id.ilike(f'%{id}%')).first()
    if cliente:
        return render_template('searchRegister.html', cliente=cliente)
    else:
        flash('Cliente não encontrado!', category=['danger'])
        return redirect(url_for('temp1'))


@app.route('/notFoundRegister', methods=['GET'])
@login_required
def notFoundRegister():
    return render_template('notFoundRegister.html')


@app.route('/searchSales', methods=['GET'])
@login_required
def searchSales():
    id = request.args.get('id')
    sale = Sale.query.filter(Sale.id.ilike(f'%{id}%')).first()
    if sale:
        return render_template('searchSales.html', sale=sale)
    else:
        flash('Venda não encontrada!', category=['danger'])
        return redirect(url_for('temp2'))


@app.route('/notFoundSales', methods=['GET'])
@login_required
def notFoundSales():
    return render_template('notFoundSales.html')


@app.route('/stock_template', methods=['GET'])
@login_required
def stock_template():
    return render_template('stock_template.html')


@app.route('/stock_register', methods=['GET'])
@login_required
def stock_register():
    return render_template('stock_register.html')


@app.route('/stock_register', methods=['POST'])
@login_required
def add_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        quantidade = request.form['quantidade']

        success, message = Produto.add_produto(nome, preco, quantidade)
        if success:
            flash(message, category=['success'])
            return redirect(url_for('stock_template'))
        else:
            flash(message, category=['danger'])
            return redirect(url_for('stock_register'))
        
            
@app.route('/stock_search', methods=['GET'])
@login_required
def stock_search():
    return render_template('stock_search.html')


@app.route('/stock_not_found', methods=['GET'])
@login_required
def stock_not_found():
    return render_template('stock_not_found.html')


@app.route('/update_credentials', methods=['POST'])
@login_required
def update_credentials():
    admin = Admin()
    new_username = request.form['username']
    new_password = request.form['password']
    admin.update_credentials(new_username, new_password)
    flash('Credentials updated successfully!', category=["successsup"])
    return redirect(url_for('index'))


@app.route('/register', methods=['GET'])
@login_required
def add_cliente_form():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
@login_required
def add_cliente():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cel = request.form['cel']
        cep = request.form['cep']
        logradouro = request.form['logradouro']
        numero = request.form['numero']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']

        success, message = Cliente.add_cliente(
            name, email, cel, cep, logradouro, numero, bairro, cidade, estado)
        if success:
            flash(message, category=['success'])
            return redirect(url_for('temp1'))
            
        else:
            flash(message, category=['danger'])
            return redirect(url_for('register'))
        
@app.route('/sales', methods=['POST'])
@login_required
def add_venda():
    if request.method == 'POST':
        amount = request.form['amount']
        price = request.form['price']
        date = request.form['date']
        cliente = request.form['cliente']
        produto = request.form['produto']

        #debug flash
        flash(f'Cliente: {cliente}, Produto: {produto}, Quantidade: {amount}, Preço: {price}, Data: {date}', category=['info'])
        # Assuming Sale.add_venda is a class method that handles adding a sale
        success, message = Sale.add_venda(cliente, produto, amount, price, date)
        if success:
            flash(message, category=['success'])
            return redirect(url_for('temp2'))
        else:
            flash(message, category=['danger'])
            return redirect(url_for('sales'))


@app.route('/api/help')
def api_help():
    return render_template('api_documentation.html')