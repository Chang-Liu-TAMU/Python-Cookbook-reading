# @Time: 2022/5/10 19:12
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:8.2.customize_string_formatting.py


_formats = {
 'ymd' : '{d.year}-{d.month}-{d.day}',
 'mdy' : '{d.month}/{d.day}/{d.year}',
 'dmy' : '{d.day}/{d.month}/{d.year}'
 }

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

# d = Date(2022, 5, 10)
# print(format(d))
# print(format(d, "mdy"))
# print("The date is {:ymd}".format(d))
# print("The date is {:mdy}".format(d))

'''
The __format__() method provides a hook into Python’s string formatting function‐
ality. It’s important to emphasize that the interpretation of format codes is entirely up
to the class itself. T
'''

from datetime import date

d = date(2022, 5, 10)
print(format(d, "%A %B %d, %Y"))
print("The end is {:%d %b %Y}. Goodbye".format(d))



