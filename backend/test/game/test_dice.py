import backend.src.game.dice.dice as dice


def test_roll():
    assert dice.roll() in dice.DieValue


def test_rolls():
    roll = dice.roll_many(2)
    assert roll.count == 2
