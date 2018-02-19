"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def check_operator():
    """Get user input and check which operator is bring requested"""

    while True:
        user_input = raw_input(">")
        split_input = user_input.split(" ")

        if len(split_input) == 3:

            if split_input[0] == '+':
                print add(int(split_input[1]), int(split_input[2]))

            elif split_input[0] == '-':
                print subtract(int(split_input[1]), int(split_input[2]))

            elif split_input[0] == '*':
                print multiply(int(split_input[1]), int(split_input[2]))

            elif split_input[0] == '/':
                print divide(int(split_input[1]), int(split_input[2]))

            elif split_input[0] == 'pow':
                print power(int(split_input[1]), int(split_input[2]))

            elif split_input[0] == 'mod':
                print mod(int(split_input[1]), int(split_input[2]))

            else:
                print "That is an incorrect input. Try again!"

        elif len(split_input) == 2:

            if split_input[0] == 'square':
                print square(int(split_input[1]))

            elif split_input[0] == 'cube':
                print cube(int(split_input[1]))

            else:
                print "That is an incorrect input. Try again!"

        elif split_input[0].lower() == 'q':
            break

        else:
            print "That is an incorrect input. Try again!"

check_operator()
