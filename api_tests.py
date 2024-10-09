import requests

url = 'http://localhost:5000/api/produtos'
novo_produto = {
    'name': 'Produto Teste',
    'preco': 10.0,
    'quantidade': 10
}

response = requests.post(url, json=novo_produto)

print(response.json())  # Exibe a resposta da API
