import requests

url = 'https://api.ipify.org?format=json'
session = requests.session()
session.headers.update({
    'referer' : 'https://www.ipify.org',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
})
response = session.get(url)
print(response.json())