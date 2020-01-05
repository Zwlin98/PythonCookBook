from functools import partial


def spam(a, b, c, d):
    print(a, b, c, d)


s1 = partial(spam, 1)

s1(3, 4, 5)
s1(5, 6, 7)

s2 = partial(spam, d=3)

s2(1, 2, 4)
