# Create by Zwlin
import re
text = 'yeah, but no, but yeah, but no, but yeah'

text.find('abc')

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

if re.match(r'\d+/\d+\d+',text1):
    print('Yes')
else:
    print('No')

if re.match(r'\d+/\d+\d+',text2):
    print('Yes')
else:
    print('No')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
res = re.findall(pattern,text)
print(res)