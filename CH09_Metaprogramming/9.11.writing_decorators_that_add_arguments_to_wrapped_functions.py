from functools import wraps

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)

# spam(1, 2, 3)
# spam(1, 2, 3, debug=True)

'''
usage example
def a(x, debug=False):
 if debug:
 print('Calling a')
 ...
def b(x, y, z, debug=False):
 if debug:
 print('Calling b')
 ...
def c(x, y, debug=False):
 if debug:
 print('Calling c')
 ...
You can refactor it into the following:
@optional_debug
def a(x):
 ...
@optional_debug
def b(x, y, z):
 ...
@optional_debug
def c(x, y
'''

#############################
'''
if the @optional_debug
decorator was applied to a function that already had a debug argument, then it would
break. If that’s a concern, an extra check could be added:
'''

from functools import wraps
import inspect
def optional_debug(func):
    if 'debug' in inspect.getfullargspec(func).args:
        raise TypeError('debug argument already defined')
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)


    #fix signatures
    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug',
                                   inspect.Parameter.KEYWORD_ONLY,
                                   default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper

@optional_debug
def add(x, y):
    return x + y

import inspect
s = inspect.signature(add)
print(type(s))
# print(str(s))
print(s)
