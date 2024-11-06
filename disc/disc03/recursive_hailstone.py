def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """

    if n == 1:
        print(1)
    elif n % 2 == 0:
        print(n)
        n = n // 2
        return hailstone(n)
    else:
        print(n)
        n = 3 * n + 1
        return hailstone(n)
