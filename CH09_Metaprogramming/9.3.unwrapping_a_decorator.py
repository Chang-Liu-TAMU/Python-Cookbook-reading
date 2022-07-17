# Assuming that the decorator has been implemented properly using @wraps (see
# Recipe 9.2), you can usually gain access to the original function by accessing the __wrap
# ped__ attribute. For example:

# >>> @somedecorator
# >>> def add(x, y):
# ... return x + y
# ...
# >>> orig_add = add.__wrapped__
# >>> orig_add(3, 4)
# >>> 7

from functools import wraps
def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add(x, y):
    return x + y

add(2, 3)
add.__wrapped__(2, 3)