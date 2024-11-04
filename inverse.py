def search(f):
    x = 0
    while not f(x):
        x += 1
    return x

def is_three(x):
    return x == 3

def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)

def inverse(f):
    """Return g(y) such that g(f(x)) -> x."""
    def inverse_of_f(y):
        def func2(x):
            return f(x) == y
        return search(func2)
    return inverse_of_f
"""
这里的inverse函数设计思路为，函数的输入为正函数，返回一个能够提供反函数值的函数，
这个函数收到给定的输入数字y，调用search函数，从0开始寻找，满足f(x) == y的x值，
如果找到了就直接返回x值。
"""
