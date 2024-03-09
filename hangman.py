from random import choice


def main():
    word = random()
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


def random():
    word_list = [
        "breakfast",
        "commute",
        "exercise",
        "laundry",
        "cleaning",
        "hygiene",
        "shopping",
        "cooking",
        "dinner",
        "sleeping",
        "homework",
        "gardening",
        "meditation",
        "relaxing",
        "internet",
        "friendship",
        "education",
        "happiness",
        "celebrate",
        "memories",
        "vacation",
        "festival",
        "routine",
        "chores",
        "traffic",
        "research",
        "learning",
        "adventure",
        "playlist",
        "exercise",
        "recreation",
        "nutrition",
        "breakfast",
        "lunchbox",
        "organize",
        "ambition",
        "happiness",
        "curiosity",
        "adventure",
        "happiness",
        "volunteer",
        "community",
        "exercise",
        "adventure",
        "creativity",
        "happiness",
        "reflection",
        "inspiration",
        "gratitude",
        "friendship",
    ]
    return choice(word_list)


if __name__ == "__main__":
    main()
