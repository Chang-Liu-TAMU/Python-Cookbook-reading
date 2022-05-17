# @Time: 2022/4/7 7:04
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:2.20.Performing_text_operations_on_byte_strings.py


data = b"monster hunter"
a = data[:7]
print(a)

print(data.startswith(b"monster"))
print(data.endswith(b"hunter"))

print(data.split())

b = data.replace(b"monster", b"MONSTER")
print(data)
print(b)

data = bytearray(b"Hello World")
print(data[:5])

print(data.startswith(b"Hello"))
print(data.split())
print(data.replace(b"Hello", b"Hello Cruel"))

#can use re with byte pattern
data = b"FOO:BAR,SPAM"
import re
print(re.split(b"[:,]", data))

#indexing of byte strings produce integer not individual characters

a = "Hello World"
print(a[0])
print(a[1])

b = b"Hello World"
print(b[0])
print(b[1])

s = b"Hello World"
print(s)
# print(s.decode("ascii"))
# print(s.decode('utf-8'))
# x = s.decode("ascii")
# y = s.decode("utf-8")
# print(ord(x[0]))
# print(ord(y[0]))

#not byte string formatting available

print("{:10s} {:10d} {:10.2f}".format("ACME", 100, 701.2).encode("utf-8"))

with open("./txts/jalape\xf1o.txt", "w") as f:
    f.write("spicy")

import os
print(os.listdir("./txts"))

print(os.listdir(b"./txts"))