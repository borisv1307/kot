import pytest

from game.irepository.irepository_game import IRepositoryGame
from game.irepository.irepository_player import IRepositoryPlayer
from game.player.player import Player


@pytest.mark.django_db(transaction=True)
def test_save_player_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room1')
    assert repository_player.save_player('The King', 'Room1').id == 1


@pytest.mark.django_db(transaction=True)
def test_get_player_by_id_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room2')
    repository_player.save_player('Giga Zaur', 'Room2')
    assert repository_player.get_player_by_id(2).username == 'Giga Zaur'


@pytest.mark.django_db(transaction=True)
def test_get_players_by_username_and_room_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room3')
    repository_player.save_player('Alienoid', 'Room3')
    assert repository_player.get_players_by_username_and_room('Alienoid', 'Room3').username == 'Alienoid'


@pytest.mark.django_db(transaction=True)
def test_update_player_username_by_id_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room4')
    repository_player.save_player('Meka Dragon', 'Room4')
    repository_player.update_player_username_by_id(4, 'Kong')
    assert repository_player.get_player_by_id(4).username == 'Kong'


@pytest.mark.django_db(transaction=True)
def test_update_player_username_by_username_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room5')
    repository_player.save_player('Godzilla', 'Room5')
    repository_player.update_player_username_by_username('Godzilla', 'Mantra')
    assert repository_player.get_players_by_username_and_room('Mantra', 'Room5').username == 'Mantra'


@pytest.mark.django_db(transaction=True)
def test_update_player_monster_name_by_id_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room6')
    repository_player.save_player('Kraken', 'Room6')
    repository_player.update_player_monster_name_by_id(6, 'Cyber Bunny')
    assert repository_player.get_player_by_id(6).monster_name == 'Cyber Bunny'


@pytest.mark.django_db(transaction=True)
def test_update_player_monster_name_by_username_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room7')
    repository_player.save_player('Hydra', 'Room7')
    repository_player.update_player_monster_name_by_username('Hydra', 'Mantis')
    assert repository_player.get_players_by_username_and_room('Hydra', 'Room7').monster_name == 'Mantis'


@pytest.mark.django_db(transaction=True)
def test_delete_player_by_user_id_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room8')
    repository_player.save_player('Space Penguin', 'Room8')
    assert repository_player.delete_player_by_id(8) is None


@pytest.mark.django_db(transaction=True)
def test_delete_player_by_user_id_db():
    repository_player = IRepositoryPlayer()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room9')
    repository_player.save_player('Alpha Zombie', 'Room9')
    assert repository_player.delete_player_by_username('Alpha Zombie') is None
