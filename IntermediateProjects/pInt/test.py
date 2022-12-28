import requests

url = "https://api.apilayer.com/fixer/symbols"

payload = {}
headers= {
  "apikey": "NdUqBM1G5hVn84mA3DtZeHf8zywGNl8n"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.json()
print(result['symbols'].keys())