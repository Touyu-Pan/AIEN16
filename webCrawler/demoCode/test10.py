import re

print(re.match(r'^09\d\d\d\d\d\d\d\d$', '0912345678'))

m = re.match(r'^(?P<provider>09\d\d)\d\d\d\d\d\d$', '0912345678')
print(m.group('provider'))