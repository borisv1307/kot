from backend.src.game.newcards.discard_cards.victory_point_manipulation_cards.commuter_train import CommuterTrain


def test_commuter_train_adds_2_victory_points(player):
    CommuterTrain().immediate_effect(player, None)
    assert player.victory_points == 2


def test_commuter_train_costs_4_energy():
    assert CommuterTrain().cost == 4


def test_commuter_train_has_effect():
    effect = CommuterTrain().effect
    assert effect and not effect.isspace()


def test_commuter_train_has_no_footnote():
    assert not CommuterTrain().footnote
