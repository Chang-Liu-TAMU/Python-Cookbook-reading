# @Time: 2022/3/29 11:31
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:2.13.Aligning_text_strings.py

#ljust, rjust, center

text = "Hello World"
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

print(text.rjust(20, "="))
print(text.center(20, "*"))

print(format(text, ">20"))
print(format(text, "<20"))
print(format(text, "^20"))

print(format(text, "=>20s"))
print(format(text, "=<20s"))
print(format(text, "*^20s"))

print("{:$>10s} {:-^10s}".format("Hello", "World"))

x = 1.23242
print(format(x, ">10"))
print(format(x, "^10.2f"))
print("ans is {:.2f}".format(x))

print("%-20s" % text)
print("%20s" % text)
#format method is better
