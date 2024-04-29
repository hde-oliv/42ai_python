import random


def main():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")

    answer = random.randint(0, 99)
    guess = 0
    tries = 0

    while guess != answer:
        user_input = input("What's your guess between 1 and 99?\n")

        if user_input == "exit":
            return print("Goodbye!")

        try:
            guess = int(user_input)
        except TypeError:
            print("That's not a number.")
            continue

        if not (0 < guess < 99):
            print("Number out of range.")
            continue

        tries += 1
        if guess > answer:
            print("Too high!")
            continue
        if guess < answer:
            print("Too low!")
            continue

    if answer == 42:
        print(
            "The answer to the ultimate question of life, the universe and everything is 42."
        )

    if tries == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print("Congratulations, you've got it!")
        print(f"You won in {tries} attempts!")


if __name__ == "__main__":
    main()
