from game.cards.keep_cards.victory_point_manipulation_cards.eater_of_the_dead import EaterOfTheDead
from game.engine.board import BoardGame
from game.player.player import Player


def test_eater_of_the_dead_player_add_card(player):
    EaterOfTheDead().immediate_effect(player, None)
    assert player.has_instance_of_card(EaterOfTheDead())


def test_eater_of_the_dead_costs_4_energy():
    assert EaterOfTheDead().cost == 4


def test_complicated_eater_logic():
    card_holder = Player()
    card_holder.add_card(EaterOfTheDead())
    playerA = Player()
    playerB = Player()
    playerC = Player()

    game = BoardGame()
    game.add_player(card_holder)
    game.add_player(playerA)
    game.add_player(playerB)
    game.add_player(playerC)
    game.start_game()
    playerA.update_health_by(-playerA.current_health)
    game.players.apply_eater_of_dead_action()
    assert card_holder.victory_points == EaterOfTheDead.victory_points_reward_value

    playerB.update_health_by(-playerB.current_health)
    playerC.update_health_by(-playerC.current_health)
    game.players.apply_eater_of_dead_action()
    assert card_holder.victory_points == EaterOfTheDead.victory_points_reward_value * 3
