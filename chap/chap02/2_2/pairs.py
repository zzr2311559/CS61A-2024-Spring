pair = [10, 20]
"""
>>> pair
[10, 20]
"""
x, y = pair
"""
>>> x
10
>>> y
20
"""

pair[0]
"""
>>> pair[0]
10
"""

pair[1]
"""
>>> pair[1]
20
"""

from operator import  getitem
getitem(pair, 0)
"""
>>> getitem(pair, 0)
10
"""

getitem(pair, 1)
"""
>>> getitem(pair, 1)
20
"""
