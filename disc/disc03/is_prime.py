def is_prime(n):
    assert n > 1
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_prime_rec(n):
    """
    >>> is prime_rec(8)
    False
    >>> is_prime_rec(1)
    True
    >>> is_prime_rec(2)
    True
    """
    def helper(i):
        if n % i == 0:
            return False if n != 2 else True
        elif i == n - 1:
            return True
        return helper(i + 1)
    return helper(2)

"""
Official Solution
"""
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def check_all(i):
        "Check whether no number from i up to n evenly divides n."
        if i == n:      # could be replaced with i > (n ** 0.5)
            return True
        elif n % i == 0:
            return False
        return check_all(i + 1)
    return check_all(2)
