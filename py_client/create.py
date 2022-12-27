import requests

endpoint = "http://localhost:8000/api/product/"

data = {
    'title': 'Ypu are pretty',
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())