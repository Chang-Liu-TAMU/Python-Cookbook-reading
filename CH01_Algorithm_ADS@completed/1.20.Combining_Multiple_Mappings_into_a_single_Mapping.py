from collections import ChainMap

a = {"x": 1, "y": 3}
b = {"y": 2, "z": 4}
c = ChainMap(a, b)
# chainmap object takes multiple mappings and make them logically appear as one

print(c["x"])
print(c["y"])
print(c["z"])

print(c.keys())
print(c.values())

#mutations always afftect first argument of chainmap
c["z"] = 10
c["w"] = 40
del c["x"]
print(a)
print(b)

#
x = ChainMap()
x["y"] = 1
x = x.new_child()
print(type(x))
x["y"] = 2
x = x.new_child()
x["y"] = 3
# print(x)

y = x.parents
print(y)
print(x)

#
a = {"x": 1, "z": 3}
b = {"y": 2, "z": 4}
merged = dict(a)
merged.update(b)

merged_by_chain = ChainMap(a, b)
print(merged)
print(merged_by_chain)
a["i"] = 999
print(merged)
print(merged_by_chain)
#altering b will no longer affect merged

