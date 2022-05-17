a = {"x": 1,
     "y": 2,
     "z": 3
}

b = {
    "w": 10,
    "x": 11,
    "y": 2
}

# find keys in common
print(type(a.keys() & b.keys()))

#find uniques keys in a
print(a.keys() - b.keys())

#find (key,val) pairs in common
print(a.items() & b.items())

