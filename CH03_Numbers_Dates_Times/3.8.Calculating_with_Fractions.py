# @Time: 2022/4/9 14:49
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3.8.Calculating_with_Fractions.py

from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)
print(a)
print(b)
print(a + b)
print(a * b)
print(Fraction(8, 8))

c = a * b
print(c)
print(c.numerator)
print(c.denominator)

print(float(c))

print(c.limit_denominator(8))

x = 3.75
nu_de = x.as_integer_ratio()
print(nu_de, type(nu_de))
y = Fraction(*nu_de)
print(y)