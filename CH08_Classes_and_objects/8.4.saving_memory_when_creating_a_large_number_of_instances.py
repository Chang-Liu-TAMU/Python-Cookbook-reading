# @Time: 2022/5/15 8:49
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:8.4.saving_memory_when_creating_a_large_number_of_instances.py
class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

# obj = Date(2022, 5, 15)
# print(obj.__dir__())
'''
When you define __slots__, Python uses a much more compact internal representation
for instances. Instead of each instance consisting of a dictionary, instances are built
around a small fixed-sized array, much like a tuple or list.
'''

