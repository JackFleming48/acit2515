import random

def initialize_game():
    game = [
        ["|", "-", "-", " "],
        ["|", " ", "|", " "],
        ["|", " ", " ", " "],
        ["|", " ", " ", " "],
        ["|", " ", " ", " "],
        ["|", " ", " ", " "],
        ["|", " ", " ", " "],
        ["_", " ", " ", " "]
    ]
    
    word_to_guess = word()
    letters = ["_","_","_","_","_"]
    strikes = 0
    guess_list = []

def word():
    words = []
    with open("words.txt") as f:
        for line in f:
            words.append(line.strip())

    word = random.choice(words)
    return list(word)

def isValid(guess):
    return guess.isalpha() and len(guess) == 1

def inLetter(word, guess):
    for y in word:
        if guess == y:
            return True
    return False

def strikeCount(strikes, game):
    if strikes == 1:
        game[2][2] = "O"
        return game
    if strikes == 2:
        game[3][2] = "|"
        return game
    if strikes == 3:
        game[3][1] = "/"
        return game
    if strikes == 4:
        game[3][3] = "\\"
        return game                
    if strikes == 5:
        game[4][2] = "|"
        return game
    if strikes == 6:
        game[5][1] = "/"
        return game
    if strikes == 7:
        game[5][3] = "\\"
        return game
    
if __name__ == "__main__":
    initialize_game()