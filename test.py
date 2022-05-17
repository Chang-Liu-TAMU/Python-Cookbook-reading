from functools import partial


def f(n):
    return list(range(n))

p = partial(f, 6)
print(p)

i = iter(p, [0, 1, 2, 3, 4, 5])
print(list(i))