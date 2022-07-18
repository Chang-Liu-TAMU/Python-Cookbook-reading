import time
from functools import wraps
# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return r
    return wrapper

# Class illustrating application of the decorator to different kinds of methods
class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    #decorator order matters
    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    #decorator order matters
    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1
'''
The problem here is that @classmethod and @staticmethod don’t actually create objects
that are directly callable. Instead, they create special descriptor objects, as described in
Recipe 8.9. Thus, if you try to use them like functions in another decorator, the decorator
will crash. Making sure that these decorators appear first in the decorator list fixes the
problem
'''

from abc import ABCMeta, abstractmethod
class A(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def method(cls):
        pass
