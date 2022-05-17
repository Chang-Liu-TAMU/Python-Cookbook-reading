# @Time: 2022/5/7 19:49
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:7.6.Defining_anonymous_inline_functions.py

add = lambda x, y: x + y
print(add(2, 3))
print(add("hello", " world"))

#same as
def add(x, y):
    return x + y
print(add(2, 3))

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
names = sorted(names, key=lambda name: name.split()[-1].lower())
print(names)