# @Time: 2022/5/7 18:37
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:7.1.writing_funtions_that_accept_any_number_of_arguments.py

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

# print(avg(1, 2))
# print(avg(1, 2, 3, 4))

import html
# s = "<spam>"
# print(html.escape(s))

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
    name=name,
    attrs=attr_str,
    value=html.escape(value))
    return element

# a = make_element('item', 'Albatross', size='large', quantity=6)
# print(a)
#
# a = make_element('p', '<spam>')
# print(a)



def anyargs(*args, **kwargs):
    print(args) # A tuple
    print(kwargs) # A dict


#discussion
def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass

try:
    a(1, 2)
except Exception as e:
    print(e)
    a(1, 2, y=4)
    print("success")