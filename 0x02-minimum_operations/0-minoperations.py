#!/usr/bin/python3
"""contains Minimum Operations function"""


def minOperations(n):
    """include min operations function"""
    summe = 0
    m = 1

    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                summe += i
                m *= i
                n = n // i
                break
    return summe
