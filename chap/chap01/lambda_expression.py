def compose1(f, g):
    return lambda x: f(g(x))

f = compose1(lambda x: x * x, lambda y: y + 1)

result = f(12)

################################################################################

compose1 = lambda f, g: lambda x: f(g(x))

def square(x):
    return x * x

def add_one(x):
    return x + 1

compose2 = compose1(square, add_one)

result = compose2(12)

################################################################################

a = 1
def f(g):
    a = 2
    return lambda y: a * g(y)

f(lambda y: a + y)(a)
