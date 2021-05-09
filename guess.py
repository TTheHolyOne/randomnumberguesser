"""
MADE BY TTHEHOLYONE#1642
GITHUB.COM/TTheHolyOne
YOUTUBE.COM/TTHEHOLYONE

To run the program:

python rannumgame.py

This is a random number guessing game made in Python 3.9
This will have a random number selected each round
you can choose how many guesses you get
"""

# Made in 2 Hours


# Uses these packages (ALL PREINSTALLED)

import random # Random
import time # Time
import sys # System
import os # Operating System

# Program

# Have the program inside a function so we can restart it later on...

def program():
    def options():
        # user prompt for the choices
        option = int(input("""
The Holy Number Game

1: Play
2: Credits
3: Quit
"""))
        if option == 1:
            pass
        elif option == 2:

            # Credits

            print("""
Game made by:

Discord: TTheHolyOne#1642
Github: github.com/TTheHolyOne
Youtube: youtube.com/TTheHolyOne
Paypal: paypal.me/ttheholymod

""")
            input("Press enter to proceed")
            options()
        elif option == 3:
            sys.exit()
        else:
            print("Not sure what you mean...")
            time.sleep(1)
            sys.exit()
            options()
    options()

# Asking for the random number it picks
# error handling
    def ask_for_number(message):
        while True:
            i = input(message)
            if i.isdigit():
                return int(i)
            else:
                print("That's not a number!")

    num1 = ask_for_number("Enter the first number: ")
    num2 = ask_for_number("Enter the second number: ")

    input("Press enter to proceed...\n")
    time.sleep(3)
    os.system('cls')

    # Asking for how many guesses the user gets

    number = random.randint(num1, num2)
    print(f"The random number will be {num1} - {num2}")
    input("Press enter to proceed...\n")
    time.sleep(1)
    os.system('cls')
# error handling
    def ask_for_guesses(message):
        while True:
            i = input(message)
            if i.isdigit():
                return int(i)
            else:
                print("That's not a number!")
    guesses = ask_for_guesses("Enter amount of guesses you would like...\n")
    guess = 0

        # Starting the game...

    while True:
        if guess > guesses:
            print("Out of guesses\n:( Try again")
            input("Press enter to proceed")
            program()

# error handling
        def ask_for_rannumber(message):
            while True:
                i = input(message)
                if i.isdigit():
                    return int(i)
                else:
                    print("Hey! Thats not a number..!")

        char = ask_for_rannumber(f"Please enter number to guess number must be {num1} - {num2}!\n")
        if char > number:
            guess += 1
            os.system('cls')
            print(f"""
Too high!
You have guessed {guess} times!
You only have {guesses}! Be Careful!
Please try again!
        """)
        if char < number:
            guess += 1
            os.system('cls')
            print(f"""
Too low!
You have guessed {guess} times!
You only have {guesses}! Be Careful!
Please try again!
        """)
        if char == number:
            guess += 1
            os.system('cls')
            input(f"""
You got it!
You have guessed {guess} times!
You had {guesses} guesses!
Great Job!

Press enter to proceed!

""")
            program()
program()

# Should never show unless a error happened

print("\n\n\n\n\n\n\n\n\n\nShutting down")

# End of program
