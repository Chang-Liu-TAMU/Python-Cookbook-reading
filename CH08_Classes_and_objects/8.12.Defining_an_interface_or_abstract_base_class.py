from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass
    @abstractmethod
    def write(self, data):
        pass

# a = IStream()
#can not isstantiate abstract class IStream with abs methods

# Code that explicitly checks for this interface could be written as follows:
def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')

##
import io
# Register the built-in I/O classes as supporting our interface
IStream.register(io.IOBase)
# Open a normal file and type check
f = open('foo.txt', "w")
print(isinstance(f, IStream)) # Returns True


# It should be noted that @abstractmethod can also be applied to static methods, class
# methods, and properties. You just need to make sure you apply it in the proper sequence
from abc import ABCMeta, abstractmethod
class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass
    @name.setter
    @abstractmethod
    def name(self, value):
        pass
    @classmethod
    @abstractmethod
    def method1(cls):
        pass
    @staticmethod
    @abstractmethod
    def method2():
        pass


#dicussion
import collections
# Check if x is a sequence
# if isinstance(x, collections.Sequence):

# Check if x is iterable
# if isinstance(x, collections.Iterable):

# Check if x has a size
# if isinstance(x, collections.Sized):

# Check if x is a mapping
# if isinstance(x, collections.Mapping):

# from decimal import Decimal
# import numbers
# x = Decimal('3.4')
# print(isinstance(x, numbers.Real)) #return False


from collections import Sequence, Mapping, Container
print(isinstance(dict(), Mapping))
print(isinstance([], Sequence))
print(isinstance(set(), Mapping))
print(all(isinstance(i(), Container) for i in [list, set, dict, tuple]))

