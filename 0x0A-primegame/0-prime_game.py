#!/usr/bin/python3

def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = [True] * (max_n + 1)
    p = 2
    while p * p <= max_n:
        if primes[p]:
            for i in range(p * p, max_n + 1, p):
                primes[i] = False
        p += 1
    prime_counts = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
