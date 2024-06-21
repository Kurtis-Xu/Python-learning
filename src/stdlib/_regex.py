import re

print(re.match('hello', 'hello world'))

print(re.match('\\d+', '12345'))
print(re.match(r'\d+', '12345'))
