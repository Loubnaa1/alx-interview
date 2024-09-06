#!/usr/bin/python3
''' prime game '''


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    maria, ben = 0, 0
    for n in nums:
        numbers = list(range(1, n + 1))
        current_player = "Maria"
        primes_found = []

        i = 2
        while i <= n:
            is_prime = True
            for p in primes_found:
                if i % p == 0:
                    is_prime = False
                    break

            if is_prime:
                primes_found.append(i)
                numbers = [num for num in numbers if num == 1 or num % i != 0]
                current_player = "Ben" if current_player == "Maria" else "Maria"
            i += 1

        maria += current_player == "Ben"
        ben += current_player == "Maria"

    return "Maria" if maria > ben else "Ben" if ben > maria else None
