import base64

# This code decode the base64 bytes without '='
def safe_base64_decode(s)
  if len(s) % 4 == 0:
    return base64.b64decode(s)
  elif len(s) % 4 == 1:
    return base64.b64decode(s + b'===')
  elif len(s) % 4 == 2:
    return base64.b64decode(s + b'==')
  else:
    return base64.b64decode(s + b'=')
    
# Test
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
