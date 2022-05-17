text = "some text"
text == "some text"
text.startswith("some thing")
text.endswith("some thing")
print(text.find(("text")))
print(text.find(("abd"))) #-1 find nothing

text1 = "3/17/2022"
text2 = "March 17, 2022"
import re
print(re.match(r"\d+/\d+/\d+", text1))

p = re.compile(r"\d+/\d+/\d+")
print(p.match(text1)) #match only checks the begining of a string
print(p.match(text2))

t = "Today is 3/17/2022, yesterday is 3/16/2022"
a = p.match(t)
print(a)
b = p.findall(t)
print(b)
print(type(b[0]))

p = re.compile(r"(\d+)/(\d+)/(\d+)")

m = p.match("11/11/1121")
print(m)

print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))

print(m.groups())

for month, day, year in p.findall(t):
    print(f"{month}-{day}-{year}")

for item in p.finditer(t):
    month, day, year = item.groups()
    print(f"{month}-{day}-{year}")



t = "10/19/2321"
print(p.match(t))
t = "10/19/2321abd"
print(p.match(t).group())
p = re.compile(r"(\d+)/(\d+)/(\d+)$")
print(p.match(t)) #???

print(re.findall(r"(\d+)/(\d+)/(\d+)", t))

