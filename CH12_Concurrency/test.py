
def f():
    n = 0
    def g():
        nonlocal n
        n += 1
        print(n)
        if n > 5:
            return 0
        return n
    return g

i = iter(f(), 0)
print(list(i))
