# @Time: 2022/4/8 15:15
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3.4.Working_with_Binary_Octal_Hexadecimal.py

x = 1234
bin_x = bin(x)
print(type(bin_x))
oct_x = oct(x)
print(oct_x)
print(hex(x))

print(format(x, "b"))
print(format(x, "o"))
print(format(x, "x"))

x = -1234
print(format(x, "b"))

print(format(2 ** 32 + x, "b"))

print(int("4d2", 16))
print(int("10011010010", 2))


import os
# os.chmod("script.py", 0755) #invalid
os.chmod("script.py", 0o755)