import pytest

from game.irepository.irepository_game import IRepositoryGame
from game.irepository.irepository_play import IRepositoryPlay
from game.irepository.irepository_player import IRepositoryPlayer
from game.player.player import Player
from game.values import constants
# from game.cards.card import Card
from game.values import locations


@pytest.mark.django_db(transaction=True)
def test_save_play_card_swept_db():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room1')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Godzilla1', 'Room1')
    assert repository_play.save_play_card_swept('Godzilla1', 'Room1', '01', '1', '02', '1', '03', '1', '1', 10, 10, 10).id == 1


@pytest.mark.django_db(transaction=True)
def test_save_play_card_purchased_db():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room2')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Godzilla2', 'Room2')
    assert repository_play.save_play_card_purchased('Godzilla2', 'Room2', '01', '1', '1', 10, 10, 10).id == 2


@pytest.mark.django_db(transaction=True)
def test_save_move_in_and_out_tokyo():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room3')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Godzilla3', 'Room3')
    assert repository_play.save_move_in_and_out_tokyo('Godzilla3', 'Room3', '1', 10, 10, 10).id == 3


@pytest.mark.django_db(transaction=True)
def test_get_play_by_id():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room4')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Godzilla4', 'Room4')
    repository_play.save_play_card_swept('Godzilla4', 'Room4', '04', '1', '05', '1', '06', '1', '1', 10, 10, 10)
    assert repository_play.get_play_by_id(4).card1_swept == '04'


@pytest.mark.django_db(transaction=True)
def test_get_plays_by_player_and_room():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room5')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Godzilla5', 'Room5')
    repository_play.save_play_card_swept('Godzilla5', 'Room5', '04', '1', '05', '1', '06', '1', '1', 10, 10, 10)
    assert repository_play.get_plays_by_player_and_room('Godzilla5', 'Room5').card2_swept == '05'


@pytest.mark.django_db(transaction=True)
def test_update_play_card_swept():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room6')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Godzilla6', 'Room6')
    repository_play.save_play_card_swept('Godzilla6', 'Room6', '01', '1', '02', '1', '03', '1', '1', 10, 10, 10)
    repository_play.update_play_card_swept_by_id(6, '10', '1', '12', '1', '13', '1')
    assert repository_play.get_play_by_id(6).card3_swept == '13'


@pytest.mark.django_db(transaction=True)
def test_update_play_card_purchased():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room7')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Godzilla7', 'Room7')
    repository_play.save_play_card_purchased('Godzilla7', 'Room7', '01', '1', '1', 10, 10, 10)
    repository_play.update_play_card_purchased_by_id(7, '21', '1')
    assert repository_play.get_play_by_id(7).card_purchased == '21'


@pytest.mark.django_db(transaction=True)
def test_update_play_card_location_by_id():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room8')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Godzilla8', 'Room8')
    repository_play.save_play_card_purchased('Godzilla8', 'Room8', '01', '1', '1', 10, 10, 10)
    repository_play.update_play_location_by_id(8, locations.Locations.TOKYO.value)
    assert repository_play.get_play_by_id(8).location == '1'


@pytest.mark.django_db(transaction=True)
def test_update_play_card_victory_point_by_id():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room9')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Godzilla9', 'Room9')
    repository_play.save_play_card_purchased('Godzilla9', 'Room9', '01', '1', '1', 10, 10, 10)
    repository_play.update_play_victory_points_by_id(9, constants.VICTORY_POINTS_TO_WIN)
    assert repository_play.get_play_by_id(9).victory_points == constants.VICTORY_POINTS_TO_WIN


@pytest.mark.django_db(transaction=True)
def test_update_play_card_energy_by_id():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room10')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Godzilla10', 'Room10')
    repository_play.save_play_card_purchased('Godzilla10', 'Room10', '01', '1', '1', 10, 10, 10)
    repository_play.update_play_energy_by_id(10, constants.ENERGY_HOARDER_DIVIDER)
    assert repository_play.get_play_by_id(10).energy_cube == constants.ENERGY_HOARDER_DIVIDER


@pytest.mark.django_db(transaction=True)
def test_update_play_card_health_by_id():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room11')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Godzilla11', 'Room11')
    repository_play.save_play_card_purchased('Godzilla11', 'Room11', '01', '1', '1', 10, 10, 10)
    repository_play.update_play_health_by_id(11, constants.DEFAULT_HEALTH)
    assert repository_play.get_play_by_id(11).health_points == constants.DEFAULT_HEALTH


@pytest.mark.django_db(transaction=True)
def test_delete_dice_by_id():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room12')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Godzilla12', 'Room12')
    repository_play.save_play_card_swept('Godzilla12', 'Room12', '01', '1', '02', '1', '03', '1', '1', 10, 10, 10)
    assert repository_play.delete_play_by_id(12) is None
