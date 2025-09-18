import random

def word():
    words = []
    with open("words.txt") as f:
        for line in f:
            words.append(line.strip())

    word = random.choice(words)
    return list(word)


print(word())