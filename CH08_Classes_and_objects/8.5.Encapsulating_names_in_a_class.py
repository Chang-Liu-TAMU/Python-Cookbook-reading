# @Time: 2022/5/15 8:54
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:8.5.Encapsulating_names_in_a_class.py

class A:
    def __init__(self):
        self._internal = 0 # An internal attribute
        self.public = 1 # A public attribute

    def public_method(self):
        '''
        A public method
        '''
        pass
    def _internal_method(self):
        pass

#two leading underscores

class B:
    def __init__(self):
        self.__private = 0
    def __private_method(self):
        pass
    def public_method(self):
        self.__private_method()


'''
 At this point, you might ask what purpose
such name mangling serves. The answer is inheritance—such attributes cannot be
overridden via inheritance. For example:
'''
class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1 # Does not override B.__private
    # Does not override B.__private_method()
    def __private_method(self):
        pass

##########################################

class X:
    def __init__(self):
        self.__private = "I am class X"

    def __private_method(self):
        pass

    def show_privates(self):
        ans = []
        for key, val in self.__dict__.items():
            if key.endswith("private"):
                ans.append(val)
        return ans

class Y(X):
    def __init__(self):
        super().__init__()
        self.__private = "I am class Y"

    def __private_method(self):
        pass

obj = X()
print(obj.show_privates())
obj = Y()
print(obj.show_privates())

#name conflict, using trailing underscore

lambda_ = 10

