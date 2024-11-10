def divisors(n):
    return [1] + [x for x in range(2,n) if n % x == 0]

"""
>>> divisors(4)
[1, 2]
>>> divisors(12)
[1, 2, 3, 4, 6]
"""

[n for n in range(1, 1000) if sum(divisors(n)) == n]

def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)
