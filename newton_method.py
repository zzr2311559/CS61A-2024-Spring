def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero) # newton_update漏了(f, df)

def approx_eq(x, y, tollerance=1e-15):
    return abs(x-y) < tollerance

def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

sqrt_64 = square_root_newton(64)




def nth_root_newton(n, a):
    def f(x):
        return pow(x, n) - a
    def df(x):
        return n * pow(x, n-1)
    return find_zero(f, df)

def pow(x, n):
    i = 1
    product = 1
    while i <= n:
        product, i = product * x, i + 1
    return product


forthrt_16 = nth_root_newton(4, 16)
