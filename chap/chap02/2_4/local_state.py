"""
the `nonlocal` statement declares that whenever we change the binding of the
name `balance`, the binding is changed in the first frame in which `balance` is
already bound. Recall that without the nonlocal statement, an assignment
statement would always bind a name in the first frame of the current
environment. The `nonlocal` statement indicates that the name appears somewhere
in the environment other than the first (local) frame or the last (global)
frame.
"""

"""
The first example shows that without `nonlocal` statement, we can still get
access to values that is not defined in the current frame. But in this case, we
can not modify that value at the parent frame.

Instead, the second example uses `nonlocal` statement, which thereby has a
effect of so-called `non-pure`, changing the value of `balance` in the
parent frame.

Tips: Go to https://pythontutor.com/cp/composingprograms.html#mode=edit for a
detailed illustration.
"""

def make_withdraw(balance):
    """
    >>> withdraw = make_withdraw(100)
    >>> withdraw(25)
    75
    >>> withdraw(25)
    75
    """
    def withdraw(amount):
        balance_copy = balance
        if amount > balance_copy:
            return 'Insufficient funds'
        else:
            balance_copy = balance_copy - amount
            return balance_copy
    return withdraw

def make_withdraw(balance):
    """
    >>> withdraw = make_withdraw(100)
    >>> withdraw(25)
    75
    >>> withdraw(25)
    50
    """
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        else:
            balance = balance - amount
            return balance
    return withdraw


"""
Ever since we first encountered nested `def` statements, we have observed that a
locally defined function can look up names outside of its local frames. No
`nonlocal` statement is required to access a non-local name. By contrast, only
after a `nonlocal` statement can a function change the binding of names in these
frames.
"""
