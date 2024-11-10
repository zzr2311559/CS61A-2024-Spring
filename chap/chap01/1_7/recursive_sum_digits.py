def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last_digit, last_digit = n // 10, n % 10
        return sum_digits(all_but_last_digit) + last_digit

def sum_digits_iter(n):
    total = 0
    while n > 0:
        last = n % 10
        total = total + last
        n = n // 10
    return total
