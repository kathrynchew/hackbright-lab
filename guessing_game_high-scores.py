import random
import time
import datetime

high_scores = {}

def guessing_game():
    """A number-guessing game."""

    print "Greetings! Welcome to the Guessing Game! Huzzah!"
    correct_num = random.randint(1, 100)
    guess_count = 1

    name = raw_input("What is your name?").title()

    print "Hello, {}!".format(name)
    while True:
        print "Please guess a number between 1 and 100. Use digits only."

        number_guess = raw_input("> ")

        try:
            number_guess = int(float(number_guess))

            if 0 < number_guess < 101:
                if number_guess == correct_num:
                    print "Congratulations, you won the game! {} is the correct number.\nYou found the secret number in {} tries.".format(correct_num, guess_count)
                    # if guess_count < high_scores["1."] or high_scores["1."] == "--":
                    #     high_scores["1."] = guess_count
                    #     print "You have a new high score!"
                    # elif guess_count < high_scores["2."] or high_scores["2."] == "--":
                    #     high_scores["2."] = guess_count
                    #     print "You have a new high score!"
                    # elif guess_count < high_scores["3."] or high_scores["3."] == "--":
                    #     high_scores["3."] = guess_count
                    #     print "You have a new high score!"
                    win_time = time.time()
                    date_stamp = datetime.datetime.fromtimestamp(win_time).strftime('%Y-%m-%d %H:%M:%S')
                    high_scores[name + " " + date_stamp] = guess_count
                    # print high_scores
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

while True:
    print """What do you want to do?
    A. Play the guessing game!
    B. See high scores
    C. Exit
    Choose A, B or C"""

    user_choice = raw_input("> ").upper()

    if user_choice == "A":
        guessing_game()
    elif user_choice == "B":
        count = 1
        while count < 3:
            for key in sorted(high_scores):
                # print key + str(high_scores[key]) + " guesses"
                print str(count) + ": " + key + ", " + str(high_scores[key])
                count += 1
    elif user_choice == "C":
        break
    else:
        print "That's not a valid choice! Try again."
