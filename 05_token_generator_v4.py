"""Component 3 (random tokens) v4
Calculate percentages to ensure the odds favour teh house
5% Unicorn, 30% Donkey, and the remaining 65% Horse/Zebra
"""

import random

STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop to generate 20 tokens
for item in range(20):
    number = random.randint(1, 100)

    # adjust balance
    # if the random number is between 1 and 5
    # User gets a unicorn (add $4 to balance)
    if 1 <= number <= 5:
        token = "Unicorn"
        balance += 4

    # if the random number is between 6 and 36
    # User gets a donkey (subtract $1 from balance)
    elif 6 <= number <= 36:
        token = "Donkey"
        balance -= 1

    # in all other cases the token must be a horse or a zebra
    # (subtract $0.50 from the balance in either case)
    else:
        # If the number is even, set the token Zebra
        if number % 2 == 0:
            token = "Zebra"
            balance -= 0.5
        # otherwise, set the token to Horse
        else:
            token = "Horse"
            balance -= 0.5

    # output
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance:.2f}")
