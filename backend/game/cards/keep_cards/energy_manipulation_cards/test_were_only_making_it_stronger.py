from game.cards.keep_cards.energy_manipulation_cards.were_only_making_it_stronger import WereOnlyMakingItStronger


def test_were_only_making_it_stronger_player_add_card(player):
    WereOnlyMakingItStronger().immediate_effect(player, None)
    assert player.has_instance_of_card(WereOnlyMakingItStronger())


def test_were_only_making_it_stronger_costs_3_energy():
    assert WereOnlyMakingItStronger().cost == 3


def test_energy_hoarder_gain_1_energy_when_health_reduced_by_three(player):
    player.add_card(WereOnlyMakingItStronger())
    player.update_health_by(-3)
    assert player.energy == 1


def test_energy_hoarder_gain_0_energy_when_health_reduced_by_one(player):
    player.add_card(WereOnlyMakingItStronger())
    player.update_health_by(-1)
    assert player.energy == 0
