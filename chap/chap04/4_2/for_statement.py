counts = [1, 2, 3]
for item in counts:
    print(item)


"""
With our knowledge of iterators, we can implement the execution rule of a for
statement in terms of while, assignment, and try statements.
"""

items = counts.__iter__()

try:
    while True:
        item = items.__next__()
        print(item)
except StopIteration:
    pass

"""
Above, the iterator returned by invoking the __iter__ method of counts is bound
to a name items so that it can be queried for each element in turn. The handling
clause for the StopIteration exception does nothing, but handling the exception
provides a control mechanism for exiting the while loop.
"""


"""
>>> t = iter([4, 3, 2, 1])
>>> for e in t:
...     print(e)
4
3
2
1
>>> for e in t:
...     print(e)
"""
