import urllib.parse as UP

url = 'https://24h.pchome.com.tw/prod/DYAJ84-1900BXR5W?fq=/S/DYAJ84'
result = UP.urlparse(url)
print(result)

print(result.path)

print(result.path[6:])
print(result.path.split('/')[2])
print(result.path.replace('/prod/', ''))

pid='123'
result = result._replace(path=f'/prod/{pid}')
print(result)

url = UP.urlunparse(result)
print(url)