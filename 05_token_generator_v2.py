"""Component 3 (random tokens) v2
Calculate user balance based on random selection of tokens"""

import random

tokens = ["Unicorn", "Horse", "Donkey", "Zebra"]
balance = 100

# Testing loop to generate 100 tokens
for item in range(100):
    token = random.choice(tokens)
    print(token, end='\t')  # Can wrap output making it easier to screenshot

    # adjust balance
    if token == "Unicorn":
        balance += 4
    elif token == "Donkey":
        balance -= 1
    else:
        balance -= 0.50

    # output
    print(f"Token: {token}, Balance: ${balance}")
