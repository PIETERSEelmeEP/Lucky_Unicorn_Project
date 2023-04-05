"""Component 3 (random tokens) v4
Format currency
Ensure odds favour the house - 10% chance of unicorn and 30% chance for each
of donkey, horse, or zebra
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
