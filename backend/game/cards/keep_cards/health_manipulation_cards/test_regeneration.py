from game.cards.keep_cards.health_manipulation_cards.regeneration import Regeneration
from game.player.player import Player


def test_add_one_extra_health_when_have_regeneration_card(player):
    health_increase = 3
    current_health = 3
    player.current_health = current_health
    player.add_card(Regeneration())
    player.update_health_by(health_increase)
    assert player.current_health == current_health + health_increase + 1
