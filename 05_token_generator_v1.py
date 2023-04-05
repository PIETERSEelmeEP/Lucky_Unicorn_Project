"""Component 3 (random tokens) v1
Generate random choice of token in random order"""

import random

tokens = ["Unicorn", "Horse", "Donkey", "Zebra"]

# Testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')  # Can wrap output making it easier to screenshot
