#!/usr/bin/python3
""" This script contains the definition of the minOperations function
"""


def minOperations(n):
    """ calculate the fewest number of operations
        Args:
            n (int): number
        Return:
            returns a number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i + minOperations(n//i)
        return n
