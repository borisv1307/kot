import game.turn_actions.attack as attack_actions
from game.cards.keep_cards.attack_manipulation_cards.nova_breath import NovaBreath
from game.player.player import Player


def test_if_attackable_in_same_locations():
    player_one = Player()
    player_two = Player()
    assert not attack_actions.is_attackable(player_one, player_two)


def test_if_attackable_in_different_locations():
    player_one = Player()
    player_two = Player()
    player_two.move_to_tokyo()
    assert attack_actions.is_attackable(player_one, player_two)


def test_gets_all_attackable_players_in_different_location():
    attack_player = Player()
    player_two = Player()
    player_three = Player()
    player_four = Player()
    player_two.move_to_tokyo()
    player_four.move_to_tokyo()
    possible_players = [player_two, player_three, player_four]
    attackable_players = attack_actions.get_attackable_players(
        attack_player, possible_players)
    assert attackable_players == [player_two, player_four]


def test_attack_all_players_if_attacker_has_nova_breath():
    attack_player = Player()
    player_two = Player()
    player_three = Player()
    player_four = Player()
    player_two.move_to_tokyo()
    player_four.move_to_tokyo()
    possible_players = [player_two, player_three, player_four]
    attack_player.add_card(NovaBreath())
    attackable_players = attack_actions.get_attackable_players(
        attack_player, possible_players)
    assert attackable_players == possible_players


def test_attacking_players_by_three():
    player_two = Player()
    player_three = Player()
    attackable_players = [player_two, player_three]
    attack_actions.attack_players(Player(), attackable_players, 3)
    assert player_two.current_health == 7 and player_three.current_health == 7


def test_player_allowed_to_yield_after_attacked_in_tokyo():
    attacker = Player()
    attacker.leave_tokyo()
    yielder = Player()
    yielder.move_to_tokyo()
    attack_actions.attack_players(attacker, [yielder])
    assert yielder.allowed_to_yield
    assert not attacker.allowed_to_yield


def test_player_not_allowed_to_yield_after_attacked_out_of_tokyo():
    attacker = Player()
    attacker.move_to_tokyo()
    yielder = Player()
    yielder.leave_tokyo()
    attack_actions.attack_players(attacker, [yielder])
    assert not yielder.allowed_to_yield
    assert not attacker.allowed_to_yield
