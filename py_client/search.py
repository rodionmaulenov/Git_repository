import requests
from getpass import getpass

endpoint_1 = "http://localhost:8000/api/auth/"

username = input('Write your own username\n')
password = getpass('Write your own password\n')

data = {
    'username': username,
    "password": password
}

auth_response = requests.post(endpoint_1, json=data)
print(auth_response.json())

if auth_response.status_code == 200:
    endpoint_2 = "http://127.0.0.1:8000/api/search/"
    token = auth_response.json()['token']

    data = {
        "Authorization": f"Token {token}"
    }

    get_response = requests.post(endpoint_2, json={'search': 'hello'}, headers=data)
    print(get_response.json())