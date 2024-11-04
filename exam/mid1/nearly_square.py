def near_square(n, k):
    """Return the largest integer that is less than or equal to n and
    equals a * b for some positive integers a and b where abs(a- b) <= k.
    >>> near_square(125, 0) # 11 * 11 = 121 and abs(11- 11) = 0
    121
    >>> near_square(120, 3) # 10 * 12 = 120 and abs(10- 12) = 2
    120
    >>> near_square(120, 1) # 10 * 11 = 110 and abs(10- 11) = 1
    110
    """
    while True:
        gap = k
        while gap >= 0:
            x = solve(gap, n)
            if x == round(x):
                return n
            gap = gap - 1
        n = n - 1




def solve(b, c):
    """Returns the largest x for which x * (x + b) = c
    >>> solve(2, 120) # x=10 solves x * (x + 2) = 120
    10.0
    >>> solve(2, 121) # x=10.045... solves x * (x + 2) = 121
    10.045361017187261
    """
    return (b*b/4 + c) ** 0.5- b/2
