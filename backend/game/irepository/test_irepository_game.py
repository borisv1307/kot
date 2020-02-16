import pytest
from game.irepository.irepository_game import IRepositoryGame


@pytest.mark.django_db(transaction=True)
def test_save_game():
    repository_game = IRepositoryGame()
    assert repository_game.save_game('Room1') == 1


@pytest.mark.django_db(transaction=True)
def test_get_game_by_id():
    repository_game = IRepositoryGame()
    repository_game.save_game('Room2')
    assert repository_game.get_game_by_id(2).room_name == 'Room2'


@pytest.mark.django_db(transaction=True)
def test_get_all_games():
    repository_game = IRepositoryGame()
    repository_game.save_game('Room3')
    repository_game.save_game('Room4')
    assert repository_game.get_game_by_id(3).room_name == 'Room3'
    assert repository_game.get_game_by_id(4).room_name == 'Room4'


@pytest.mark.django_db(transaction=True)
def test_update_game_status_by_id():
    repository_game = IRepositoryGame()
    repository_game.save_game('Room5')
    repository_game.update_game_status_by_id(5, '1')
    assert repository_game.get_game_by_id(5).game_status == '1'


@pytest.mark.django_db(transaction=True)
def test_update_game_winners_by_id():
    repository_game = IRepositoryGame()
    repository_game.save_game('Room6')
    repository_game.update_game_winners_by_id(6, 1, 2, 3, 4, 5, 6)
    assert repository_game.get_game_by_id(6).second_winner == 2


@pytest.mark.django_db(transaction=True)
def test_delete_game_by_id():
    repository_game = IRepositoryGame()
    repository_game.save_game('Room7')
    assert repository_game.delete_game_by_id(7) is None
