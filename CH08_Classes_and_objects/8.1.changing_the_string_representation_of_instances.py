# @Time: 2022/5/10 18:43
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:8.1.changing_the_string_representation_of_instances.py

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    # def __repr__(self):
    #     return "Pair({0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return "({0.x!s}, {0.y!s})".format(self)

    def __repr__(self):
        return "Pair(%r, %r)" % (self.x, self.y)


"""
The __repr__() method returns the code representation of an instance, and is usually
the text you would type to re-create the instance. The built-in repr() function returns
this text, as does the interactive interpreter when inspecting values. The __str__()
method converts the instance to a string, and is the output produced by the str() and
print() functions.
"""

'''
The implementation of this recipe also shows how different string representations may
be used during formatting. Specifically, the special !r formatting code indicates that the
output of __repr__() should be used instead of __str__(), the default.
'''


p = Pair(3, 4)
print(p)
print("p is {!r}".format(p))

'''
It is standard practice for the output of __repr__() to produce text such that
eval(repr(x)) == x. If this is not possible or desired, then it is common to create a
useful textual representation enclosed in < and > instead. For example:
'''

# f = open("file.dat", "w")
# print(f)



