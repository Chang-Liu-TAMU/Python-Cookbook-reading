# @Time: 2022/3/31 9:04
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:2.16.Reformatting_Text_to_a_fixed_number_of_columns.py


s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap

print(s)

#being wrapped
a = textwrap.fill(s, 70)
print(type(a))
print(a)

print(textwrap.fill(s, 40, initial_indent="   ", subsequent_indent="@@@"))

import os

print(os.get_terminal_size().columns) #does not work ???