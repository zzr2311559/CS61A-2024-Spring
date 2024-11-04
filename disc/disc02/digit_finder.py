def find_digit(k):
    def func(x):
        i = 1
        while i <= k:
            last = x % 10
            x = x // 10
            i += 1
        if x == 0:
            last = 0
        return last
    return func
