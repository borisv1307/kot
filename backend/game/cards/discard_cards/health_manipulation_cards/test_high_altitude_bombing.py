from game.cards.discard_cards.health_manipulation_cards.high_altitude_bombing import HighAltitudeBombing


def test_high_altitude_bombing_subtracts_3_health(player, five_players):
    HighAltitudeBombing().immediate_effect(player, five_players)
    assert player.current_health == 7


def test_high_altitude_bombing_subtracts_3_health_other_players(player, five_players):
    HighAltitudeBombing().immediate_effect(player, five_players)
    assert all(other_players.current_health ==
               7 for other_players in five_players)


def test_high_altitude_bombing_costs_4_energy():
    assert HighAltitudeBombing().cost == 4
