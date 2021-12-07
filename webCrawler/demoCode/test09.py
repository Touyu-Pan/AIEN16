import re

print(re.match(r'^09\d\d\d\d\d\d\d\d$', '0912345678'))

print(re.match(r'^[a-zA-Z]\d\d\d\d\d\d\d\d\d$', 'N123456789'))
print(re.match(r'^[a-zA-Z]\d\d\d\d\d\d\d\d\d$', 'n123456789'))

print(re.match(r'^\w\d\d\d\d\d\d\d\d\d$', 'N123456789'))
print(re.match(r'^\w\d\d\d\d\d\d\d\d\d$', 'n123456789'))

print(re.match(r'^\w\d\d\d\d\s\s\d\d\d\d\d$', 'n1234\n\t56789'))

print(re.match(r'^\w\d{4}\s{2}\d{5}$', 'n1234\n\t56789'))