# @Time: 2022/4/14 17:16
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:4.6.Defining_Generator_functions_with_extra_states.py


from _collections import deque

class LineHisory:
    def __init__(self, lines, hislen=3):
        self.lines = lines
        self.history = deque(maxlen=hislen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open("some_file.txt") as f:
    lines = LineHisory(f, 3)
    for line in lines:
        if "python" in line:
            for lineno, line in lines.history:
                print("{}:{}".format(lineno, line), end="")


obj = LineHisory(3)
