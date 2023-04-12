"""Lu Base component - based on 00_LU_base_v1
Components added after they have been created and tested
"""
import random


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


# Function to generate random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1  # Keep track of rounds
        number = random.randint(1, 100)

        # Adjust balance
        # if the random number is between 1 and 5
        # user gets a unicorn (add $4 to balance)
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4
            print(formatter("!", "Congratulations, you got an Unicorn"))
            print()

        # if the random number is between 6 and 36
        # user gets a donkey (subtract $1 from balance)
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1
            print(formatter("#", "Sadly, you got a Donkey"))
            print()

        # in all other cases the token must be a horse or a zebra
        # subtract $0.50 from the balance in either case
        else:
            # if the number is even, set the token to zebra
            if number % 2 == 0:
                token = "zebra"
                balance -= 0.5
                print(formatter(":", "Sadly, you got a Zebra"))
                print()

            # Otherwise set the token to horse
            else:
                token = "horse"
                balance -= 0.5
                print(formatter("~", "Sadly, you got a Horse"))
                print()

        # Output
        print(f"Round {rounds_played}. Token: {token}, Balance: ${balance:.2f}")
        print()
        if balance < 1:
            print("Sorry you have run out of money")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round?\npress <enter> to play again or "
                               "'x' to exit ")
        print()
    return balance


# function to format text
def formatter(_symbol, _text):
    sides = _symbol * 3
    formatted_text = f"{sides} {_text} {sides}"
    top_bottom = _symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine go here....
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()

played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

# Ask the user how much they want to add to their account to play with
starting_balance = num_checker("How much would you like to add to your account to play with? $", 1, 10)
print(f"You have ${starting_balance} in your account to play with")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print()
print(formatter("*", "Goodbye"))
