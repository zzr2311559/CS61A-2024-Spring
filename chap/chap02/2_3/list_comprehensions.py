odds = [1, 3, 5, 7, 9]
"""
>>> [x+1 for x in odds]
[2, 4, 6, 8, 10]

>>> [x for x in odds if 25 % x == 0]
[1, 5]

>>> [x+1 for x in odds if 25 % x == 0]
[2, 6]
"""
