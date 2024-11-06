def fact_iter(n):
    total = 1
    i = 1
    while i <= n:
        total, i = total * i, i + 1
    return total

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

"""
it is often clearer to think about recursive calls as functional abstractions.
That is, we should not care about how fact(n-1) is implemented in the body
of fact; we should simply trust that it computes the factorial of n-1.
"""
