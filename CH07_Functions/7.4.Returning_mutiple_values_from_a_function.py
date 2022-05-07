# @Time: 2022/5/7 18:58
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:7.4.Returning_mutiple_values_from_a_function.py

def myfunc():
    return 1, 2, 3

# a, b, c = myfunc()
# print(a, b, c)

#all tuples, with or without parentheses
a = (1, 2)
print(a, type(a))
b = 1, 2
print(b, type(b))


#return tuple
x = myfunc()
print(x, type(x))
