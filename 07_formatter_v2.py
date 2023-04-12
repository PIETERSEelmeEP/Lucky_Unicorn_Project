"""Component 5 - statement formatter v2
Change v1 into a function
"""


# function to format text
def formatter(_symbol, _text):
    sides = _symbol * 3
    formatted_text = f"{sides} {_text} {sides}"
    top_bottom = _symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
text = input("Enter the statement you want to format: ")
symbol = input("What symbol do you want to use: ")
print()
print(formatter(symbol, text))
