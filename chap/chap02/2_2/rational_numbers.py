"""
Suppose we have a way of constructing a rational number from a numerator and a
denominator. We also assume that, given a rational number, we have a way of
selecting its numerator and its denominator component.

Constructor function:
1. rational(n, d) returns the rational number with numerator n and denominator d.

Selector function:
1. numer(x) returns the numerator of the rational number x.
2. denom(x) returns the denominator of the rational number x.
"""

def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom (y))

def print_rational(x):
    print(numer(x), '/', denom(x))

def rationals_are_equal(x, y):
    return numer(x) * denom(y) == denom(x) * numer(y)

"""
We can use 2-element list to represent pair, constructing the function below.
"""

def rational(n, d):
    return [n, d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]


"""
>>> half = rational(1, 2)
>>> print_rational(half)
1 / 2
>>> third = rational(1, 3)
>>> print_rational(mul_rationals(half, third))
1 / 6
>>> print_rational(add_rationals(third, third))
6 / 9
"""

from math import gcd

def rational(n, d):
    """
    >>> print_rational(add_rationals(third, third))
    2 / 3
    """
    g = gcd(n, d)
    return (n//g, d//g)

################################################################################

"""
Abstraction  Barriers

An abstraction barrier violation occurs whenever a part of the program that can
use a higher level function instead uses a function in a lower level.
"""

def square_rational(x):
    return mul_rationals(x, x)

def square_rational_violating_once(x):
    return rational(numer(x) * numer(x), denom(x), denom(x))

def square_rational_violating_twice(x):
    return [x[0] * x[0], x[1] * x[1]]
