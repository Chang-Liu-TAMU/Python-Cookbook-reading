p = (4, 5)
x, y = p
print(f"p is {p}")
print("x, y = p")
print(f"x = {x}, y = {y}")

data = ["liuchang", 50, 100.1, (2022, 3, 1)]
name, share, price, date = data
print("name, share, price, date = data")
print(f"name = {name}")
print(f"share = {share}")

_, _, _, (a, b, c) = data
print(a, b, c)