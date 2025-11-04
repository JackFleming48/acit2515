import abc
import enum
import json
import pathlib
import sys

from secret_word import HangmanWord, SecretWord, WordleWord


class GameState(enum.Enum):
    """Enumeration with three states: ACTIVE, WON, and LOST."""

    ACTIVE = 1
    WON = 2
    LOST = 3


class WordGame(abc.ABC):
    """The game class encapsulates the logic of word guessing game.  It allows
    the setting of a secret word and allows players guess the secret word.
    Only allowing the specified number of attempts.

    Class Attributes:
        _GUESS_PROMPT (str):
            prompt for user guess
        _GUESSES_REMIANING (str):
            prompt to tell user the remaining guesses
        _CORRECT_GUESS (str):
            prompt to tell user they guessed correctly
        _INCORRECT_GUESS (str):
            prompt to tell user they guessed incorrectly
        _OUT_OF_TURNS (str):
            prompt to inform user that they are out of turns
        _CLR_SCRN (str):
            terminal code that clears the screen
        RESTORE_FILE_PATH (pathlib.Path):
            file path for saving and restoring game state

    Attributes:
        _game_state (GameState): if the game is in progress, won, or lost
        _max_turns (int): maximum number of guesses or turns in the game
        _guesses (list[str]): user guesses of secret word
        _secret_word (SecretWord):
            subclass secret word object used to manage secret word.
    """

    # Strings for player prompts
    _GUESS_PROMPT = "Please Enter a Letter or Guess the word"
    _GUESSES_REMAINING = "Number of guesses remaining:"
    _CORRECT_GUESS = "You guessed the word\n"
    _INCORRECT_GUESS = "Incorrect guess\n"
    _OUT_OF_TURNS = "You are out of turns: game over\n"
    _CLR_SCRN = "\033[H\033[J"

    RESTORE_FILE_PATH: pathlib.Path = (
        pathlib.Path(__file__).parent.resolve() / "game_save.json"
    )

    @abc.abstractmethod
    def __init__(self, word: str | None, turns: int | None):
        """
        Initializes the game with a specified number of turns, secret word, and an
        empty list for guesses. If no word is supplied a random word is selected.

        Args:
          self:
            reference the current game object.
          turns:
            number of attempts to guess the word
          word:
            data to store in the _secret_word attribute
        """
        self._game_state = GameState.ACTIVE
        self._max_turns = turns
        self._guesses = []

    @property
    def game_state(self) -> GameState:
        return self._game_state

    @property
    def guesses(self) -> list[str]:
        return sorted(self._guesses)

    @property
    @abc.abstractmethod
    def secret_word(self) -> SecretWord:
        """
        Forces inheriting classes to create secret word for there usage
        message, showing secret word letters spaces, and a guess prompt.

        Returns:
          secret_word.SecretWord:
            object with be of subclass depending on game type
        """
        pass

    @secret_word.setter
    @abc.abstractmethod
    def secret_word(self, word: str):
        """
        Forces inheriting classes to create secret word and allow
        it to be set in the inheriting intialization function.

        This must set the self._secret_word attribute
        """
        pass

    @property
    def guesses_left(self):
        """
        Calculates the number of turns left based on the maximum turns allowed and the
        turns already taken.

        Returns:

        the number of turns remaining
        """

        return self._max_turns - len(self._guesses)

    @abc.abstractmethod
    def _format_prompt(self) -> str:
        """
        Create a subclass specific prompt based on the Game state
        """
        pass

    @abc.abstractmethod
    def guess(self, guess: str | None = None) -> str:
        """
        Handle the different cases for guesses in a word guessing game.

        Update _game_status and return user_prompt for next round

        Args:
          guess (str | none):
            a letter or word to be guessed

        Returns:
            str:
                prompt to be to user
        """

        pass

    def save(self):
        """
        Converts game state to a dictionary and saves it as JSON to RESTORE_FILE_PATH
        """

        # Convert to dictionary:
        data = {}
        data["class_name"] = self.__class__.__name__
        data["guesses"] = self._guesses
        data["max_turns"] = self._max_turns
        data["word"] = self.secret_word.word

        with open(self.RESTORE_FILE_PATH, "w") as restore_file:
            json.dump(data, restore_file, indent=4)

    @classmethod
    def restore(cls):
        """
        Creates a new game object from game state JSON in RESTORE_FILE_PATH
        """

        try:
            with open(cls.RESTORE_FILE_PATH, "r") as restore_file:
                data = json.load(restore_file)

        except FileNotFoundError:
            sys.exit(1)

        class_type = globals()[data["class_name"]]
        restored_game = class_type(data["word"], data["max_turns"])
        restored_game._guesses = data["guesses"]

        # remove old file
        pathlib.Path.unlink(cls.RESTORE_FILE_PATH)

        return restored_game


