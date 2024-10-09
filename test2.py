import requests
import random
import test

# Define the base URL for the API
BASE_URL = 'http://127.0.0.1:5000/api/sales'

#  Define a function to generate random sales data
def generate_random_sales(i):
    names = ["Gabriel", "Carlos", "Henrique", "Patrick", "Luan", "Kemelly", "Gustavo", "Lucas"]
    last_names = ["Silva", "Pereira", "Souza", "Gomes", "Oliveira", "Rodrigues", "Costa", "Alves"]
    
    cliente = i # random.choice(names) + " " + random.choice(last_names)
    produto = random.randint(1, 10)
    amount = random.randint(1, 10)
    price = random.randint(1, 10)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)
    if mes <= 9:
        if dia <= 9:
            date = f"2024-0{mes}-0{dia}"
        else:
            date = f"2024-0{mes}-{dia}"
    else:
        if dia <= 9:
            date = f"2024-{mes}-0{dia}"
        else:
            date = f"2024-{mes}-{dia}"
    
    
    return {
        "cliente": cliente,
        "produto": produto,
        "amount": amount,
        "price": price,
        "date": date
    }

# Function to add a sale using the API
def add_sale(sale_data):
    try:
        response = requests.post(BASE_URL, json=sale_data)
        if response.status_code == 201:
            print(f"Venda para o cliente '{sale_data['cliente']}' adicionada com sucesso!")
        else:
            try:
                # Tenta obter a resposta em JSON, caso seja válida
                error_message = response.json()
            except requests.exceptions.JSONDecodeError:
                # Se a resposta não for um JSON válido, captura o texto simples
                error_message = response.text
            print(f"Erro ao adicionar venda: {error_message}")
    except requests.ConnectionError as e:
        print(f"Erro de conexão: {e}")

# Main function to populate the database with a specified number of clients
def populate_sales(num_sales):
    for i in range(num_sales):
        sales_data = generate_random_sales(i)
        add_sale(sales_data)

# Specify how many clients you want to add
if __name__ == '__main__':
    num_sales = int(input("Quantos vendas deseja adicionar? "))
    populate_sales(num_sales)
