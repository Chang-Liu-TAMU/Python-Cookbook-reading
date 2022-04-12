# @Time: 2022/4/12 21:26
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3.9.Calculating_with_large_numerical_arrays.py


x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print(x * 2)


import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(a * 2)
print(a + 10)

def f(x):
    return x ** 2 + 3 * x + 8

print(f(a))

#universal functions
# np.sqrt
# np.cos

grid = np.zeros(shape=(10000, 10000), dtype=float)
print(grid)

a = np.arange(9).reshape((3, 3))
print(a)
print(a[0])
print(a[:, 0])
s = slice(1, 3)
print(a[s, s])

b = a + [100, 101, 102]
print(b)
print(a)
# a += [100, 101, 102]
# print(a)

print(np.where(a < 10, a, 10))
#if a < 10, pick from a eise make it 10
w = np.where(a < 6) # returns tuple
v = np.asarray(a < 6).nonzero()
#w is shorthand for v
print(w)
print(v) # same thing