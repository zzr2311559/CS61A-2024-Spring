def swipe(n):
    if n < 10:
        print(n)
    else:
        all_but_last, last = n // 10, n % 10
        print(last)
        swipe(all_but_last)
        print(last)
