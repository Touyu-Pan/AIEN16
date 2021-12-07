import json

text = '{"3001": 128,"3012": 54}'
obj = json.loads(text)
print(obj)
print(obj['3012'])

obj['2330'] = 600
text = json.dumps(obj)
print(text)