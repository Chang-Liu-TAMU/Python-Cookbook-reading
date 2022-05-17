import re
num = re.compile("\d+")
s1 = "123"  # ascii digits
x, y, z = "\u0661", "\u0662", "\u0663"
print(x, y, z)
s2 = x + y + z  # arabic digits
print(num.findall(s1))  # matched
print(num.findall(s2))  # matched

# match all characters in a few different arabic code pages
pattern = '[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+'
print(pattern)
arabic = re.compile(pattern)

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = "stra\u00dfe"
print(s)
print(pat.findall(s))

print(s.upper())



