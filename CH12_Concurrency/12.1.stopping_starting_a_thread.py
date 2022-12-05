# @Time: 2022/4/29 7:06
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:12.1.stopping_starting_a_thread.py

import time
from threading import Thread

# def countdown(n):
#     while n > 0:
#         print("T-minus: ", n)
#         n -= 1
#         time.sleep(5)
#
# t = Thread(target=countdown, args=(2, ))
# t.start()
# print("I am finished")
# if t.is_alive():
#     print("still running")
# else:
#     print("completed")

'''
t.join() to block
'''

'''
The interpreter remains running until all threads terminate. For long-running threads
or background tasks that run forever, you should consider making the thread daemonic.
For example:

    t = Thread(target=countdown, args=(10,), daemon=True) 
    t.start()
'''

'''
Daemonic threads can’t be joined. However, they are destroyed automatically when the
main thread terminates.
'''

class CountdownTask:
    def __init__(self):
        self._running = True


    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print("T-minus: ", n)
            n -= 1
            time.sleep(3)

# c = CountdownTask()
# t = Thread(target=c.run, args=(3,))
# t.start()
# time.sleep(3)
# c.terminate()
# t.join() # wait for actual termination

import socket
from socket import socket

class IOTask:
    def terminate(self):
        self._running = False

    def run(self, sock: socket):
        sock.settimeout(5)
        while self._running:
            try:
                data = sock.recv(1892)
                break
            except socket.timeout:
                continue
        return

'''
note:
    Due to a global interpreter lock (GIL), Python threads are restricted to an execution
model that only allows one thread to execute in the interpreter at any given time. For
this reason, Python threads should generally not be used for computationally intensive
tasks where you are trying to achieve parallelism on multiple CPUs. They are much
better suited for I/O handling and handling concurrent execution in code that performs
blocking operations (e.g., waiting for I/O, waiting for results from a database, etc.)
'''

class Countdown(Thread):
    def __init__(self, name, n, **kwargs):
        super().__init__(**kwargs)
        self.n = n
        self.name = name
    def run(self):
        # super().run()
        # run method here overrides original run
        while self.n > 0:
            print("I am ", self.n)
            self.n -= 1
            time.sleep(3)

    def __str__(self):
        return f"thread-<name:{self.name}>"

def f(n):
    for i in range(n):
        print(i, end=" ")

# c = Countdown("my_thread", 3)
# c.start()
# print(c)

# c = Countdown("my_thread", 3, target=f, args=(3,))
# c.start()

import multiprocessing
if __name__ == "__main__":
    c = CountdownTask()
    p = multiprocessing.Process(target=c.run, args=(3, ))
    p.start()