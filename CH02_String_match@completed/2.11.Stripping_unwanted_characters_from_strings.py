# @Time: 2022/3/28 9:06
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:2.11.Stripping_unwanted_characters_from_strings.py

#whitespace stripping

s = "   hello world  \n"
print(s.strip())
print(s.lstrip())
print(s.rstrip())

#specify characters to strip
t = "----hello====="
print(t.lstrip("-"))
print(t.rstrip("="))

#note: strip methods does not apply to text in middle
s = "  hello   world   \n"
s = s.strip()
print(s)

#using replace or other
print(s.replace(" ", ""))
import re
print(re.sub("\s+", " ", s))

#reading text
with open("xx.txt") as f:
    lines = (line.strip() for line in f)
    for line in lines:
        pass


