from functools import wraps
import logging


def logged(level, name=None, message=None):
    '''
    Add logging to a function,if name and message is aren't specified,
    they default to the function's module and name.
    :param level: the logging level
    :param name:  the logger name
    :param message: the log message
    '''

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print("Spam!")
