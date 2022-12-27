import requests

endpoint = "http://localhost:8000/api/product/3/update/"

data = {
    'title': 'Timur Junior'

}
get_response = requests.put(endpoint, json=data)

print(get_response.json())