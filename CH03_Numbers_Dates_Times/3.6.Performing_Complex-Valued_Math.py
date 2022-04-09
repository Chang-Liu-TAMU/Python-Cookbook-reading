# @Time: 2022/4/9 14:40
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3.6.Performing_Complex-Valued_Math.py

a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)

print(a.real)
print(a.imag)

print(a + b)
print(a - b)
print(a / b)
print(abs(a))

import cmath, math
#cosine math

print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

print(cmath, cmath.sin(math.pi / 6))

import numpy as np

a = np.array([2+3j, 4+5j, 7-7j, 8+9j])
print(a)
print(a + 2)
print(np.sin(a))
print(np.sin(math.pi / 6))

import math
try:
    print(math.sqrt(-1))
except:
    print(cmath.sqrt(-1))



