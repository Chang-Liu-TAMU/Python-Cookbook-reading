# @Time: 2022/4/13 21:26
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3.11.Picking_things_at_random.py

import random

objs = [1, 2, 3, 4, 5]
print(random.choice(objs))

print(random.sample(objs, 2))

random.shuffle(objs)
print(objs)
random.shuffle(objs)
print(objs)

print(random.randint(0, 10))

print(random.random()) # 0 - 1

print(random.getrandbits(100))

# random.seed()
# random.seed(12345)
# random.seed(b"bytedata")