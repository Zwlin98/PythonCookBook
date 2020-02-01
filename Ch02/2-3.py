# Create by Zwlin
from fnmatch import fnmatch,fnmatchcase

print(fnmatch('foo.txt','*.TXT'))

print(fnmatchcase('foo.txt','*.TXT'))

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

res = [addr for addr in addresses if fnmatchcase(addr,'* ST')]
print(res)
res = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(res)