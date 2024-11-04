<<<<<<< HEAD
def unique_digits(n):
    """Return the number of unique digits in positive integer n.
    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    unique = 0
    while n > 0:
        last_digit = n % 10
        n = n // 10
        if not has_digit(last_digit, n):
            unique += 1
    return unique

def has_digit(digit, n):
    while n > 0:
        last_digit = n % 10
        n = n // 10
        if last_digit == digit:
            return True
    return False
=======
def unique_digits(n):
    """Return the number of unique digits in positive integer n.
    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    unique = 0
    while n > 0:
        last_digit = n % 10
        n = n // 10
        if not has_digit(last_digit, n):
            unique += 1
    return unique

def has_digit(digit, n):
    while n > 0:
        last_digit = n % 10
        n = n // 10
        if last_digit == digit:
            return True
    return False
>>>>>>> 1515e9a (disc)
