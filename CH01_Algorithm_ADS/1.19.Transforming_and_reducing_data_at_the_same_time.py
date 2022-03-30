num = [1, 2, 3, 4, 5]
s = sum(x ** 2 for x in num)
# s = sum([x ** 2 for x in num]) #waste memory
print(s)

# ***************************************
import os
files = os.listdir(".")
if any(name.endswith(".py") for name in files):
    print("There be python")
else:
    print("no python")

# ***************************************

s = (1, 2, 3)
print(','.join(str(x) for x in s))

# ***************************************

games = [{"price": 100}, {"price": 200}]
min_price = min(item["price"] for item in games)
min_item_with_price = min(games, key=lambda item: item["price"])
print(min_price)
print(min_item_with_price)