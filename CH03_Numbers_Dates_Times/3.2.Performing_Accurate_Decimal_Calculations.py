# @Time: 2022/4/8 15:03
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3.2.Performing_Accurate_Decimal_Calculations.py

a = 4.2
b = 2.1
c = a + b
print(c)

print((a + b) == 6.3)


from decimal import Decimal
a = Decimal("4.2")
b = Decimal("2.1")
c = a + b
print(c)
print(c == Decimal("6.3"))


from decimal import localcontext
a = Decimal("1.3")
b = Decimal("1.7")
print(a / b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)


nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))

import math
print(math.fsum(nums))

