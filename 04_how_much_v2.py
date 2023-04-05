"""Component 2 (How much) v2
Use try/accept and pull error message put of the loop"""

error = "Please enter a whole number between 1 and 10\n"
valid = False

# Keep asking until a valid amount (1:10) is entered
while not valid:
    try:
        # Ask for amount
        user_balance = int(input("How much would you wanna play with? $"))

        # Check if balance is valid(too high or too low)
        if 0 < user_balance <= 10:
            print(f"You are playing with ${user_balance} in your account")
            valid = True
        else:
            print(error)
