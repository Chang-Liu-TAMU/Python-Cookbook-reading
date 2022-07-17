# import logging
# a = logging.getLogger("foo")
# b = logging.getLogger("bar")
# print(a is b)
# c = logging.getLogger("foo")
# print(a is c)

# The class in question
class Spam:
    def __init__(self, name):
        self.name = name
# Caching support
import weakref
_spam_cache = weakref.WeakValueDictionary()

def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s

# a = get_spam("foo")
# b = get_spam("bar")
# print(a is b)
# c = get_spam("foo")
# print(a is c)

########################################
# Note: This code doesn't quite work
import weakref
class Spam:
    _spam_cache = weakref.WeakValueDictionary()
    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
        return self

    def __init__(self, name):
        print('Initializing Spam')
        self.name = name
s = Spam("dave")
t = Spam("dave")
#alway initialize instances


'''
 A WeakValueDictionary instance only holds onto the referenced
items as long as they exist somewhere else. Otherwise, the dictionary keys disappear
when instances are no longer being used. Observe:
'''
a = get_spam("a")
b = get_spam("b")
c = get_spam("c")
print(list(_spam_cache))
del a
del c
print(list(_spam_cache))
del b
print(list(_spam_cache))

#############################################################
import weakref
class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s
    def clear(self):
        self._cache.clear()

class Spam:
    manager = CachedSpamManager()

    def __init__(self, name):
        self.name = name

def get_spam(name):
    return Spam.manager.get_spam(name)

"""
to avoid :
>>> a = Spam('foo')
>>> b = Spam('foo')
>>> a is b
False
"""

'''
Alternatively, if you want to give users a stronger hint that they shouldn’t instantiate
Spam instances directly, you can make __init__() raise an exception and use a class
method to make an alternate constructor like this:
'''

class Spam:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")
    # Alternate constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name

import weakref

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self, name):
        if name not in self._cache:
            s = Spam._new(name) # Modified creation
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

