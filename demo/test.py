import requests

url = "http://localhost:8000/login"

payload = {'field1_e': 'your-email@example.com', 'field2_p': 'your-password'}

headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.post(url, data=payload, headers=headers)

print(response.text)
