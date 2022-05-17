# @Time: 2022/3/30 9:47
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:2.15.Interpolating_Variables_in_strings.py

if False:
    s = "{name} has {n} messages"
    # print(s.format("Guido", 37)) # must be key args
    print(s.format(name="Guido", n=38))

if False:
    name = "Guido"
    n = 37
    s = "{name} has {n} messages"
    v = vars()
    print(v, type(v))
    print(s.format_map(v))


class SafeSub(dict):
    def __missing__(self, key):
        return "{" + key + "}"
        # return "{missing key}"

if False:
    s = "{name} has {n} messages"
    class Info:
        def __init__(self, name, n):
            self.name = name
            self.n = n

    a = Info("Guido", 37)
    print(vars(a))
    print(s.format_map(vars(a)))


    name = "changliu"
    print(s.format_map(SafeSub(vars())))

if False:
    import sys

    def sub(text: str):
        #f_locals returns copy of variables of last frame, no risk of modifying them
        return text.format_map(SafeSub(sys._getframe(1).f_locals))

    name = "Guido"
    n = 37
    print(sub("Hello {name}"))

    print(sub("U have {n} messages"))

    print(sub("your favoriate color is {color}"))

#following methods are not preferable
# name = "Guido"
# n = 37
# print("%(name) has %(n) messages." % vars()) #seems to be deprecated


import string
name = "Guido"
n = 37
t = string.Template("$name has $n messages")
print(t.substitute(vars()))

