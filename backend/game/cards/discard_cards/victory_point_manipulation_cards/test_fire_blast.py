from game.cards.discard_cards.victory_point_manipulation_cards.fire_blast import FireBlast


def test_fire_blast_subtracts_2_health(player, five_players):
    for other_players in five_players:
        other_players.update_health_by(12)
    FireBlast().immediate_effect(player, five_players)
    assert all(other_players.current_health == 10
               for other_players in five_players)


def test_fire_blast_costs_3_energy():
    assert FireBlast().cost == 3
