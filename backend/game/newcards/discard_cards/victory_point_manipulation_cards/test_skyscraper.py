from game.newcards.discard_cards.victory_point_manipulation_cards.skyscraper import \
    Skyscraper


def test_skyscraper_adds_4_victory_points(player):
    Skyscraper().immediate_effect(player, None)
    assert player.victory_points == 4


def test_apartment_building_costs_6_energy():
    assert Skyscraper().cost == 6