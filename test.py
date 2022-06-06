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

class Obj:
    pass

a = Obj()
print(type(Obj.__name__))
