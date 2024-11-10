def trace(fn):
    def wrapped(x):
        print("->", fn, '(', x')')
        return fn(x)
    return wrapped

@ trace
def tripleV1(x):
    return x * 3

tripleV1(12)


def tripleV2(x):
    return x * 3

tripleV2 = trace(tripleV2)
tripleV2(12)
