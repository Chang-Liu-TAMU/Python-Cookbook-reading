from functools import wraps
import logging
def logged(level, name=None, message=None):
    '''
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
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
    print('Spam!')


# add(1, 2)
# spam()

########################################
# @decorator(x, y, z)
# def func(a, b):
#     pass

#equals
# def func(a, b):
#     pass
# func = decorator(x, y, z)(func)
'''
Carefully observe that the result of decorator(x, y, z) must be a callable which, in
turn, takes a function as input and wraps it. See Recipe 9.7 for another example of a
decorator taking arguments.
'''
