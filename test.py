import requests

url = 'http://localhost:5000/api/clientes/1'  # Substitua o ID pelo cliente desejado

response = requests.delete(url)

print(response.json())  # Exibe a resposta da API