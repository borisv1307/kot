from game.newcards.discard_cards.victory_point_manipulation_cards.frenzy import Frenzy


def test_frenzy_costs_7_energy():
    assert Frenzy().cost == 7
