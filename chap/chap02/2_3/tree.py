def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branch must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree) # Check if the branches are empty

'''
>>> t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
>>> t
[3, [1], [2, [1], [1]]]
>>> label(t)
3
>>> branches(t)
[[1], [2, [1], [1]]]

>>> label(branches(t)[1])
2
>>> is_leaf(t)
False
>>> is_leaf(branches(t)[0])
True
'''
################################################################################

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

################################################################################

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        print(branch_counts)
        return sum(branch_counts)

################################################################################

def leaves(tree):
    """
    Return a list containing the leaf labels of tree.

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]

    Hint:
    >>> sum([ [1], [2, 3], [4] ], [])
    [1, 2, 3, 4]
    >>> sum([ [1] ], [])
    [1]
    >>> sum([ [[1]], [2] ], [])
    [[1], 2]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

################################################################################

"""Creating new tree"""
def increment_leaves(t):
    """
    Return a tree like t but with leaf labels incremented.
    """
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    """
    Return a tree like t but with all labels incremented.
    """
    return tree(label(t)+1, [increment_leaves(b) for b in branches(t)])

################################################################################

def print_tree(t, indent=0):
    """
    Show all the labels with indentation suggesting tree structure.
    """
    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)

################################################################################

"""Summing paths"""

"""
Some recursive functions build up their results by manipulating the return value
of a recursive call. The function `fact` below is an example of these functions.
"""
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

"""
On the other hand, some recursive function build up their results by passing
information into the recursive call as an argument.
"""
def fact_times(n, k):
    """
    Return k * n * (n-1) * ... * 1
    """
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)
"""
Notice that in `fact_times`, the result of the current call is the same of the returned
call.(eg. fact_times(3, 5) = fact_times(2, 5 * 3))
This idea suggests that the result of the base case needs to be the same result
of the original recursive call.
"""

from tree import *

numbers = tree(3, [tree(4), tree(5,[tree(6)])])
haste = tree('h', [tree('a', [tree('s'), tree('t')]), tree('e')])

def print_sums(t, so_far):
    """
    >>> print_sums(numbers)
    7
    14

    >>> print_sums(haste, '')
    has
    hat
    he
    """
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)

################################################################################

def count_paths(t, total):
    """
    Return the number of paths from the root to any node in tree t for which the
    labels along the path sum to total.

    >>> t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total-label(t)) for b in branches(t)])
