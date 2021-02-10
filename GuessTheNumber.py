# The computer randomly generates a number.
# The user inputs a number, and the computer will tell you
# if you are too high, or too low. Then you will get to keep
# guessing until you guess the number.
import random

guess_count = 0
print("Try and guess my number!")
while True:
    try:
        difficulty = int(input("How hard would you like this to be? \n Try and guess a number between 1 and: "))
        print("")
        if difficulty < 3:
            print("Please enter a number of 3 or more\n")
            continue

    except ValueError:
        print("Please enter a number")
        continue
    else:
        break

number_to_guess = random.randint(1, difficulty)
while True:
    try:
        user_guess = int(input("What's your guess? "))
        if user_guess < 1 or user_guess > difficulty:
            print("value out of range\n")
            continue
        else:
            if user_guess < number_to_guess:
                print("Too low\n")
                guess_count = guess_count + 1
                continue
            elif user_guess > number_to_guess:
                print("Too High\n")
                guess_count = guess_count + 1
                continue
            else:
                guess_count = guess_count + 1
                print("{}{} {}".format("\n\nCorrect! Number of tries: ", guess_count, "\nWell Done!"))
                break
    except ValueError:
        print("Sorry please enter a whole number\n")
        continue
    # else:
    #    break

