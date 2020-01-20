import pytest

from game.irepository.irepository_player import IRepositoryPlayer
from game.player.player import Player


@pytest.mark.django_db(transaction=True)
def test_irepository_player():
    irepositoryplayer = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla')
    player.set_username('Test')
    player.set_password('Test')
    irepositoryplayer.save_player_db(player)
