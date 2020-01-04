import time
from functools import wraps


def timethis(func):
    '''
    Decorator that reports the execution time
    :param func:
    :return:
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(cnt):
    while cnt > 0:
        cnt -= 1


if __name__ == '__main__':
    countdown(100000)
    countdown(1000000)
