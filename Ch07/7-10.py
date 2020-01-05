def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


apply_async(add, (2, 3), callback=print_result)
# Got: 5
apply_async(add, ("hello", "world"), callback=print_result)


# Got: helloworld


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ("hello", "world"), callback=r.handler)


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ("hello", "world"), callback=handler)


def make_handler1():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


handler = make_handler1()
next(handler)
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ("hello", "world"), callback=handler.send)
