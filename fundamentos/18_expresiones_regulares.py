import re 
p = re.compile('ab*')
p
re.compile('ab*')

p = re.compile('ab*', re.IGNORECASE)

print(p.match('::: message'))

m = p.search('::: message'); print(m)

m.group()

m.span()