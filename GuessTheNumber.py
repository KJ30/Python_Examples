import random

# Random number from 1 - 100
number = random.randint(1, 100)
title = "Guess The Number Game"
width = len(title) * 3
middle = int(width / 3)


def main():
    print_header()
    guess_random()


# print header

def print_header():
    print("=" * width)
    print(" " * middle, title.upper())
    print("=" * width)
    print()


# Loop through attempts until guess is correct

def guess_random():
    guess = 0
    while guess != number:
        user_input = input("Guess a number from 1 - 10:")
        guess = int(user_input)
        if guess > number:
            print("Too high")
        elif guess < number:
            print("To Low")
        else:
            print("Well Done , You win")


if __name__ == '__main__':
    main()
