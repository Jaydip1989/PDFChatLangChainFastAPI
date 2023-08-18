import requests
import json
url = "http://127.0.0.1:8000/orders_pydantic"

header = {
    'accept':'application/json',
    'Content-Type':'application/json'
}

params = {
    'product':'desktop',
    'units':'3'
}

response = requests.post(url, headers=header, data=json.dumps(params))
print(response.json())