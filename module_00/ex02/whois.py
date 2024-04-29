import sys


def main():
    if len(sys.argv) == 1:
        return

    if len(sys.argv) != 2:
        print("AssertionError: more than one argument provided")

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return

    if number == 0:
        print("I'm Zero.")
    else:
        responses = ["Even", "Odd"]
        print(f"I'm {responses[number % 2]}.")


if __name__ == "__main__":
    main()
