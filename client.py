#How do we make a request to our API?

import requests

URL = "http://127.0.0.1:5000/api/items"

response = requests.get(URL).json()

print(response)
