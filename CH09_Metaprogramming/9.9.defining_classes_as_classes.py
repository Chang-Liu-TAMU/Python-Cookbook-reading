import types
from functools import wraps
# class Profiled:
#     def __init__(self, func):
#         wraps(func)(self)
#         self.ncalls = 0
#
#     def __call__(self, *args, **kwargs):
#         print("I am __call__")
#         self.ncalls += 1
#         return self.__wrapped__(*args, **kwargs)
#
# @Profiled
# def add(x, y):
#     return x + y
# print(add)
# print(add(1, 2))

################################################
from functools import partial
class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        print(f"I am __call__")
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            ret = types.MethodType(self, instance)
            #alternative
            # ret = partial(self,instance)
            '''
            types.MethodType() makes a bound method
            first arg: "self" is a callable
            instance arg: be the default arg passed to "self"
            then types.MethodType(self, instance) is a bound method where intance is passed automatically
            '''
            # print(f"self: {self}, instance: {instance}")
            # print(type(ret))
            return ret

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)

    def foo(self, x):
        print(self, x)

s = Spam()
# print(s)
# print(s.bar)
# print(s.foo)
# print(Spam.bar.__wrapped__)
f = s.bar
# print(f)
f(1)



# def grok(self, x):
#     print(self)
#     print("I am grok")
# f = grok.__get__(s, Spam)
# print(f)
# f(1)

##############################
import types
from functools import wraps
def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper

# Example
@profiled
def add(x, y):
    return x + y