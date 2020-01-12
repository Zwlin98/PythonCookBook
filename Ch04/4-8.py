# Create by Zwlin
from itertools import dropwhile


# with open('4-4.py') as f:
#     for line in f:
#         print(line.strip())


with open('4-4.py') as f:
    cnt = 0
    for line in dropwhile(lambda line: line.strip().startswith("def"), f.readlines()):
        print(cnt,line, end='')
        cnt+=1

# with open('4-4.py') as f:
#     for line in f:
#         if 'self' not in line:
#             print(line,end='')