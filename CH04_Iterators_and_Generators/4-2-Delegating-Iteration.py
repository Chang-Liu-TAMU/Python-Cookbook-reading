# @Time: 2022/4/12 20:24
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:4-2-Delegating-Iteration.py


class Node:
    '''
    Python’s iterator protocol requires __iter__() to return a special iterator object that
implements a __next__() method to carry out the actual iteration. If all you are doing
is iterating over the contents of another container, you don’t really need to worry about
the underlying details of how it works. All you need to do is to forward the iteration
request along.
    '''
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

if __name__ == "__main__":
    root = Node(0)
    root.add_child(Node(1))
    root.add_child(Node(2))
    for ch in root:
        print(ch)

