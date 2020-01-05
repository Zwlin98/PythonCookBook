# 默认参数
def spam(a, b=66):
    print(a, b)


def spam1(a, b=None):
    if b is None:
        b = []
    pass


_no_value = object()


def spam2(a, b=_no_value):
    if b is _no_value:
        print("No b value supplied")
    pass


spam2(1)
