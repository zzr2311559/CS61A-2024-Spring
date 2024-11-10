def paths(m, n):
    """
    >>> paths(2, 2)
    2
    >>> paths(3, 3)
    6
    """
    if m == 1:
        return 1
    elif n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)

# Alternative Solution:
# def paths(m, n):
#     def helper(i, j):
#         if i == m:
#             return 1
#         elif j == n:
#             return 1
#         else:
#             return helper(i + 1, j) + helper(i, j + 1)
#     return helper(1, 1)
