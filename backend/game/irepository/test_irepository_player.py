import pytest

from game.irepository.irepository_player import IRepositoryPlayer
from game.player.player import Player


@pytest.mark.django_db(transaction=True)
def test_save_player():
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla')
    player.set_username('Test_Save')
    repository_player.save_player_db(player)
    assert repository_player.get_player_db(player).username == 'Test_Save'


@pytest.mark.django_db(transaction=True)
def test_get_player():
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player_db(player)
    assert repository_player.get_player_db(player).username == 'Test_Get'


@pytest.mark.django_db(transaction=True)
def test_update_player():
    repository_player = IRepositoryPlayer()
    player1 = Player()
    player1.set_monster_name('Godzilla2')
    player1.set_username('Test_Update1')
    repository_player.save_player_db(player1)
    player2 = Player()
    player2.set_monster_name('Godzilla2')
    player2.set_username('Test_Update2')
    repository_player.update_player_db(player2)
    assert repository_player.get_player_db(player2).username == 'Test_Update2'


@pytest.mark.django_db(transaction=True)
def test_delete_player():
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla3')
    player.set_username('Test_Delete')
    repository_player.save_player_db(player)
    assert repository_player.delete_player_db(player) is None
