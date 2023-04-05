"""Component 2 (How much) v4
Changing v3 into a function
Also needed to change user_balance to the more generic variable name 'response' and
to change the condition and position of the number comparison into the loop to make
the function recyclable"""


# Function
def num_checker(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a whole number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount is entered (low:high)
    while True:
        try:
            # Ask for the amount
            response = int(input(question))

            # Check if the response is in the required range
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Main routine
user_balance = num_checker("How much would you like to add to your account to play with? $", 1, 10)
print(f"You have ${user_balance} in your account to play with")
