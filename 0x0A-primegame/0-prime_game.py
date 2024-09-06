#!/usr/bin/python3
""" Prime Game
"""


def isWinner(rounds, numbers):
    """Determine the winner of the Prime Game"""
    if rounds < 1 or not numbers:
        return None

    # Initialize scores and maximum number
    score_maria = score_ben = 0
    max_limit = max(numbers)

    # Create a list to mark prime numbers
    prime_list = [False] * max_limit
    for idx in range(1, max_limit):
        prime_list[idx] = True

    index = 1
    while index < max_limit:
        if prime_list[index]:
            multiple = (index + 1) * 2
            while multiple <= max_limit:
                prime_list[multiple - 1] = False
                multiple += (index + 1)
        index += 1

    game_round = 0
    while game_round < rounds:
        prime_count = sum(prime_list[:numbers[game_round]])
        if prime_count % 2 == 0:
            score_ben += 1
        else:
            score_maria += 1
        game_round += 1

    if score_maria == score_ben:
        return None
    return "Maria" if score_maria > score_ben else "Ben"
