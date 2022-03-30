from operator import itemgetter
from itertools import groupby

rows = [
    {"name": "ryu", "gender": "male"},
    {"name": "sakura", "gender": "female"},
    {"name": "luke", "gender": "male"},
    {"name": "lusiya", "gender": "female"}
]

key = itemgetter("gender")
rows.sort(key=key)
for gender, chars in groupby(rows, key=key):
    print(gender)
    for c in chars:
        print("    ", c)

print("*" * 50)
#alternative
from collections import defaultdict
d = defaultdict(list)
for item in rows:
    d[item["gender"]].append(item)

for key, vals in d.items():
    print(key)
    for v in vals:
        print("    ", v)

