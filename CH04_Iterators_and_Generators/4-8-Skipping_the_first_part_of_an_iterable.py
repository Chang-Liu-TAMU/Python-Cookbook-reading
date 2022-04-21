# @Time: 2022/4/21 14:57
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:4-8-Skipping_the_first_part_of_an_iterable.py

with open("./4-1-passwd") as f:
    for line in f:
        print(line, end="")

print("\n")

from itertools import dropwhile
with open("./4-1-passwd") as f:
    for line in dropwhile(lambda line: line.startswith("#"), f):
        print(line, end="")

print("\n")

from itertools import islice
items = ["a", "b", "c", 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

#ugly codes

with open("./4-1-passwd") as f:
    while True:
        line = next(f, "")
        if not line.startswith("#"):
            break

    while line:
        print(line, end="")
        line = next(f, None)
print("\n")

#following filters all lines
with open("./4-1-passwd") as f:
    lines = (line for line in f if not line.startswith("#"))
    for line in lines:
        print(line, end="")
