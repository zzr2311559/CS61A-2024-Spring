<<<<<<< HEAD
def match_k(k):
    def check(x):
        i = 1
        while x // (10 ** k) > 0:
            digit = x % 10
            k_apart = x // (10**k) % 10
            if digit != k_apart:
                return False
            x = x // 10
        return True
    return check
=======
def match_k(k):
    def check(x):
        i = 1
        while x // (10 ** k) > 0:
            digit = x % 10
            k_apart = x // (10**k) % 10
            if digit != k_apart:
                return False
            x = x // 10
        return True
    return check
>>>>>>> 1515e9a (disc)
