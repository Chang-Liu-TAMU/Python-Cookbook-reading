# @Time: 2022/5/7 20:15
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:7.7.Capturing_variables_in_anonymous_functions.py


'''
The problem here is that the value of x used in the lambda expression is a free variable
that gets bound at runtime, not definition time. Thus, the value of x in the lambda
expressions is whatever the value of the x variable happens to be at the time of execution.
'''

x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

#what are the values of a(10) and b(10)
print(a(10))
print(b(10))
# all 30, use x at runtime



#x is bound at definition
# x = 10
# a = lambda y, x=x: x + y
# x = 20
# b = lambda y, x=x: x + y
# print(a(10))
# print(b(10))



# funcs = [lambda x: x+n for n in range(5)]
# for f in funcs:
#     print(f(0))


# funcs = [lambda x, n=n: x+n for n in range(5)]
# for f in funcs:
#     print(f(0))
