# @Time: 2022/5/10 8:18
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:7.12.Accessing_variables_defined_inside_a_closure.py

def sample():
    n = 0
    def func():
        print("n =", n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n

    return func

# f = sample()
# f()
# f.set_n(10)
# print(f.get_n())


#****************************************
#slight extension to this recipe

import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))

    def __len__(self):
        return self.__dict__["__len__"]()

    def __str__(self):
        return self.__dict__["__str__"]()


def Stack1():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)


    def __str__():
        return " ".join(str(x) for x in items) if items else "Empty"

    return ClosureInstance()

# s = Stack()
# print(s)
# s.push(10)
# s.push(20)
# s.push("hello")
# print(s)
# print(len(s))


class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


from timeit import timeit
s = Stack1()
t1 = "s.push(1);s.pop()"
t2 = "from __main__ import s"
print(timeit(t1, t2))

s = Stack2()
print(timeit(t1, t2))

