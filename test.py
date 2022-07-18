# class A:
#     pass
#
# class B(A):
#     def f(self):
#         a = super()
#         b = super(B, B)
#         print(a)
#         print(b)
#         print(b is A)
#
#
# b = B()
# b.f()

# class Obj:
#     def show(self, n):
#         print(f"hello{n}")
#
# a = Obj()
# x = getattr(a, "show")
# print(x)
# x(3)
#
# class A:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def show(self):
#         print("A")
#
#     def state(self):
#         self.__class__ = B
#
# class B:
#     def __init__(self, b):
#         self.b = b
#
#     def state(self):
#         self.__class__ = A
#
#     def show(self):
#         print("B")
#
# b = B(100)
# print(b)
# b.state()
# print(b)
# print(b.b)
# b.show()
# b.state()
# b.show()

# def gen():
#     yield (yield 1) + (yield 2)
#
# g = gen()
# x = g.send(None)
# y = g.send(10)
# z = g.send(20)
# print(x, y, z)

# print(type(type))
# print(isinstance(type, type))
# print(isinstance(type, object))
# # print(isinstance(object, type))
#
# from inspect import signature
#
# def f(x:int , y: int):
#     pass
#
# sig = signature(f)
# d = sig.parameter

