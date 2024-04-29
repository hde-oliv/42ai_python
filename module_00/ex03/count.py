import sys
import string


def text_analyzer(text=None):
    """
    This function counts the number of upper, lower characters, punctuation
    and spaces in a given text.
    """

    if text is None:
        text = input("Insert string:")

    if not isinstance(text, str):
        print("ValueError: not a string")
        return

    ispunc = lambda x: x in string.punctuation

    print(f"The text contains {len(text)} character(s):")
    print(f"- {len(list(filter(str.isupper, text)))} upper letter(s)")
    print(f"- {len(list(filter(str.islower, text)))} lower letter(s)")
    print(f"- {len(list(filter(ispunc, text)))} punctuation mark(s)")
    print(f"- {len(list(filter(str.isspace, text)))} space(s)")


def main():
    if len(sys.argv) > 2:
        print("error: too much arguments")
        return

    try:
        text_analyzer(sys.argv[1])
    except:
        text_analyzer()


if __name__ == "__main__":
    main()
