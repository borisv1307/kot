from game.newcards.discard_cards.victory_point_manipulation_cards.fire_blast import FireBlast


def test_fire_blast_subtracts_2_health(five_players):
    for player in five_players:
        player.update_health_by(10)
    FireBlast().immediate_effect(None, five_players)
    assert all(other_players.current_health ==
               8 for other_players in five_players)


def test_fire_blast_costs_3_energy():
    assert FireBlast().cost == 3
