def streak(n):
    """Return whether positive n is a dice integer in which all the digits are the same.
    >>> streak(22222)
    True
    >>> streak(4)
    True
    >>> streak(22322) # 2 and 3 are different digits.
    False
    >>> streak(99999) # 9 is not allowed in a dice integer.
    False
    """
    d = n % 10
    if d < 1 or d > 6:
        return False
    while n:
        if (n // 10) % 10 != 0 and (n // 10) % 10 != d:
            return False
        n = n // 10
    return True

def changes(n):
    """Return the number of adjacent digits that are different in dice number n.
    >>> changes(22222)
    0
    >>> changes(222255)
    1
    >>> changes(22322)
    2
    >>> changes(22366666622)
    3
    >>> changes(52431)
    4
    """
    count = 0
    while n >= 10:
        if n % 10 != (n // 10) % 10:
            count = count + 1
        n = n // 10
    return count

def count_if(f):
    """Return a function that takes a positive integer n and returns
    the count of its digits for which f returns a true value.
    >>> is_three = lambda d: d == 3
    >>> count_threes = count_if(is_three) # count_threes returns the number of threes in n
    >>> count_threes(431663334231)
    # 3 appears 5 times
    5
    """
    def g(n):
        count = 0
        while n:
            if f(n % 10):
                count += 1
            n = n // 10
        return count
    return g

def count_at_least(k):
    """Return a function that returns how many of the digits of its argument are at least k.
    >>> above_3 = count_at_least(3) # above_3 returns the # of digits greater than or equal to 3
    >>> above_3(431663334231)
    9
    """
    return count_if(lambda d: d >= k)

def times(k, n, d):
    """Returns whether n contains digit d exactly k times.
    >>> times(3, 6132344561, 4) # 4 only appears 2 times
    False
    >>> times(3, 61323445614, 4) # 4 appears exactly 3 times
    True
    """
    return count_if(lambda x: x == d)(n) == k

def streaks(n):
    """Return whether positive n is a dice integer in which all the digits are the same.
    >>> streak(22222)
    True
    >>> streak(4)
    True
    >>> streak(22322) # 2 and 3 are different digits.
    False
    >>> streak(99999) # 9 is not allowed in a dice integer.
    False
    """
    return n % 10 <= 6 and n % 10 >= 1 and count_if(lambda x: (n // 10) % 10 != 0 and (n // 10) % 10 == x)(n) == count_if(lambda y: y != 0)(n)
