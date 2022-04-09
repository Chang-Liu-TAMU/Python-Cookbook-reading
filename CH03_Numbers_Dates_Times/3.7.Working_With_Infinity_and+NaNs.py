# @Time: 2022/4/9 14:45
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3.7.Working_With_Infinity_and+NaNs.py

a = float("inf")
b = float("-inf")
c = float("nan")
print(a)
print(b)
print(c)

import math
print(math.isinf(a))
print(math.isinf(-b))
print(math.isnan(c))

a = float("inf")
print(a)
print(a + 45)
print(a * 10)
print(10 / a)

print(a / a)
print(a + float("-inf"))


c = float("nan")
print(c + 23)
print(c / 2)
print(c * 2)
print(math.sqrt(c))


c = float("nan")
d = float("nan")
print(c == d)
print(c is d)

