def f(s=[]):
    """
    >>> f()
    1
    >>> f()
    2
    >>> f()
    3
    """
    s.append(5)
    return len(s)
