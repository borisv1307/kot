from backend.src.game.newcards.discard_cards.victory_point_manipulation_cards.apartment_building import \
    ApartmentBuilding


def test_apartment_building_adds_3_victory_points(player):
    ApartmentBuilding().immediate_effect(player, None)
    assert player.victory_points == 3


def test_apartment_building_costs_5_energy():
    assert ApartmentBuilding().cost == 5


def test_apartment_building_has_effect():
    effect = ApartmentBuilding().effect
    assert effect and not effect.isspace()


def test_apartment_building_has_no_footnote():
    assert False
