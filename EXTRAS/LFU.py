# @Time: 2022/4/13 11:29
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:LFU.py


class Node:
    def __init__(self, key=None, val=None):
        self.val = val
        self.key = key
        self.f = 1
        self.left = None
        self.right = None


class DLL:
    def __init__(self):
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.left = self.tail
        self.tail.right = self.head

    def remove_node(self, node):
        node.left.right = node.right
        node.right.left = node.left
        self.size -= 1

    def add_head(self, node):
        self.head.left.right = node
        node.left = self.head.left
        self.head.left = node
        node.right = self.head
        self.size += 1

    def remove_tail(self):
        tail = self.tail.right
        self.remove_node(tail)
        return tail


class LFUCache:
    '''
    referring to discuss board,
    thanks, stranger
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq_map = {}
        self.min_freq = None

    def get(self, key: object) -> object:
        # print(self.cache)
        # print(self.freq_map)
        if key not in self.cache:
            return -1
        val = self.cache[key].val
        self.update(key, val)
        return val

    def put(self, key: int, value: object) -> None:
        # print(self.freq_map)
        if self.capacity == 0:
            return
        if key in self.cache:
            self.update(key, value)
        else:
            if len(self.cache) == self.capacity:
                removed = self.freq_map[self.min_freq].remove_tail()
                del self.cache[removed.key]
            self.min_freq = 1
            new = Node(key, value)
            if 1 not in self.freq_map:
                self.freq_map[1] = DLL()
            self.cache[key] = new
            self.freq_map[1].add_head(new)

    def update(self, key, val):
        ptr = self.cache[key]
        ptr.val = val
        f = ptr.f
        ptr.f += 1
        if f + 1 not in self.freq_map:
            self.freq_map[f + 1] = DLL()
        self.freq_map[f].remove_node(ptr)
        self.freq_map[f + 1].add_head(ptr)
        if self.freq_map[f].size == 0 and self.min_freq == f:
            self.min_freq += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class MyObj:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

if __name__ == "__main__":
    x, y, z = MyObj("x"), MyObj("y"), MyObj("z")
    assert  x is not y and y is not z
    lfu = LFUCache(2)
    print(lfu.get(1))
    lfu.put(1, x)
    lfu.put(2, y)
    print(lfu.get(1))
    print(lfu.get(2))
    lfu.put(3, z)
    print(lfu.get(1))
    print(lfu.get(3))

