from collections import Counter

some_sequence = [1, 2, 3, 2, 3, 3]
w = Counter(some_sequence)
top_three = w.most_common(3)
print(top_three)

#***********Counter Object is a dictionary , so you can use it as a normal dict*****************
new_data = [2, 3, 100]
w.update(new_data)
print(w)

"""
c1 = Counter(xx)
c2 = Counter(xx)

Combining counts: c1 + c2
subtract counts: c1 - c2
"""

