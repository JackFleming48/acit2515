from hangman import isValid, already_guessed, guesses
import pytest

@pytest.mark.parametrize("guess, expected", [
    ("a", True),
    ("ab", False),
    ("Z", True),
    ("1", False),
    ("", False),
    ("!", False)

])
def test_isValid(guess, expected):
    assert isValid(guess) is expected

@pytest.mark.parametrize("guess, guess_list, expected", [
    ("a", ["a"], True),
    ("a", ["b"], False),
    ("a", ["b", "c", "a"], True)
])
def test_already_guessed(guess, guess_list, expected):
    assert already_guessed(guess, guess_list) is expected


@pytest.mark.parametrize("guess, guess_list, expected", [
    ("a", [], ["a"]),
    ("b", ["z"], ["z", "b"])
])
def test_guesses(guess, guess_list, expected):
    guess_list = list(guess_list)
    assert guesses(guess, guess_list) == expected