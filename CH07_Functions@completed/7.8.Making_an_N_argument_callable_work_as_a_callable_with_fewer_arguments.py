# @Time: 2022/5/7 20:21
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:7.8.Making_an_N_argument_callable_work_as_a_callable_with_fewer_arguments.py

def spam(a, b, c, d):
    print(a, b, c, d)

from functools import partial
s1 = partial(spam, 1)
s1(2, 3, 4)

#wrong notice,
s2 = partial(spam, b=3)
# s2(2, 4, 5)
#correct
s2(2, c=4, d=5)





'''
partial() fixes the values for certain arguments and returns a new callable
as a result. This new callable accepts the still unassigned arguments, combines them
with the arguments given to partial(), and passes everything to the original function.
'''

# points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
# import math
# def distance(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     #Euclidean distance
#     return math.hypot(x2 - x1, y2 - y1)
#
# pt = (4, 3)
# points.sort(key=partial(distance,pt))




# def output_result(result, log=None):
#     if log is not None:
#         log.debug('Got: %r', result)
# # A sample function
# def add(x, y):
#     return x + y
#
#
# if __name__ == '__main__':
#     import logging
#     from multiprocessing import Pool
#     from functools import partial
#     logging.basicConfig(level=logging.DEBUG)
#     log = logging.getLogger('test')
#     p = Pool()
#     p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
#     p.close()
#     p.join()




from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT:' + line)


serv = TCPServer(('', 15000), EchoHandler)
serv.serve_forever()


#add some custom args in __init__
class EchoHandler(StreamRequestHandler):
 # ack is added keyword-only argument. *args, **kwargs are
 # any normal parameters supplied (which are passed on)
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)
    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)

from functools import partial
serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
serv.serve_forever()

#messy code
# points.sort(key=lambda p: distance(pt, p))
#
# p.apply_async(add, (3, 4), callback=lambda result: output_result(result,log))
#
# serv = TCPServer(('', 15000),
# lambda *args, **kwargs: EchoHandler(*args,
# ack=b'RECEIVED:',
# **kwargs))

