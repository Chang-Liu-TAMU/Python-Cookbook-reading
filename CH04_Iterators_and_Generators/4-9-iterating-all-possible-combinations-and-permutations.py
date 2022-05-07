# @Time: 2022/4/27 11:55
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:4-9-iterating-all-possible-combinations-and-permutations.py

from itertools import permutations

items = ["obj1", 'obj2', "obj3"]
for p in permutations(items):
    print(p)
    break

print("\n")
for p in permutations(items, 2):
    print(p)
    break

from itertools import combinations
#order is not considers, and chosen item is removed
for c in combinations(items, 3):
    print(c)
for c in combinations(items, 2):
    print(c)

from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 2):
    print(c)