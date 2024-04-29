import sys
import string

morse_letters = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
]

morse_numbers = [
    "-----",
    ".----",
    "..---",
    "...--",
    "....-",
    ".....",
    "-....",
    "--...",
    "---..",
    "----.",
]


def main():
    if len(sys.argv) == 1:
        return

    phrase = " ".join(sys.argv[1:])
    phrase = phrase.lower()

    letters_map = dict(zip(string.ascii_lowercase, morse_letters))
    numbers_map = dict(zip(string.digits, morse_numbers))
    space_map = {" ": "/"}

    morse_map = dict(letters_map, **numbers_map)
    morse_map.update(space_map)

    try:
        [print(morse_map[c], end=" ") for c in phrase]
    except KeyError:
        pass

    print("")


if __name__ == "__main__":
    main()
