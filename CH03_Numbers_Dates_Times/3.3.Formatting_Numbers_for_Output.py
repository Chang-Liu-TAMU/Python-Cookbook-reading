# @Time: 2022/4/8 15:08
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3.3.Formatting_Numbers_for_Output.py

x = 1234.56789
print(format(x, "0.2f"))

print(format(x, ">10.1f"))
print(format(x, "<10.1f"))
print(format(x, "^10.1f"))

print(format(x, ","))
print(format(x, "0,.1f"))

print(format(x, "e"))
print(format(x, "0.2E"))

print("the value is {:0,.2f}".format(x))

print(x)
print(format(x, "0.1f"))
print(format(-x, "0.1f"))


swap_separators = {ord("."): ",", ord(","): "."}
s = format(x, ",")
print(s)
print(s.translate(swap_separators))


print("%0.2f" % x)
print("%10.1f" % x)
print("%-10.1f" % x)

