import weakref
class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []
    def __repr__(self):
        return 'Node({!r:})'.format(self.value)
    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return self._parent() #dereference weakref
        # return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

# root = Node(("parent"))
# c1 = Node("child")
# root.add_child(c1)
# print(c1.parent)
# del root
# print(c1.parent)


#########################################
# Class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('Data.__del__')
# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
# a = Data()
# del a
# a = Node()
# del a
# a = Node()
# # b = Node()
# a.add_child(Node())
# del a
# print("nothing happens")
# import gc
# gc.collect() #forced garbage collection
# print(b)

"""
del something
just reduces the reference counts by 1
if 0, the __del__ method of the object will be invoked
"""

#############################################################
# Class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('Data.__del__')
# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []
# NEVER DEFINE LIKE THIS.
# Only here to illustrate pathological behavior
    def __del__(self):
        del self.data
        del self.parent
        del self.children
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

# a = Node()
# a.add_child(Node())
# del a
#
# import gc
# gc.collect() #works
# # print("hello ")


import weakref

a = Node()
a_ref = weakref.ref(a)
print(a_ref)
del a
print(a_ref())