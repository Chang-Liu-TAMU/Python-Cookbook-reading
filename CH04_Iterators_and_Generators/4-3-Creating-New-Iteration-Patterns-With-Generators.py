# @Time: 2022/4/12 20:29
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:4-3-Creating-New-Iteration-Patterns-With-Generators.py


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

# for n in frange(1, 5, 0.6):
#     print(n)


def countdown(n):
    print(f"starting counting from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Done")

g = countdown(3)
print(next(g))
print(next(g))
print(next(g))
#stuck in yield point
# print(next(g))

print("*" * 30)
i = iter([])
print(next(i))