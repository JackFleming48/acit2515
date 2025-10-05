import random

class Hangman:

    def __init__(self, word):
        self.word = list(word)
        self.game_board = [
            ["|", "-", "-", " "],
            ["|", " ", "|", " "],
            ["|", " ", " ", " "],
            ["|", " ", " ", " "],
            ["|", " ", " ", " "],
            ["|", " ", " ", " "],
            ["|", " ", " ", " "],
            ["_", " ", " ", " "],
        ]
        self.strikes = 0
        self.correct_display = ["_"] * len(word)
        self.guess_list = []
        self.incorrect_guesses = []
        self.game_is_lost = False
        self.game_is_won = False

    def run(self):
        while not self.game_is_lost and not self.game_is_won:
            self.drawMan()
            self.display()
            letter = self.guess()
            self.guess_in_word(letter)
            self.game_lost()
            self.game_won()

    def guess_in_word(self, letter):
        if not self.duplicate_guess(letter):
            if letter in self.word:
                for i, l in enumerate(self.word):
                    if letter == l:
                        self.correct_display[i] = letter
            else:
                self.strikes += 1
                self.incorrect_guesses.append(letter)
        else:
            print("You already guessed that!")


    def display(self):
        for x in self.game_board:
            print("".join(x))
        print(f"Strikes: {self.strikes}/7")
        print(f"Incorrect guesses: {' '.join(self.incorrect_guesses)}")
        print(f"{" ".join(self.correct_display)}")

    def game_won(self):
        if "_" not in self.correct_display:
            self.game_is_won = True
        if self.game_is_won:
            print("Congratulations you won!")


    def game_lost(self):
        if self.strikes >= 7:
            self.game_is_lost = True
        if self.game_is_lost:
            print(f"Game over, you lose!\nThe word was: {''.join(self.word)}")
    
    def guess(self):
        user_guess = input("Guess a letter:\n").lower()
        if not user_guess.isalpha():
            raise TypeError
        elif not len(user_guess) == 1:
            raise Exception("Guess needs to be 1 char")
        else:
            return user_guess
        
    def drawMan(self):
        if self.strikes == 1:
            self.game_board[2][2] = "O"
        elif self.strikes == 2:
            self.game_board[3][2] = "|"
        elif self.strikes == 3:
            self.game_board[3][1] = "/"
        elif self.strikes == 4:
            self.game_board[3][3] = "\\"              
        elif self.strikes == 5:
            self.game_board[4][2] = "|"
        elif self.strikes == 6:
            self.game_board[5][1] = "/"
        elif self.strikes == 7:
            self.game_board[5][3] = "\\"


    def duplicate_guess(self, letter):
        return letter in self.incorrect_guesses or letter in self.correct_display

    


def word():
    ans = []
    with open("words.txt", "r") as f:
        for line in f:
            ans.append(line.strip())
    return random.choice(ans)


def main():
    game = Hangman(word())
    game.run()



if __name__ == "__main__":
    main()