# Ask the user if they have played before
show_instructions = input("Have you previously played this game?: ")

# If user says yes, output 'Program Continues'
if show_instructions == "yes":
    print("Program Continues")

# If user says no, output 'Display Instructions'
elif show_instructions == "no":
    print("Display Instructions")

# Otherwise - show error
else:
    print("Please answer 'yes' or 'no' :")
