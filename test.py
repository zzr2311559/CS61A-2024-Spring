from operator import mul, pow
from math import pi


def square(x):
    return mul(x,x)

def area(shape_constant, r):
    return square(r) * shape_constant

def area_circle(r=1):
    return area(pi, r)

def area_rectangle(r=1):
    return area(1, r)

def area_triangle(r=1):
    return area(1/2, r)
################################################################################



def summation(n, fn):
    total = 0
    i = 1
    while n >= i:
        total, i = fn(i) + total, i + 1
    return total

def identity(x):
    return x

def cube(x):
    return pow(x, 3)

def sum_naturals(n):
    return summation(n, identity)

def sum_cubes(n):
    return summation(n, cube)

def make_adder(n):
    def adder(k):
        return n + k
    return adder
######################################################


def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x,y,tolerance=1e3):
    return abs(x - y) < tolerance

phi = improve(golden_update, square_close_to_successor)
######################################################

def average(x, y):
    return (x + y)/2

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)

result = sqrt(256)
######################################################

def square(x):
    return x * x

def successor(x):
    return x + 1

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

def f(x):
    """Never called"""
    return -x

square_successor = compose1(square, successor)
result = square_successor(12)
######################################################


def remove(n, digit):
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if digit != last:
            kept = kept + last * 10 ** digits
            digits += 1
    return kept
######################################################
