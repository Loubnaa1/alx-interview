#!/usr/bin/python3
"""contains the function make change"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total <= 0:
            break
        count = total // coin
        total -= count * coin
        coin_count += count
    if total == 0:
        return coin_count
    else:
        return -1
