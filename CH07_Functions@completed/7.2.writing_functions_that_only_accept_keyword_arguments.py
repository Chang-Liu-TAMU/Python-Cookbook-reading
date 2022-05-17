# @Time: 2022/5/7 18:50
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:7.2.writing_functions_that_only_accept_keyword_arguments.py


def recv(maxsize, *, block):
    'Receives a message'
    pass
try:
    recv(1024, True) # TypeError
except Exception as e:
    print(e)
    recv(1024, block=True) # Ok
    print("ok")



def minimum(*values, clip=None):
    """
    This technique can also be used to specify keyword arguments for functions that accept
a varying number of positional arguments.
    """
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

minimum(1, 5, 2, -5, 10) # Returns -5
minimum(1, 5, 2, -5, 10, clip=0) # Returns 0


