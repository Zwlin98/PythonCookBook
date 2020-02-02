# Create by Zwlin

text = 'yeah, but no, but yeah, but no, but yeah'

print(text.replace('yeah','yep'))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

import re

print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
res = pattern.sub(r'\3-\1-\2',text)

print(res)

from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2),mon_name,m.group(3))

res = pattern.sub(change_date,text)
print(res)