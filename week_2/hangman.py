import random

def displayGame(game, letters, strikes, guess_list, word_to_guess, incorrect_guesses):
    while True:
        printGame(game, letters, strikes, guess_list)
        print(f"Incorrect guesses: {incorrect_guesses}")
        guess = input("Guess a letter:\n")

        if not isValid(guess):
            print("That input is not valid")
            continue

        if already_guessed(guess, guess_list):
            print("You already guessed that!")
            continue

        
        if inLetter(word_to_guess, guess):
            for i, letter in enumerate(word_to_guess): 
                if letter == guess:
                    letters[i] = guess
            guess_list = guesses(guess, guess_list)

        else:
            strikes+=1
            strikeCount(strikes, game)
            incorrect_guesses.append(guess)

            if strikes >= 7:
                strikeCount(strikes, game)
                print(f"Game Over!\nThe word was {''.join(word_to_guess)}")
                break



        if "_" not in letters:
            print(f"You Win!\nThe word was {''.join(word_to_guess)}")
            break

        
def already_guessed(guess, guess_list):
    if guess in guess_list:
        return True
    return False

def initializeGame():
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
    incorrect_guesses = []
    displayGame(game, letters, strikes, guess_list, word_to_guess, incorrect_guesses)

def word():
    words = []
    with open("words.txt") as f:
        for line in f:
            words.append(line.strip())

    word = random.choice(words)
    return list(word)

def guesses(guess, guess_list):
    guess_list.append(guess)
    return guess_list

def printGame(game, letters, strikes, guess_list):
    for x in game:
        print("".join(x))
    print(" ".join(letters))
    print(f"Strikes: {strikes}")


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
    initializeGame()