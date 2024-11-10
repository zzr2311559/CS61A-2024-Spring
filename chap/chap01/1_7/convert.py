def normal_rec_sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last = n // 10
        last = n % 10
        return last + normal_rec_sum_digits(all_but_last)
        """
        `all_but_last` is what's left to sum
        `last + normal_rec_sum_digits(all_but_last)` is a partial sum
        """

def sum_digits_iter(n):
    """
    Converting recursion to iteration
    """
    digit_sum = 0 # need a local var to keep track of partial sum
    while n > 0: # if there are digits left to sum
        n, last = n // 10, n % 10 # rebind n to update(n)/all_but_last
        digit_sum = digit_sum + last # update local var
    return digit_sum

def sum_digits_rec(n, digit_sum=0):
    """
    Converting iteration to recursion
    """
    if n == 0:
        return digit_sum
    else:
        n, last = n // 10, n % 10
        return sum_digits_rec(n, digit_sum + last)
