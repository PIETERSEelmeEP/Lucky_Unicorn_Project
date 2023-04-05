"""Lu Base component
Components added after they have been created and tested"""


# Yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If user says yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If user says no, output 'Display Instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no' :")


# function to display instructions
def instructions():
    print("***** How To Play *****")
    print()
    print("The rules of the game will go here")
    print()


# number checking function
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


# Main routine go here....
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

# Ask the user how much they want to add to their account to play with
user_balance = num_checker("How much would you like to add to your account to play with? $", 1, 10)
print(f"You have ${user_balance} in your account to play with")
