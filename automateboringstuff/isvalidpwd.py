import re

def isValidPwd(pwd):
  up = re.compile(r'[A-Z]').search(pwd)
  low = re.compile(r'[a-z]').search(pwd)
  num = re.compile(r'\d').search(pwd)
  if len(pwd) < 8:
    return False
  elif up and low and num:
    return True
  else:
    return False

print isValidPwd('Password123')

