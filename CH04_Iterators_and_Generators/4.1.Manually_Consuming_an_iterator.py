# @Time: 2022/4/12 20:15
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:4.1.Manually_Consuming_an_iterator.py

with open("./4-1-passwd") as f:
    try:
        while True:
            line = next(f)
            print(line, end="")
    except StopIteration as e:
        print(e)


with open("./4-1-passwd") as f:
    while True:
        line = next(f, None) #customize your terminating signal
        if line == None:
            break
        print(line, end="")


items = [1, 2, 3]
it = iter(items)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))





