import time
from functools import wraps


def timethis(func):
    '''
    Decorator that reports the execution time.
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
def countdown(n: int):
    """
    counts down
    """
    while n > 0:
        n -= 1

# countdown(1000)
# print(countdown.__name__)
# print(countdown.__doc__)
# print(countdown.__annotations__)
# print(countdown.__wrapped__)
# print(countdown)


'''
An important feature of the @wraps decorator is that it makes the wrapped function
available to you in the __wrapped__ attribute
'''

from inspect import signature
print(signature(countdown))

