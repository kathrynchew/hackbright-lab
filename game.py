"""A number-guessing game."""
import random

high_scores = {}
num_plays = 0

print "Greetings! Welcome to the Guessing Game! Huzzah!"
correct_num = random.randint(1, 5)


name = raw_input("What is your name?").title()


def guessing_game(high_scores):
    global num_plays
    num_plays += 1
    guess_count = 1
    print "Hello, {}!".format(name)
    while guess_count < 6:
        print "Please guess a number between 1 and 100. Use digits only. You only get 5 guesses! You are on guess number {}".format(guess_count - 1)

        number_guess = raw_input("> ")

        try:
            number_guess = int(float(number_guess))

            if 0 < number_guess < 101:
                if number_guess == correct_num:
                    print "Congratulations, you won the game! {} is the correct number.\nYou found the secret number in {} tries.".format(correct_num, guess_count)
                    high_scores[name + " " + str(num_plays)] = guess_count
                    print num_plays
                    break
                elif number_guess > correct_num:
                    print "Sorry, that guess is too high! Try a lower number."
                else:
                    print "Sorry, that guess is too low! Try a higher number."
            else:
                print "What are you thinking! I said between 1-100!!!!! Try again, jeez!"
        except:
            print "I said digits, bozo! Don't you know how to count? Try again!"
        guess_count += 1

    if number_guess != correct_num:
        print "Too many tries :("


def print_dict(high_scores):
    for key in high_scores:
        print key + ": " + str(high_scores[key])


while True:
    print """What do you want to do?
    A. Play the guessing game!
    B. View High Scores
    C. Quit"""
    user_choice = raw_input("> ").upper()

    if user_choice == "A":
        guessing_game(high_scores)
    elif user_choice == "B":
        print_dict(high_scores)
    elif user_choice == "C":
        break
    else:
        print "That's not a valid choice. Try again!"
