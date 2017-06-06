import re

# This code validate the email address
m = r'^([\w\_\.\-]+)@([\w]+\..*)$'
n = re.match(m, 'mikucyy@163.com')
print(n.groups())
