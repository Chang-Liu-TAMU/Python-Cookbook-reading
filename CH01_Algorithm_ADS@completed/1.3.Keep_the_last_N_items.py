from collections import deque

def search(lines, pattern, history=5):
    previous = deque(maxlen=history)
    for line in lines:
        if pattern:
            pass
        else:
            yield line, previous
        previous.append(line)

if __name__ == "__main__":
    with open("1-3-test.txt") as f:
        for line, previous in search(f, None):
            for pline in previous:
                print(pline.strip())
            print("now: ", line.strip())
            print("-" * 20)

    q = deque()
    q.append(1)
    q.appendleft(2)
    q.pop()
    q.popleft()
