from game.cards.keep_cards.health_manipulation_cards.armor_plating import ArmorPlating
from game.player.player import Player


def test_lose_no_health_when_hurt_one_health_point(player):
    health_change = -1
    current_health = 3
    player.current_health = current_health
    player.add_card(ArmorPlating())
    player.update_health_by(health_change)
    assert player.current_health == current_health
