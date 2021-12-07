import urllib.parse as UP

text = '新冠肺炎'

print(UP.quote(text))

text = '%E7%96%AB%E8%8B%97'
print(UP.unquote(text))