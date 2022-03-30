# @Time: 2022/3/30 9:23
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:2.14.Combining_and_concatenate_strings.py

parts = ["Is", "Houstion", "Not", "Houston"]
print("".join(parts))
print(",".join(parts))

a = "Is college station"
b = "not college station"
print(a + " " + b)

print("{} {}".format(a, b))
print("{1} {0}".format(a, b))

c = "Hello" "World"
print(c)

parts = "abc"
s = ""
#inefficient
for p in parts:
    s += p

data = ["ACME", 50, 91.2]
print(",".join(str(d) for d in data))


print(a + ":" + b + ":" + c)  # ugly
print(":".join([a, b, c]))  # still ugly

print(a, b, c, sep=":")   # better


chunk1, chunk2 = "c1", "c2"
f = open("file.txt")
f.write(chunk1 + chunk2)

# or
f.write(chunk1)
f.write(chunk2) # more efficient for larger strings


def sample():
    yield "Is"
    yield "Chicago"
    yield "Not"
    yield "Chicago?"


print("".join(sample()))

for p in sample():
    f.write(p)


#hybrid scheme
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield "".join(parts)
            parts = []
            size = 0
    yield "".join(parts)


for p in combine(sample(), 32787):
    f.write(p)


