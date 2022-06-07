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
    def show(self, n):
        print(f"hello{n}")

a = Obj()
x = getattr(a, "show")
print(x)
x(3)