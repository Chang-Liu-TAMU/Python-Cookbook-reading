# @Time: 2022/5/17 14:14
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:8.6.create_managed_attributes.py

'''
It’s important to stress that the @first_name.setter and
@first_name.deleter decorators won’t be defined unless first_name was already es‐
tablished as a property using @property.

A critical feature of a property is that it looks like a normal attribute, but access auto‐
matically triggers the getter, setter, and deleter methods
'''
# class Person:
#     def __init__(self, first_name):
#         self.first_name = first_name
#         #using self.first_name = first_name in __init__
#         # to trigger setter function, type checking when initializing
#
#     # Getter function
#     @property
#     def first_name(self):
#         return self._first_name
#
#     # Setter function
#     @first_name.setter
#     def first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._first_name = value
#
#     # Deleter function (optional)
#     @first_name.deleter
#     def first_name(self):
#         raise AttributeError("Can't delete attribute")

#alternative definition getter, deleter, setter
class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")
    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)
    #name is the property name defined by ourself to be accessed


# print(Person.name.fget)
# p = Person(123)
#can directly call getter ...
#p.get_first_name()

#avoid code like this
# class Person:
#     def __init__(self, name):
#         self.first_name = name
#
#     @property
#     def first_name(self):
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self, value):
#         self._first_name = value


#usage
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


#avoid repetition like this
# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def first_name(self):
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._first_name = value
#
#     # Repeated property code, but for a different name (bad!)
#     @property
#     def last_name(self):
#         return self._last_name
#
#     @last_name.setter
#     def last_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._last_name = value