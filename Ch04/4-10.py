# Create by Zwlin
my_list = ['a','b','c']

for idx,val in enumerate(my_list):
    print(idx,val)

for idx, val in enumerate(my_list,1):
    print(idx, val)

for en in enumerate(my_list):
    print(en)

data = [(1,2),(3,4),(5,6),(7,8)]

for n,(x,y) in enumerate(data):
    print(n,x,y)