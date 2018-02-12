"""A number-guessing game."""
import random

print "Greetings! Welcome to the Guessing Game! Huzzah!"
correct_num = random.randint(1, 100)


name = raw_input("What is your name?").title()


def guessing_game():
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

    if guess_count != correct_num:
        print "Too many tries :("

while True:
    print """What do you want to do?
    A. Play the guessing game!
    B. Quit
    CHOOSE A OR B!!!!"""
    user_choice = raw_input("> ").upper()

    if user_choice == "A":
        guessing_game()
    elif user_choice == "B":
        break
    else:
        print "That's not a valid choice. Try again!"
