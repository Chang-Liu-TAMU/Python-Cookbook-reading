#example 01
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)

#example02
record = ("changliu", "chang_liu_tamu@163.com", "123", '456')
name, email, *others = record
print(record)
print(f"name is {name}")
print(f"email is {email}")
print(f"others is {others}")

#example 03
a = [1, 2, 3, 4, 5]
*heads, tail = a
s = sum(heads)
print(s)
print(a)

#example 04
records = [
    ("foo", 1, 2),
    ("bar", "hello"),
    ("foo", 3 ,4)
]


def do_foo(x, y):
    print("foo", x, y)


def do_bar(s):
    print("bar", s)


for name, *args in records:
    if name == "foo":
        do_foo(*args)
    else:
        do_bar(*args)

#example05
line = "I_am_head:fjaieo:faejiofa:fje:I_am_tail"
h, *middle, t = line.split(":")
print(h)
print(middle)
print(t)

#example06
l = ('changliu', 10, 2.0, (2022, 3, 1))
name, *_, (*_, day) = l
print(name)
print(day)

#example07
items = [1, 10, 2, 323, 13]
a, *b = items
print(a)
print(b)


#examples recursion sum
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print(sum(range(5)))

