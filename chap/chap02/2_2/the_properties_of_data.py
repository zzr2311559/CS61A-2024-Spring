def pair(x, y):
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get


def select(p, i):
    return p(i)

"""
>>> p = pair(20, 14)
>>> select(p, 0)
20
>>> select(p, 1)
14
"""
