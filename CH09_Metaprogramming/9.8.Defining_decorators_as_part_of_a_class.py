from functools import wraps


class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper

a = A()
@a.decorator1
def spam():
    pass

# As a class method
@A.decorator2
def grok():
    pass


#usage
# class Person:
#     # Create a property instance
#     first_name = property()
#     # Apply decorator methods
#
#     @first_name.getter
#     def first_name(self):
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._first_name = value
#


# class B(A):
#     @A.decorator2 #must use A. explicitly
#     def bar(self):
#         pass