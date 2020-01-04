from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator1")
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator2")
        return func(*args, **kwargs)

    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


if __name__ == '__main__':
    print(add(2, 3))
    print(add.__wrapped__(2, 3))
    print(add.__wrapped__.__wrapped__(2, 3))