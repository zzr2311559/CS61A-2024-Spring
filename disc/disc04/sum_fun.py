"""
Fill the blanks
"""
# def sums(n,m):
#     """Return lists that sum to n containing positive numbers up to m that
#     have no adjacent repeats.
#
#     >>> sums(5, 1)
#     []
#     >>> sums(5, 2)
#     [[2, 1, 2]]
#     >>> sums(5, 3)
#     [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
#     >>> sums(5, 4)
#     [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1]]
#     >>> sums(5, 5)
#     [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
#     >>> sums(6, 3)
#     [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
#     """
#     if n < 0: # if n < 0, then we need to drop the value of that term.
#         return [] # `for i in []` gives us nothing
#     elif n == 0:
#         sums_to_zero = [] # `for i in [[]]` gives us ``[]``
#         return [sums_to_zero]
#     result = []
#     for k in range(1, m+1):
#         result = result + [ ___ + rest for rest in ___ if rest == [] or ___ ]
#     return result




def sums(n,m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 4)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if n < 0: # if n < 0, then we need to drop the value of that term.
        return [] # `for i in []` gives us nothing
    elif n == 0:
        sums_to_zero = [] # `for i in [[]]` gives us ``[]``
        return [sums_to_zero]
    result = []
    for k in range(1, m+1):
        """
        [<map expression> for <name> in <sequence expression> if <filter expression>]
        """
        result = result + [([k] + rest) for rest in sums(n-k, m) if rest == [] or rest[0] != k] # [k] + rest is seen as combined expression, it can only be executed if filter expression is satisfied
    return result
