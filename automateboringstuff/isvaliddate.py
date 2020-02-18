import re

def isLeap(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def isValidDate(date_str):
  ptn = re.compile(r'''^(0|[1-9]|[1-2][0-9]|3[0-1]/
    0[1-9]|1[0-2]/
    [1-2][0-9][0-9][0-9]$)''',re.VERBOSE)
  if not ptn.match(date_str):
    print "No match"
    return False
  else:
    day,month,year = date_str.split('/')
    if month in ['04','06','09','11'] and int(day) > 30:
      return False
    elif month == '02':
      if isLeap(int(year)):
        return int(day) <= 29
      else:
        return int(day) <= 28
    else:
      return (int(month)<=12 and int(day)<=31)

print isValidDate('03/13/2091')
