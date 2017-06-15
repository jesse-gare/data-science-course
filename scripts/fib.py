#!/usr/bin/env python
"""
This is a fibonacci module.
"""

def fibonacci(N):
    """
    A function to get the first N fibonacci numbers.
    >>> fibonacci(2)
    [1, 1]
    >>> fibonacci(3)
    [1, 1, 3]
    """
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

if __name__ == "__main__":
    import sys
    N = int(sys.argv[1])
    print(fibonacci(N))

    import doctest
    doctest.testmod()
