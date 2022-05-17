# @Time: 2022/5/8 20:48
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:7.10.carrying_extra_state_with_callback_functions.py

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', 'world'), callback=print_result)


#*******************************************
#carry extra information
class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ("hello", "world"), callback=r.handler)

#************************************************
#using a closure instead
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ("hello", "world"), callback=handler)

#**********************************************************
#using coroutine
def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

handler = make_handler()
next(handler)
apply_async(add, (2, 3), callback=handler)
apply_async(add, ("hello", "world"), callback=handler)


#**************************************
#using a object
class SequenceNo:
    def __init__(self):
        self.sequence = 0

def handler(result, seq):
    seq.sequence +=1
    print('[{}] Got: {}'.format(seq.sequence, result))

seq = SequenceNo()
from functools import partial
apply_async(add, (2, 3), callback=partial(handler, seq=seq))

#using a lambda func
apply_async(add, ("hello", "world"), callback=lambda r: handler(r, seq))


