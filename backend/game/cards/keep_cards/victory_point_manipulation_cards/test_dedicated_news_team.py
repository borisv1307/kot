from game.cards.discard_cards.health_manipulation_cards.heal import Heal
from game.cards.keep_cards.victory_point_manipulation_cards.dedicated_news_team import DedicatedNewsTeam

from game.deck.deck_handler import DeckHandler
from game.player.player import Player


def test_dedicated_news_team_player_add_card(player):
    DedicatedNewsTeam().immediate_effect(player, None)
    assert player.has_instance_of_card(DedicatedNewsTeam())


def test_eater_of_the_dead_costs_3_energy():
    assert DedicatedNewsTeam().cost == 3


def test_dedicated_news_team_player_buys_card(player):
    player.energy = 100
    deck_handler = DeckHandler()

    # Force the card this test will buy to be Heal since it doesn't affect victory points
    deck_handler.store.clear()
    deck_handler.store.append(Heal())

    original_victory_points = player.victory_points
    DedicatedNewsTeam().immediate_effect(player, None)
    
    deck_handler.buy_card_from_store(0, player, [Player(), Player()])
    assert player.victory_points == original_victory_points + 1
