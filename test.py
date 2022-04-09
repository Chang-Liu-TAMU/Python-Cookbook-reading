class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __iter__(self):
        return self.dfs()

    def dfs(self):
        yield self.val
        if self.left:
            yield from self.left.dfs()
        if self.right:
            yield from self.right.dfs()


root = Node(1)
child1 = Node(2)
child2 = Node(3)
root.left = child1
root.right = child2

i = iter(root)
print(i)
for j in i:
    print(j)
# def gen(node):
#     yield node.val
#     if node.left:
#         yield from gen(node.left)
#     if node.right:
#         yield from gen(node.right)
#
# g = gen(root)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))