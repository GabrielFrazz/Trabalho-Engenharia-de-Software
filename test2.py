import requests
import random

# Define the base URL for the API
BASE_URL = 'http://127.0.0.1:5000/api/sales'

#  Define a function to generate random sales data
def generate_random_sales():
    cliente = random.randint(1, 10)
    data = f"202{random.randint(1,4)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
    produto = random.randint(1, 10)
    quantidade = random.randint(1, 10)
    
    return {
        "cliente": cliente,
        "data": data,
        "produto": produto,
        "quantidade": quantidade
    }

# Function to add a sale using the API
def add_sale(sale_data):
    response = requests.post(BASE_URL, json=sale_data)
    if response.status_code == 201:
        print(f"Venda para o cliente '{sale_data['cliente']}' adicionada com sucesso!")
    else:
        print(f"Erro ao adicionar venda: {response.json()}")

# Main function to populate the database with a specified number of clients
def populate_sales(num_sales):
    for i in range(num_sales):
        sales_data = generate_random_sales()
        add_sale(sales_data)

# Specify how many clients you want to add
if __name__ == '__main__':
    num_sales = int(input("Quantos vendas deseja adicionar? "))
    populate_sales(num_sales)
