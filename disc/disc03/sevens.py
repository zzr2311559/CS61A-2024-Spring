def sevens(n, k):
    """
    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    turn = 1
    direction = 0 # 0 denotes clockwise, 1 denotes counterclockwise
    who = 0
    while turn <= n:
        if direction == 0:
            who =  who + 1
            if who == k+1:
                who = 1
        else:
            who = who - 1
            if who == 0:
                who = k
        if has_seven(turn) or turn % 7 == 0:
            direction = 1 - direction
        turn += 1
    return who




def has_seven(n):
    if n < 10:
        return True if n == 7 else False
    else:
        all_but_last, last = n // 10, n % 10
        if last == 7:
            return True
    return has_seven(all_but_last)

"""
Official Solution
"""

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)

def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        if i % 7 == 0 or has_seven(i):
            direction = -direction
        who = who + direction
        if who > k:
            who = 1
        if who < 1:
            who = k
        return f(i + 1, who, direction)
    return f(1,1,1)



































#