class WordleGame(WordGame):
    """The WordleGame class encapsulates the logic of a wordle game.  It allows
    the setting of a secret word and allows players guess secret word 5 times

    Class Attributes:
        _NUM_GUESSES (int): number of guesses in a wordle game
        _EMPTY_GUESS (str): representation of empty guess used to format prompt
        _GAME_START (str): greeting for new game prompt
        _GUESS_PROMPT (str): per guess prompt string

    Attributes:
        _game_state (GameState): if the game is in progress, won, or lost
        _max_turns (int): maximum number of guesses or turns in the game
        _guesses (list[str]): user guesses of secret word
        _secret_word(WordleWord):
            WordleWord object used to manage secret word.
    """

    # Strings for player prompts
    _NUM_GUESSES = 5
    _EMPTY_GUESS = "_____"
    _GAME_START = "\nWelcome to Wordle\n"
    _GUESS_PROMPT = "Enter a five letter word guess:\n"

    def __init__(self, word=None, turns=None):
        """
        Initializes the game with a specified number of turns, secret word, and an
        empty list for guesses. If no word is supplied a random word is selected.

        Args:
          self:
            reference the current game object.
          turns:
            number of attempts to guess the word
          word:
            The `SecretWord`
        """
        turns = self._NUM_GUESSES
        super().__init__(word, turns)
        self.secret_word = word

    @property
    def guesses(self) -> list[str]:
        """Overide to keep guesses in order"""
        return self._guesses

    @property
    def secret_word(self):
        return self._secret_word

    @secret_word.setter
    def secret_word(self, word):
        self._secret_word = WordleWord(word)

    def _guesses_box(self):
        box_display = ""

        # Create an ouput word box for each of the allowed gueses
        for word_box in range(0, self._NUM_GUESSES):
            if word_box < len(self._guesses):
                box_display += self._secret_word.show_letters(self._guesses[word_box])
                box_display += "\n"
            else:
                box_display += self._secret_word.show_letters(self._EMPTY_GUESS)
                box_display += "\n"

        return box_display

    def _format_prompt(self, word=None) -> str:
        """Create prompt for user for next step in game"""

        prompt = ""
        if len(self._guesses) == 0:  # No guesses intial prompt
            prompt = (
                self._CLR_SCRN
                + "\n"
                + self._GAME_START
                + f"{self._GUESSES_REMAINING} {self.guesses_left}\n"
                + self._guesses_box()
                + self._GUESS_PROMPT
            )
        else:  # not the first guess
            prompt = self._CLR_SCRN + "\n" + self._guesses_box()

            # Not an valid guess: None, "", or word that isn't 5 letters
            if (
                (word is None)
                or (word == "")
                or (len(word) != self._secret_word.WORD_LENGTH)
            ):
                prompt += (
                    f"{self._GUESSES_REMAINING} {self.guesses_left}\n"
                    + self._GUESS_PROMPT
                )

            elif self._secret_word.check(word):  # guessed the word
                prompt += f"{self._CORRECT_GUESS}\n"

            elif self.guesses_left > 0:  # unsuccessful guess and more guesses left
                prompt += (
                    f"{self._GUESSES_REMAINING} {self.guesses_left}\n"
                    + self._GUESS_PROMPT
                )

            else:  # unsuccessful guess and no guesses left: game over
                prompt += (
                    f"{self._OUT_OF_TURNS}"
                    + "Word: "
                    + self._secret_word.formatted_word
                )

        return prompt

    def guess(self, guess=None) -> str:
        """
        Handle the different cases for guessing letters or words in wordle game.
            - No Guess
            - Empty Guess
            - Word Guess

        Update game status and output accordingly.

        Args:
          guess:
            a word to be guessed

        Returns:
            str:
                output to be communicated to user
        """

        user_prompt = ""

        # A valid Worldle word was guessed
        if isinstance(guess, str) and len(guess) == self._secret_word.WORD_LENGTH:

            # add formatted guess to guesses
            self._guesses.append(guess.strip().upper())

            # The guess is the secret word, user wins
            if self._secret_word.check(guess):
                self._game_state = GameState.WON

            else:  # The guess is incorrect
                if self.guesses_left <= 0:  # No turns left, game over
                    self._game_state = GameState.LOST

            user_prompt = self._format_prompt(guess)

        else:  # No guess was provided or non five letter word was guessed
            user_prompt = self._format_prompt()

        return user_prompt

class HangmanGame(WordGame):
    """The Hangman class encapsulates the logic of a hangman game.  It allows
    the setting of a secret word and allows players guess letters or the secret word.
    Only allowing the specified number of attempts.
    """
    pass

