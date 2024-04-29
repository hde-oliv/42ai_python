import sys


def main():
    if len(sys.argv) == 1:
        return

    result = " ".join(sys.argv[1:]).swapcase()[::-1]
    print(result)


if __name__ == "__main__":
    main()
