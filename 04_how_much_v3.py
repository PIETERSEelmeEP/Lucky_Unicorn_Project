"""Component 2 (How much) v3
More efficient method - includes valid range as the basis of the while loop
which eliminates the need to use the 'valid' variable"""

# Main routine
error = "Please enter a whole number between 1 and 10\n"
user_balance = 0

# Keep asking until a valid amount (1:10) is entered
while not 1 <= user_balance <= 10:
    try:
        user_balance = int(input("Please enter a whole number between 1 and 10\n"
                                 "How much do you wanna play with/add to your account"))
        print()

    except ValueError:
        print(error)

print(f"You have ${user_balance} in your account to play with")
