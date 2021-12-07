import re

text = 'fdsfdsfdsf\n\n\n\n\ndsdfdf\ndf\n\n\ndsffdsfds'
print(text)

print('----------')

text = re.sub(r'\n+', '\n', text)
print(text)