import requests
#Hello world 
endpoint = "http://localhost:8000/api/"


get_response = requests.post(endpoint, json={'content': 'Hello World!'})

print(get_response.json())
