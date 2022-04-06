# @Time: 2022/4/7 7:17
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3.1.Rounding_Numberical_Values.py

print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361, 3))

print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(1.55, 1))
print(round(2.55, 1))

a = 16227731
print(round(a, -1))
print(round(a, -3))

x = 1.23456
y = format(x, "0.2f")
print(y)
print(y == x)

a = 2.1
b = 4.2
c = a + b
print(c)

c = round(c, 2) # do not do this !!!


