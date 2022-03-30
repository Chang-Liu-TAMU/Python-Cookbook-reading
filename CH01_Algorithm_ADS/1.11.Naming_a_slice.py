a = list(range(10))
slice1 = slice(0, 3)
slice2 = slice(4, 8)
print(a[slice1])
print(a[slice2])

a[slice2] = ["@", "#", "$", "%"]
print(a)

del a[slice1]
print(a)

print(f"slice start: {slice1.start}")
print(f"slice stop: {slice1.stop}")
print(f"slice step: {slice1.step}")

c = slice(0, 100, 3)
s = "0as0ef0df0vd0ef0d"
for i in range(*c.indices(len(s))):
    print(s[i], end='')

