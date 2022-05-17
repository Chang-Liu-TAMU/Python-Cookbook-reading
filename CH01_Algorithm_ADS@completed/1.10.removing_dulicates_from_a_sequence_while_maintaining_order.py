def dedupe(items, key=None):
    '''
    :param items: items with dups to be handled
    :param key: a func which maps item to hashable (if needed)
    :return: items without dups
    '''
    seen = set()
    for item in items:
        val = item if not key else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [1, 5, 3, 4, 10, 4, 3, 2, 1, 3]
print(a)
print(list(dedupe(a)))

b = [[1, 2], [3, 4], [1, 2]]
print(b)
print(list(dedupe(b, key=lambda x: str(x[0]) + str(x[1]))))

#with dictionary
#key = lambda x: x["x"]

# with open("./somefile.txt", "r") as f:
#     for line in dedupe(f):
#         pass

