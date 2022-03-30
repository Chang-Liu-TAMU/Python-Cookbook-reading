import re
simple_names = "rye,sakura,ken,luke,drug,lusiya"
print(simple_names.split(","))
complex_names = "ryu sakura; ken, luke,drug,      lusiya"
print(re.split(r"[;,\s]\s*", complex_names))

#with group
print(re.split(r"(;|,|\s)\s*", complex_names))

#*************************************************
split_names = re.split(r"(;|,|\s)\s*", complex_names)
values = split_names[::2]
delimiters = split_names[1::2] + [""]
print(''.join(v + d for v, d in zip(values, delimiters)))

#*************************************************
print(re.split(r"(?:;|,|\s)\s*", complex_names))

