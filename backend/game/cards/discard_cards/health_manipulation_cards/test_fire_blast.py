from game.cards.discard_cards.health_manipulation_cards.fire_blast import FireBlast
from game.values import constants


def test_fire_blast_subtracts_2_health(player, five_players):
    FireBlast().immediate_effect(player, five_players)
    assert all(other_players.current_health == constants.DEFAULT_HEALTH - 2
               for other_players in five_players)


def test_fire_blast_costs_3_energy():
    assert FireBlast().cost == 3


def test_type_is_discard():
    assert FireBlast().card_type == "Discard"
