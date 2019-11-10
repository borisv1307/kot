from game.cards.discard_cards.victory_point_manipulation_cards.high_altitude_bombing import HighAltitudeBombing


def test_high_altitude_bombing_subtracts_3_health(player):
    player.update_health_by(10)
    HighAltitudeBombing().immediate_effect(player, None)
    assert player.current_health == 7


def test_high_altitude_bombing_subtracts_3_health_other_players(five_players):
    for player in five_players:
        player.update_health_by(10)
    HighAltitudeBombing().immediate_effect(None, five_players)
    assert all(other_players.current_health ==
               7 for other_players in five_players)


def test_high_altitude_bombing_costs_4_energy():
    assert HighAltitudeBombing().cost == 4
