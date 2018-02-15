"""A number-guessing game."""
import random

all_scores = {}
high_scores = []
num_plays = 0

print "Greetings! Welcome to the Guessing Game! Huzzah!"


name = raw_input("What is your name? > ").title()


def guessing_game():
    """Loops through game & updates high scores"""
    #Importing vars as global vars so function can modify them, not just use contents
    global num_plays
    global all_scores
    global high_scores
    num_plays += 1
    guess_count = 1
    correct_num = random.randint(1, 100)

    while guess_count < 10:
        print "\nPlease guess a number between 1 and 100. Use digits only. \nYou only get 10 guesses! \nYou are on guess number {}\n".format(guess_count - 1)

        number_guess = raw_input("> ")

        try:
            number_guess = int(float(number_guess))

            if 0 < number_guess < 101:
                if number_guess == correct_num:
                    print "\nCongratulations, you won the game! {} is the correct number.\nYou found the secret number in {} tries.\n".format(correct_num, guess_count)
                    all_scores[name + " turn #" + str(num_plays)] = guess_count
                    generate_high_scores()
                    break
                elif number_guess > correct_num:
                    print "\nSorry, that guess is too high! Try a lower number."
                else:
                    print "\nSorry, that guess is too low! Try a higher number."
            else:
                print "\nWhat are you thinking! I said between 1-100!!!!! Try again, jeez!"
        except:
            print "I said digits, bozo! Don't you know how to count? Try again!"
        guess_count += 1

    if number_guess != correct_num:
        print "\nToo many tries :("


def generate_high_scores():
    """Takes dictionary with all scores, sorts by value, tracks top 3 scores"""
    global high_scores
    global all_scores
    counter = 0
    check_current_score = []
    for key in sorted(all_scores.iterkeys(), key=lambda k: all_scores[k]):
        if counter < 3:
            check_current_score.append((key, all_scores[key]))
            counter += 1
    if check_current_score != high_scores:
        print "Congratulations you got a new high score!"
        # print "check_current_score: "
        # print check_current_score
    high_scores = check_current_score


def print_scores(high_scores):
    """Print top 3 scores formatted as a list"""
    place_count = 1
    print "\nThe current top 3 scores are:"
    for item in high_scores:
        print str(place_count) + ". " + str(item[0]) + ": " + str(item[1]) + " guesses"
        place_count += 1


while True:
    print "\nHello, {}!".format(name)
    print """What do you want to do?
    A. Play the guessing game!
    B. View High Scores
    C. Quit"""
    user_choice = raw_input("> ").upper()

    if user_choice == "A":
        guessing_game()
    elif user_choice == "B":
        print_scores(high_scores)
    elif user_choice == "C":
        break
    else:
        print "That's not a valid choice. Try again!"
