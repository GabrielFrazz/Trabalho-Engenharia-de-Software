import requests

def delete_all_clients():
    url = 'http://localhost:5000/api/clientes/delete_all'  # Adjust the URL to match your server configuration
    response = requests.delete(url)
    
    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print(f"Failed to delete clients. Status code: {response.status_code}")

if __name__ == "__main__":
    delete_all_clients()