# @Time: 2022/4/14 17:22
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:4.7.Taking_a_slice_of_iterator.py


def count(n):
    while True:
        yield n
        n += 1

c = count(0)
#can not use slice directly like c[1:6]

import itertools
for x in itertools.islice(c, 1, 10):
    print(x)

"""
Discussion:
    Iterators and generators can’t normally be sliced, because no information is known about
their length (and they don’t implement indexing). The result of islice() is an iterator
that produces the desired slice items, but it does this by consuming and discarding all
of the items up to the starting slice index. Further items are then produced by the islice
object until the ending index has been reached.
"""