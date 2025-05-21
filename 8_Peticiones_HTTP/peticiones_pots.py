

import requests

url ="https://webhook.site/3c764bb9-cc75-49dc-9816-3e60e426fab1"

payload = {"plato":"pasta","cantidad":2}
query_params = {"nombre":"Paco","plato":"pasta","cantidad":2}
response = requests.post(url, data=payload, params=query_params)

print(response.status_code)
#print(response.json())