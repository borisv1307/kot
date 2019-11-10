from game.cards.discard_cards.victory_point_manipulation_cards.commuter_train import CommuterTrain


def test_commuter_train_adds_2_victory_points(player):
    CommuterTrain().immediate_effect(player, None)
    assert player.victory_points == 2


def test_commuter_train_costs_4_energy():
    assert CommuterTrain().cost == 4
