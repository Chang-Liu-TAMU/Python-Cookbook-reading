# @Time: 2022/4/13 21:33
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:4.5.Iterating_in_reverse.py

#generator is not reversible
a = [1, 2, 3, 4]
for x in reversed(a):
    print(a)

'''
Reversed iteration only works if the object in question has a size that can be determined
or if the object implements a __reversed__() special method.
'''

# f = open("somefile.txt")
# for line in reversed(list(f)):
#     print(line, end="")


class Countdown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        print("\nnow starting to count down")
        i = self.n
        while i > 0:
            yield i
            i -= 1

    def __reversed__(self):
        print("\nnow starting to count")
        i = 1
        while i <= self.n:
            yield i
            i += 1

c = Countdown(6)
for i in iter(c):
    print(i, end=" ")

for i in reversed(c):
    print(i, end=" ")

