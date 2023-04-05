"""Component 3 (random tokens) v4
Calculate percentages to ensure the odds favour teh house
5% Unicorn, 30% Donkey, and the remaining 65% Horse/Zebra
"""

import random

tokens = ["Unicorn",
          "Horse", "Horse", "Horse",
          "Donkey", "Donkey", "Donkey",
          "Zebra", "Zebra", "Zebra"]
STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)

    # adjust balance
    if token == "Unicorn":
        balance += 4
    elif token == "Donkey":
        balance -= 1
    else:
        balance -= 0.50

    # output
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance:.2f}")
