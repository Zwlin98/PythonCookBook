# Create by Zwlin
xpts = [1, 5, 6, 2, 10, 7]

ypts = ["foo","bar","text","hello","Tim"]

for x,y in zip(xpts,ypts):
    print(x,y)

print(dict(zip(xpts,ypts)))