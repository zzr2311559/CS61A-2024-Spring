def cascade(n):
    """Print a cascade of prefixes of n.
    >>> cascade(1234)
    1234
    123
    12
    1
    12
    123
    1234
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

def cascadeV2(n):
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)

def half_cascade(n):
    n = n // 10
    if n:
        half_cascade(n)
        print(n)

def inverse_cascade(n):
    """
    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)
# def grow(n):
#     def f_then_g(f, g, n):
#         if n:
#             f(n)
#             g(n)
#     return f_then_g(grow, print, n // 10)

# def shrink(n):
#     def f_then_g(f, g, n):
#         if n:
#             f(n)
#             g(n)
#     return f_then_g(print, shrink, n // 10)
################################################################################

def inverse_cascadeV2(n):
    growV2(n)
    print(n)
    shrinkV2(n)


def growV2(n):
    n = n // 10
    if n < 10:
        print(n)
    else:
        grow(n)
        print(n)

def shrinkV2(n):
    n = n // 10
    if n < 10:
        print(n)
    else:
        print(n)
        shrink(n)
