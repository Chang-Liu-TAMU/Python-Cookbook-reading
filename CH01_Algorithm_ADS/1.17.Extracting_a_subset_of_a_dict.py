#you wanna make a dictionary a subset of another dictionary

prices = {"key1": 100, "key2": 200}

p1 = {key: val for key, val in prices.items() if val > 100}
print(p1)

names = {"key1"}
p2 = {key: val for key, val in prices.items() if key in names}
print(p2)
#comprehension is faster

names = {"key2"}
p3 = {key: prices[key] for key in prices.keys() & names}
print(p3)