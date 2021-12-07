import requests

url = 'https://api.ipify.org?format=json'
response = requests.get(url)
print(response.json())