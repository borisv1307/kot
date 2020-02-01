import pytest

from game.irepository.irepository_play import IRepositoryPlay
from game.irepository.irepository_player import IRepositoryPlayer
from game.player.player import Player
from game.cards.card import Card
from game.values.locations import Locations


@pytest.mark.django_db(transaction=True)
def test_save_play():
    repository_play = IRepositoryPlay()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    player.set_password('Pass')
    repository_player.save_player_db(player)
    card = Card("Drop from High Altitude", 8, "+ 9[Energy]", "")
    player.add_card(card)
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    repository_play.save_play_db(player)
    assert repository_play.get_play_db(player).location == 'Locations.TOKYO'


@pytest.mark.django_db(transaction=True)
def test_get_play():
    repository_play = IRepositoryPlay()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    player.set_password('Pass')
    repository_player.save_player_db(player)
    card = Card("Drop from High Altitude", 8, "+ 9[Energy]", "")
    player.add_card(card)
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    repository_play.save_play_db(player)
    assert repository_play.get_play_db(player).victory_points == 2


@pytest.mark.django_db(transaction=True)
def test_update_play():
    repository_play = IRepositoryPlay()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    player.set_password('Pass')
    repository_player.save_player_db(player)
    card = Card("Drop from High Altitude", 8, "+ 9[Energy]", "")
    player.add_card(card)
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    repository_play.save_play_db(player)
    card = Card("Fire Blast", 3, "All other monsters - 2[health]", "")
    player.add_card(card)
    player.leave_tokyo()
    player.update_victory_points_by(1)
    player.update_energy_by(1)
    player.update_health_by(-1)
    assert repository_play.get_play_db(player).victory_points == 2


@pytest.mark.django_db(transaction=True)
def test_delete_dice():
    repository_play = IRepositoryPlay()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    player.set_password('Pass')
    repository_player.save_player_db(player)
    card = Card("Drop from High Altitude", 8, "+ 9[Energy]", "")
    player.add_card(card)
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    repository_play.save_play_db(player)
    assert repository_play.delete_play_db(player) is None
