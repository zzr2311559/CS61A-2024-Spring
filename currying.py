def curried_pow(x):
"""
>>> curried_pow(2)(3)
8
"""
    def h(y):
        return pow(x, y)
    return h

################################################################################

def map_to_range(start, end, f):
"""
>>> map_to_range(0, 10, curried_pow(2))
1
2
4
8
16
32
64
128
256
512
"""
    while start < end:
        print(f(start))
        start = start + 1
################################################################################

def curry2(f):
    """Return a curried version of the given two-argument function."""
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

def uncurry2(g):
    def f(x, y):
        return g(x)(y)
    return f

"""
>>> pow_curried = curry2(pow)
>>> pow_curried(2)(5)
32
>>> map_to_range(0, 10, pow_curried(2))
1
2
4
8
16
32
64
128
256
512
>>> uncurry2(pow_curried)(2,5)
32
"""
