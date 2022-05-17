# @Time: 2022/5/10 20:46
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:8.3.making_objects_support_the_context_management.py
#
# from socket import socket, AF_INET, SOCK_STREAM
#
# class LazyConnection:
#     def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
#         self.address = address
#         self.family = AF_INET
#         self.type = SOCK_STREAM
#         self.sock = None
#
#
#     def __enter__(self):
#         if self.sock is not None:
#             raise RuntimeError("Already connected")
#         self.sock = socket(self.family, self.type)
#         self.sock.connect(self.address)
#         return self.sock
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.sock.close()
#         self.sock = None

# from functools import partial
#
# conn = LazyConnection(("www.python.org", 80))
# with conn as s:
#     s.send(b"GET /index.html HTTP/1.0\r\n")
#     s.send(b"Host: www.python.org\r\n")
#     s.send(b"\r\n")
#     resp = b"".join(iter(partial(s.recv, 8192), b""))
#     print(resp)


#**************************************************
#multiple connections


from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.connections = []


    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connections.pop().close()


from functools import partial
conn = LazyConnection(("www.python.org", 80))
with conn as s1:
    with conn as s2:
        pass
