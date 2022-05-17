# list comprehension
import math
mylist = [1, 2, -10, 9, 80, -379]
positives = [x for x in mylist if x > 0]
# positives = [math.sqrt(x) for x in mylist if x > 0]
negatives = [x for x in mylist if x < 0]
# negatives = [x if x < 0 else 0 for x in mylist]

# if mememory is a concern
pos = (x for x in mylist if x > 0)
print(pos)
print(list(pos))

# if more complex filtering logic needs to be applied
values = ["1", "5", "&", "10", "#"]
def is_int(obj):
    try:
        x = int(obj)
        return True
    except ValueError:
        return False

f = filter(is_int, values)
print(f)
print(list(f))
# print(list(f)) #consumed

#
from itertools import compress
days = ['Mon', "Tu", "Wed", "Th", "Fri", "Sa", "Sun"]
weathers = [1, 0, 0, 1, 0, 1, 1]
gooddays = [x == 1 for x in weathers]

c = compress(days, gooddays)
print(c)
print(list(c))
