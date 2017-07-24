import random

title = "Roll The Dice"
width = len(title) * 3
space = width / 3


def main():
    print_header()
    roll()


def print_header():
    print("=" * width)
    print(" " * int(space), title)
    print("=" * width)
    print()


def roll():
    user_input = 0

    while user_input != "n":
        user_input = input("Roll The Dice of Destiny [Y]es,[No]?")
        user_input = user_input.lower().strip()
        throws = 0

        if user_input == "y":
            user = input("How many times would you like to roll?")
            rolls = int(user)

            for i in range(rolls):
                dice = random.randint(1, 6)
                throws = throws + 1

                print("Roll", throws, "=", dice)
                
        else:
            print("The Dice Of Destiny Have Rolled For The Last Time, Let The Odds Be Ever In Your Favour")


if __name__ == '__main__':
    main()
