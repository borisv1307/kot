import pytest

from game.irepository.irepository_game import IRepositoryGame
from game.irepository.irepository_player import IRepositoryPlayer
from game.player.player import Player


@pytest.mark.django_db(transaction=True)
def test_save_player_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room1')
    player = Player()
    player.set_monster_name('The King')
    player.set_username('The King')
    assert repository_player.save_player(player, 'Room1').id == 1


@pytest.mark.django_db(transaction=True)
def test_get_player_by_id_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room2')
    player = Player()
    player.set_monster_name('Giga Zaur')
    player.set_username('Giga Zaur')
    repository_player.save_player(player, 'Room2')
    assert repository_player.get_player_by_id(2).monster_name == 'Giga Zaur'


@pytest.mark.django_db(transaction=True)
def test_get_players_by_player_and_room_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room3')
    player = Player()
    player.set_monster_name('Alienoid')
    player.set_username('Alienoid')
    repository_player.save_player(player, 'Room3')
    assert repository_player.get_players_by_player_and_room(player, 'Room3').monster_name == 'Alienoid'


@pytest.mark.django_db(transaction=True)
def test_update_player_username_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room4')
    player1 = Player()
    player1.set_monster_name('Meka Dragon')
    player1.set_username('Meka Dragon')
    repository_player.save_player(player1, 'Room4')
    repository_player.update_player_username('Kong', 4)
    assert repository_player.get_player_by_id(4).username == 'Kong'


@pytest.mark.django_db(transaction=True)
def test_update_player_monster_name_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room5')
    player1 = Player()
    player1.set_monster_name('Kraken')
    player1.set_username('Kraken')
    repository_player.save_player(player1, 'Room5')
    repository_player.update_player_monster_name('Cyber Bunny', 5)
    assert repository_player.get_player_by_id(5).monster_name == 'Cyber Bunny'


@pytest.mark.django_db(transaction=True)
def test_delete_player_by_user_id_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room6')
    player = Player()
    player.set_monster_name('Space Penguin')
    player.set_username('Space Penguin')
    repository_player.save_player(player, 'Room6')
    assert repository_player.delete_player_by_id(6) is None
