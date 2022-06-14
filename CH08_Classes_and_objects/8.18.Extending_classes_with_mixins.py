#here are a set of mixin classes
'''
Add logging to get/set/delete operations for debugging.
'''
class LoggedMappingMixin:
    __slots__ = ()
    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)
    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)
    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)

class SetOnceMappingMixin:
    '''
    Only allow a key to be set once.
    '''
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    '''
    Restrict keys to strings only
    '''
    __slots__ = ()
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        return super().__setitem__(key, value)

'''
These classes, by themselves, are useless. In fact, if you instantiate any one of them, it
does nothing useful at all (other than generate exceptions).
'''
#example 01
class LoggedDict(LoggedMappingMixin, dict):
    pass

# d = LoggedDict()
# d['x'] = 23
# print(d["x"])
# del d['x']

#example 02
from collections import defaultdict
class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass

# d = SetOnceDefaultDict(list)
# d['x'].append(2)
# d['y'].append(3)
# d['x'].append(10)
# print(d)
# d['x'] = 23 error

#example03
from collections import OrderedDict
class StringOrderedDict(StringKeysMappingMixin,
                        SetOnceMappingMixin,
                        OrderedDict):
    pass

d = StringOrderedDict()
d['x'] = 23
# d[42] = 10

"""
In the example, you will notice that the mixins are combined with other existing classes
(e.g., dict, defaultdict, OrderedDict), and even one another. When combined, the
classes all work together to provide the desired functionality
"""

# from xmlrpc.server import SimpleXMLRPCServer
# from socketserver import ThreadingMixIn
# class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
#     pass


'''
It is also common to find mixins defined in large libraries and frameworks—again,
typically to enhance the functionality of existing classes with optional features in some
way.
'''

'''
If you are thinking about defining a mixin class that has an __init__() method and
instance variables, be aware that there is significant peril associated with the fact that
the class doesn’t know anything about the other classes it’s going to be mixed with. Thus,
any instance variables created would have to be named in a way that avoids name clashes.
'''

class RestrictKeysMixin:
    def __init__(self, *args, _restrict_key_type, **kwargs):
        self.__restrict_key_type = _restrict_key_type
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if not isinstance(key, self.__restrict_key_type):
            raise TypeError('Keys must be ' + str(self.__restrict_key_type))
        super().__setitem__(key, value)

class RDict(RestrictKeysMixin, dict):
    pass

d = RDict(_restrict_key_type=str)
e = RDict([('name','Dave'), ('n',37)], _restrict_key_type=str)
f = RDict(name='Dave', n=37, _restrict_key_type=float)
print(f)
# f[42] = 10 error

# class LoggedDict(LoggedMappingMixin, dict):
#     pass

'''
the use of super() in LoggedMappingMixin delegates to the next class over in the mul‐
tiple inheritance list. That is, a call such as super().__getitem__() in LoggedMapping
Mixin actually steps over and invokes dict.__getitem__(). Without this behavior, the
mixin class wouldn’t work at all.
'''

#alternative implementation
def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls

@LoggedMapping
class LoggedDict(dict):
    pass
