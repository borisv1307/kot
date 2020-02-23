import pytest

from game.irepository.irepository_game import IRepositoryGame


@pytest.mark.django_db(transaction=True)
def test_save_game():
    repository_game = IRepositoryGame()
    assert repository_game.save_game('Room1').id == 1


@pytest.mark.django_db(transaction=True)
def test_get_game_by_id():
    repository_game = IRepositoryGame()
    repository_game.save_game('Room2')
    assert repository_game.get_game_by_id(2).room_name == 'Room2'


@pytest.mark.django_db(transaction=True)
def test_get_game_by_status():
    repository_game = IRepositoryGame()
    repository_game.save_game('Room3')
    repository_game.save_game('Room4')
    result = repository_game.get_game_by_status(2)
    assert result[0].room_name == 'Room3'
    assert result[1].room_name == 'Room4'


@pytest.mark.django_db(transaction=True)
def test_get_all_games():
    repository_game = IRepositoryGame()
    repository_game.save_game('Room5')
    repository_game.save_game('Room6')
    assert repository_game.get_game_by_id(5).room_name == 'Room5'
    assert repository_game.get_game_by_id(6).room_name == 'Room6'


@pytest.mark.django_db(transaction=True)
def test_update_game_status_by_id():
    repository_game = IRepositoryGame()
    repository_game.save_game('Room7')
    repository_game.update_game_status_by_id(7, '1')
    assert repository_game.get_game_by_id(7).game_status == '1'


@pytest.mark.django_db(transaction=True)
def test_update_game_winners_by_id():
    repository_game = IRepositoryGame()
    repository_game.save_game('Room8')
    repository_game.update_game_winners_by_id(8, 1, 2, 3, 4, 5, 6)
    assert repository_game.get_game_by_id(8).second_winner == 2


@pytest.mark.django_db(transaction=True)
def test_delete_game_by_id():
    repository_game = IRepositoryGame()
    repository_game.save_game('Room9')
    assert repository_game.delete_game_by_id(9) is None
