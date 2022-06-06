class Structure:
    # Class variable that specifies expected fields
    _fields= []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


class Point(Structure):
    _fields = ['x','y']


import math
class Circle(Structure):
    _fields = ['radius']
    def area(self):
        return math.pi * self.radius ** 2

# s = Stock("acme", 50, 90)
# # print(s)
# # p = Point(1, 2)
# # print(p)
# # c = Circle(7)
# # print(c)
# # s2 = Stock("abcd", 50)


# ****************Should you decide to support keyword arguments,************

class Structure:
    _fields= []
    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        # Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))
        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))
    def __str__(self):
        l = [f"{i}={str(self.__dict__[i])}" for i in self._fields]
        return f"{str(type(self))}({','.join(l)})"

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

# s1 = Stock('ACME', 50, 91.1)
# print(s1)
# s2 = Stock('ACME', 50, price=91.1)
# print(s2)
# s3 = Stock('ACME', shares=50, price=91.1)
# print(s3)


# It leads to much less code than manually writing __init__() methods like this:
# class Stock:
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius ** 2

class Structure:
    # Class variable that specifies expected fields
    _fields= []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments (alternate)
        self.__dict__.update(zip(self._fields,args))
#>>help(Stock)



# It should be noted that it is also possible to automatically initialize instance variables
# using a utility function and a so-called “frame hack.” For example:
class Stock:
    def __init__(self, name, shares, price):
        init_fromlocals(self)

def init_fromlocals(self):
    import sys
    locs = sys._getframe(1).f_locals
    for k, v in locs.items():
        if k != 'self':
            setattr(self, k, v)


