"""
>>> range(1, 10)  # Includes 1, but not 10
range(1, 10)


>>> list(range(5, 8))
[5, 6, 7]

>>> list(range(4))
[0, 1, 2, 3]


>>> for _ in range(3):
        print("Hellow World!")

Hellow World!
Hellow World!
Hellow World!

"""
def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheer(n):
    for _ in range(3):
            print("Hellow World!")
