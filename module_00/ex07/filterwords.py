import sys
import string


def main():
    if len(sys.argv) != 3:
        print("error: wrong number of arguments")
        return

    try:
        phrase = str(sys.argv[1])
        number = int(sys.argv[2])
    except ValueError:
        print("error: invalid argument type")
        return

    ispunc = lambda x: x in string.punctuation

    def count(word):
        result = 0
        for c in word:
            if not ispunc(c):
                result += 1
        return result

    def clear(word):
        new_word = []
        for c in word:
            if not ispunc(c):
                new_word.append(c)
        return "".join(new_word)

    words = phrase.split(" ")
    result = [word for word in words if count(word) > number]
    result = [clear(word) for word in result]

    print(result)


if __name__ == "__main__":
    main()
