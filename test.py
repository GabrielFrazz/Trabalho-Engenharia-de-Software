import requests
import random

# Define the base URL for the API
BASE_URL = 'http://127.0.0.1:5000/api/clientes'

# Define a function to generate random client data
def generate_random_client():
    names = ["Gabriel", "Carlos", "Henrique", "Patrick", "Luan", "Kemelly", "Gustavo", "Lucas"]
    last_names = ["Silva", "Pereira", "Souza", "Gomes", "Oliveira", "Rodrigues", "Costa", "Alves"]
    
    name = random.choice(names) + " " + random.choice(last_names)
    email = f"{name.replace(' ', '').lower()}@example.com"
    cel = f"(11) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    cep = f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"
    logradouro = f"Rua {random.choice(last_names)}"
    numero = str(random.randint(1, 5000))
    bairro = f"Bairro {random.choice(last_names)}"
    cidade = "São Paulo"
    estado = "SP"
    
    return {
        "name": name,
        "email": email,
        "cel": cel,
        "cep": cep,
        "logradouro": logradouro,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado
    }

# Function to add a client using the API
def add_client(client_data):
    try:
        response = requests.post(BASE_URL, json=client_data)
        if response.status_code == 201:
            print(f"Cliente '{client_data['name']}' adicionado com sucesso!")
        else:
            print(f"Erro ao adicionar cliente: {response.json()}")
    except requests.ConnectionError as e:
        print(f"Erro de conexão: {e}")

# Main function to populate the database with a specified number of clients
def populate_clients(num_clients):
    for i in range(num_clients):
        client_data = generate_random_client()
        add_client(client_data)

# Specify how many clients you want to add
if __name__ == '__main__':
    num_clients = int(input("Quantos clientes deseja adicionar? "))
    populate_clients(num_clients)
