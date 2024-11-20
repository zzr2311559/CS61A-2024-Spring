This is a note that contains some problems when doing the [**Cats**](https://www.learncs.site/docs/curriculum-resource/cs61a/project/cats#problem-6-3-pts) project.



## For problem 6: 

> Implement `feline_fixes`, which is a diff function that takes two strings. It returns the minimum number of characters that must be changed in the `typed` word in order to transform it into the `source` word. If the strings are not of equal length, the difference in lengths is added to the total.

there is a special requirement that needs to be fulfilled. The description is as followed:

> Why is there a limit? We know that `autocorrect` will reject any `source` word whose difference with the `typed` word is greater than `limit`. It doesn't matter if the difference is greater than `limit` by 1 or by 100; autocorrect will reject it just the same. Therefore, as soon as we know the difference will be above `limit`, it makes sense to try to minimize extra computation, even if the returned difference won't be exactly correct.

A smart way to implement this trick is to leverage the power of the argument `limit` by passing `limit-1` to the next recursion if the current first character of `typed` and `source` is not the same, otherwise, pass `limit` instead of `limit-1`. By construct a framework like this, we managed to keep track of `limit` and test if it's being exceeded.

So next time, when we have other limitations needed to be fulfilled, try to think about how to impose this limitation by making some changes on the argument that can present that limitation.

The answer could be:

```python
def feline_fixes(typed, source, limit):
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> feline_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> feline_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> feline_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> feline_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> feline_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    if len(source) == 0 and len(typed) == 0:
        return 0
    elif len(source) == 0 or len(typed) == 0:
        return abs(len(typed) - len(source))
    elif limit < 0:
        return 1 # any number that greater the initial limit would do

    else:
        if typed[0] != source[0]:
            return 1 + feline_fixes(typed[1:], source[1:], limit-1) # limit - 1 is how U do the efficient trick, I didn't come up with this idea myself.
        else:
            return feline_fixes(typed[1:], source[1:], limit)
    # END PROBLEM 6

```



## For problem 7:

>Implement `minimum_mewtations`, which is a diff function that returns the minimum number of edit operations needed to transform the `typed` word into the `source` word.

This problem is pretty tricky, since it might be extremely confused when you think of when to choose `add`, `remove`, and `substitute` or just `remain`. But actually, thanks to recursion, you do not need to choose them by hand. 

What we want is a minimum value of a combined function call using the 4 mentioned operation(`<operation>(...<opration>(<operation>(typed, source))`), recursion can help us to find a minimum by go through all the possible choice if you direct a right target, which in this case is, `min`.

```python
def minimum_mewtations(typed, source, limit):
    """A diff function that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.
    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if typed == source:
        return 0
    elif limit < 0:
        return 999
    elif len(typed) == 0 or len(source) == 0:
        return abs(len(typed) - len(source))

    if typed[0] == source[0]:
        remain = minimum_mewtations(typed[1:], source[1:], limit)
        return ramain
    else:
        add = 1 + minimum_mewtations(typed, source[1:], limit-1)
        remove = 1 + minimum_mewtations(typed[1:], source, limit-1)
        substitute = 1 + minimum_mewtations(typed[1:], source[1:], limit-1)
    return min(add, min(remove, substitute))

```



## Reference

https://github.com/y1cunhui/cs61A-2021Fall/tree/main
