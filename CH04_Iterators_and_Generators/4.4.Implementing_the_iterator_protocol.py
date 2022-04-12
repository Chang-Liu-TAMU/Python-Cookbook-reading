# @Time: 2022/4/12 20:50
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:4.4.Implementing_the_iterator_protocol.py

################ clean version #########################
# class Node:
#     def __init__(self, val):
#         self._value = val
#         self._children = []
#
#     def __repr__(self):
#         return "Node({!r})".format(self._value)
#
#     def add_child(self, node):
#         self._children.append(node)
#
#     def __iter__(self):
#         return iter(self._children)
#
#     def depth_first(self):
#         yield self
#         for c in self:
#             yield from c.depth_first()


############# some messy version ####################

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def add_child(self, node):
        self._children.append(node)


    def __iter__(self):
        return iter(self._children)

    # def iter(self):
    #     return iter(self._children)



    def depth_first(self):
        return DepthFirstIterator(self)

    # def __iter__(self):
    #     return DepthFirstIterator(self)


class DepthFirstIterator:
    '''
    DFS traversal
    '''
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._children_iter == None:
            self._children_iter = iter(self._node)
            # self._children_iter = self._node.iter()
            return self._node
        elif self._child_iter:
            try:
                following = next(self._child_iter)
                return following
            except StopIteration:
                self._child_iter = None
                return next(self)

        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)
            # return next(self._child_iter)

root = Node(0)
left = Node(1)
right = Node(2)
left.add_child(Node(3))
left.add_child(Node(4))
right.add_child(Node(5))
right.add_child(Node(6))
root.add_child(left)
root.add_child(right)

for i in root.depth_first():
    print(i)

# for i in root:
#     print(i)