#!/usr/bin/python3
""" Prime Game
"""


def isWinner(x, nums):
    """Who wins in Prime Game"""
    if x < 1 or not nums:
        return None
    wins_maria, wins_ben = 0, 0
    highest_number = max(nums)
    total = [True] * highest_number
    total[0] = False  # 1 is not a prime number
    for index, prime in enumerate(total):
        if prime and index + 1 > 1:
            for non_prime in range((index + 1) * 2, highest_number + 1,
                                   index + 1):
                total[non_prime - 1] = False
    for rnd_numb in nums[:x]:
        count_primes = sum(total[:rnd_numb])
        if count_primes % 2 == 0:
            wins_ben += 1
        else:
            wins_maria += 1
    if wins_maria == wins_ben:
        return None
    return "Maria" if wins_maria > wins_ben else "Ben"
