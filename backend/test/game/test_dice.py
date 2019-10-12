# import pytest
import backend.src.game.dice as dice


# First, we will see if it's returning back a value that we expect,
def test_roll():
    assert dice.roll() in dice.DICE_VALUES


# After that, we can test to ensure that we're getting random stuff back.

# I'll test to ensure that two different sets of 10 rolls are not identical.
# For this to happen by chance is infinitesimal.
def test_multiple_rolls():
    first_set = dice.rolls(10)
    second_set = dice.rolls(10)
    assert not all(
        [first_set[i] == second_set[i] for i in range(len(first_set))])
