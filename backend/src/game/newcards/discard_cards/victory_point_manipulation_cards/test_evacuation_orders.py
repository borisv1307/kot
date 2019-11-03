from backend.src.game.newcards.discard_cards.victory_point_manipulation_cards.evacuation_orders import \
    EvacuationOrders


def test_evacuation_orders_subtracts_5_victory_points(five_players):
    for player in five_players:
        player.update_victory_points_by(10)
    EvacuationOrders().immediate_effect(None, five_players)
    assert all(other_players.victory_points ==
               5 for other_players in five_players)


def test_apartment_building_costs_7_energy():
    assert EvacuationOrders().cost == 7
