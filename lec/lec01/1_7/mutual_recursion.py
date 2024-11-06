def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)

result = is_even(4)
"""
Mutually recursive functions can be turned into a single recursive function
by breaking the abstraction boundary between the two functions. In this example,
the body of is_odd can be incorporated into that of is_even, making sure to
replace n with n-1 in the body of is_odd to reflect the argument passed into it
"""

def is_even(n):
    if n == 0:
        return True
    else:
        if n - 1 == 0:
            return False
        else:
            return is_even((n-1)-1)
################################################################################

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = n // 10, n % 10
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return last + sum_digits(all_but_last)
