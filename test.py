def f1():
    print("I am f1")


def f2():
    print("I am f2")


p1 = r"\d+"
p2 = r"\*"

print(vars()["f1"]())