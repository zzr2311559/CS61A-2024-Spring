def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    """
    assert n >= 0 and n % 1 == 0, 'the number must be a positive integer.'
    i = 0
    while n >= i:
        i += 1
        if i % 3 == 0:
            if i % 5 == 0:
                print('fizzbuzz')
            else:
                print('fizz')
        else:
            if i % 5 == 0:
                print('buzz')
            else:
                print(i)
