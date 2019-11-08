from game.newcards.discard_cards.victory_point_manipulation_cards.gas_refinery import \
    GasRefinery


def test_gas_refinery_costs_6_energy():
    assert GasRefinery().cost == 6


def test_gas_refinery_adds_2_victory_points(player, five_players):
    GasRefinery().immediate_effect(player, five_players)
    assert player.victory_points == 2


def test_gas_refinery_subtracts_3_health(player, five_players):
    GasRefinery().immediate_effect(player, five_players)
    assert all(other_players.current_health ==
               7 for other_players in five_players)