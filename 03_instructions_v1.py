"""Took function from component 02_v1 as the basis for this new function which
incorporates both yes/no and show instructions"""


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
    print("program continues")
    print()


# Main routine go here....
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()
else:
    print("Program continues")
