#!/usr/bin/python


def frame(text):
    text_length = len(text)
    text_row = "* " + text + " *"
    other_row = "*" * text_length + "*"*4
    new_text = other_row + "\n" + text_row + "\n" + other_row
    return new_text


def triangle(row):
    output = ""
    for number in range(0, row+1):
        output += "*" * number + "\n"


def flag(size=0):

    amount = 21*size

    text_row = "*" * int(((amount-1)/2)) + " " + "*" * (int((amount-1)/2))
    text_column = ""
    for number in range(1, 10):
        if(number == 5):
            text_column += "\n"
        else:
            text_column += text_row + "\n"
    return text_column


print(frame("Välkommen till Python"))


print(triangle(3))

print(flag(1))