# @Time: 2022/5/7 19:00
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:7.5.defining_functions_with_default_arguments.py

#
# def spam(a, b=42):
#     print(a, b)
# spam(1) # Ok. a=1, b=42
# spam(1, 2) # Ok. a=1, b=2



# def spam(a, b=None):
#     if b is None:
#         b = []
#     return a, b

#using this idiom
# _no_value = object()
# def spam(a, b=_no_value):
#     if b is _no_value:
#         print('No b value supplied')
#
#
# spam(1)
# spam(1, 2)
# spam(1, None)


# x = 42
# def spam(a, b=x):
#     print(a, b)
#
# spam(1)
# x = 23
# spam(1)

# def spam(a, b=[]):
#     print(b)
#     return b
# x = spam(1)
# x.append(100)
# x.append(200)
# print(x)
# spam(1)

def spam(a, b=None):
    if not b:
        print("b not provided")

#besides None, many objects evaluate to False
spam(1)
spam(1, [])
spam(1, "")
spam(1, 0)