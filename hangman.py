from random import choice
from hangmanwords import randomword


def main():
    word = randomword()
    blank = []
    numbers = []
    lives = ["❤️", "❤️", "❤️", "❤️", "❤️", "❤️", "❤️"]

    for _ in range(len(word)):
        blank.append("_")
    for i in blank:
        print(i + " ", end="")
    print()

    while True:
        count = -1
        if "❤️" not in lives:
            print("You lose!")
            print("The word is", word)
            break

        for heart in lives:
            print(heart, end="")
        print()

        while True:
            try:
                x = input("Character: ").lower()
                if len(x) == 1 and x.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                pass

        if x in word:
            for j in word:
                count += 1
                if x == j:
                    numbers.append(count)
                    blank[count] = x
        else:
            for live in range(len(lives)):
                if lives[live] == "❤️":
                    lives[live] = ""
                    break

        for i in blank:
            print(i + " ", end="")
        print()

        if "_" not in blank:
            print("You win!")
            print("The word is", word)
            break


if __name__ == "__main__":
    main()
