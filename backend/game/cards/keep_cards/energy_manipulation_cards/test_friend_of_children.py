from game.cards.keep_cards.energy_manipulation_cards.friend_of_children import FriendOfChildren


def test_friend_of_children_player_add_card(player):
    FriendOfChildren().immediate_effect(player, None)
    assert player.has_instance_of_card(FriendOfChildren())


def test_friend_of_childrencosts_3_energy():
    assert FriendOfChildren().cost == 3


def test_friend_of_children_gain_1_extra_energy(player):
    player.add_card(FriendOfChildren())
    player.update_energy_by(3)
    assert player.energy == 4


def test_friend_of_children_gain_no_extra_energy(player):
    player.energy = 5
    player.add_card(FriendOfChildren())
    player.update_energy_by(0)
    assert player.energy == 5
