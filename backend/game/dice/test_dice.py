import game.dice.dice as dice

def test_roll():
    assert dice.roll() in dice.DieValue