import sys


def operations(num1: int, num2: int):
    print("Sum:        ", num1 + num2)
    print("Difference: ", num1 - num2)
    print("Product:    ", num1 * num2)

    try:
        print("Quotient:   ", num1 / num2)
        print("Remainder:  ", num1 % num2)
    except ZeroDivisionError:
        print("Quotient:    ERROR (division by zero)")
        print("Remainder:   ERROR (modulo by zero)")


def main():
    if len(sys.argv) != 3:
        print("error: invalid number of arguments")
        return

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("error: argument not an integer")
        return

    operations(num1, num2)


if __name__ == "__main__":
    main()
