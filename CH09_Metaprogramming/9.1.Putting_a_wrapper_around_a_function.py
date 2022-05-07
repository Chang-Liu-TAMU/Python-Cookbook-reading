# @Time: 2022/4/27 16:43
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:9.1.Putting_a_wrapper_around_a_function.py

import time
from functools import wraps


def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@timethis
def accumu(n):
    a = 0
    for i in range(n):
        a += i

accumu(1000000)
accumu(10000000)

'''
@timethis
def countdown(n):
    pass
    
    ||
    ||equals
    ||

def countdown(n):
    pass
countdown = timethis(countdown)
'''

class A:
    @classmethod
    def method(cls):
        print(cls)

class B:
    def method(self):
        # cls and self do not matter at all
        print(self)
    method = classmethod(method)

A.method()
B.method()