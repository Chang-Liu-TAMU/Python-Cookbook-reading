import heapq

#question: why there is an extra index in the tuple
#answer: if there is no index, items can be compared if priorities are equal, which may throw
#errors. Since all indexes are strictly increasing, only priorities will be compared


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def __bool__(self):
        return self._queue != []


class Character:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Character({!s})".format(self.name)


if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Character("Ryu"), 6)
    q.push(Character("Sakura"), 4)
    q.push(Character("Luke"), 2)
    q.push(Character("Ken"), 3)
    while q:
        print(q.pop())
