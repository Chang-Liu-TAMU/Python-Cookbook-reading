# @Time: 2022/4/27 16:14
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:4-10-iterating-over-the-index-value-pairs-of-a-squence.py

my_list = ["a", "b", "c"]
for idx, val in enumerate(my_list):
    print(idx, val)
print("\n")
for idx, val in enumerate(my_list, 1):
    print(idx, val)

def parse_data(filename):
    with open(filename, "rt") as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[0])
                # ...
            except ValueError as e:
                print("Line {}: Parse error: {}".format(lineno, e))
# parse_data("4-10.txt")

from collections import defaultdict
word_summary = defaultdict(list)

with open("4-10.txt", "r") as f:
    # with "w", we overwrite
    lines = f.readlines()

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)
print(word_summary)

#this tip helps to get rid of messy code
lineno = 1
for line in open("4-10.txt"):
    print(f"{lineno}: {line}", end="")
    lineno += 1

data = [(1, 2), (3, 4), (5, 6), (7, 8)]
for n, (x, y) in enumerate(data):
    pass
# correct

for n, x, y in enumerate(data):
    pass
# wrong