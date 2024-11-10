def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    """
    >>> reduce(mul, [2, 4, 8], 1)
    64
    """
    reduced = initial
    for x in s:
        reduced = reduced_fn(reduced, x)
    return reduced

def divisior_of(n):
    """
    >>> divisior_of(12)
    [1, 2, 3, 4, 6]
    """
    divides_n = lambda x: n % x == 0
    return [1] + keep_if

from operater import add

def sum_of_divisors(n):
    return reduce(add, divides_n(n), 0)

def perfect(n):
    return sum_of_divisors(n) == n

"""
>>> keep_if(perfect, range(1, 1000))
[1, 6, 28, 496]
"""

apply_to_all = lambda map_fn, s: list(map(map_fn, s))
keep_if = lambda filter_fn, s: list(filter(filter_fn, s))
