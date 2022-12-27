import requests

input_pk = input("Write your number /n")

try:
    int_number = str(input_pk)
except:
    int_number = None
    print('Write whole number')

if int_number:
    endpoint = f"http://localhost:8000/api/product/{int_number}/delete/"

    get_response = requests.delete(endpoint)

    print(get_response.status_code, get_response.status_code == 204)