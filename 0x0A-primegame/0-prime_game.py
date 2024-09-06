#!/usr/bin/python3
def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    maria = 0
    ben = 0

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
                new_numbers = []
                for num in numbers:
                    if num == 1 or num % i != 0:
                        new_numbers.append(num)
                numbers = new_numbers

                if current_player == "Maria":
                    current_player = "Ben"
                else:
                    current_player = "Maria"

            i += 1

        if current_player == "Ben":
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
