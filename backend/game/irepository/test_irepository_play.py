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
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player(player, 'Room1')
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    assert repository_play.save_play_card_swept(player, 'Room1', '01', '1', '02', '1', '03', '1') == 1


@pytest.mark.django_db(transaction=True)
def test_save_play_card_purchased_db():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room2')
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player(player, 'Room2')
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    assert repository_play.save_play_card_purchased(player, 'Room2', '01', '1') == 2


@pytest.mark.django_db(transaction=True)
def test_save_play_card_used():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room3')
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player(player, 'Room3')
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    assert repository_play.save_play_card_used(player, 'Room3', '02', '1') == 3


@pytest.mark.django_db(transaction=True)
def test_get_play_by_id():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room4')
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player(player, 'Room4')
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    repository_play.save_play_card_swept(player, 'Room4', '04', '1', '05', '1', '06', '1')
    assert repository_play.get_play_by_id(4).card1_swept == '04'


@pytest.mark.django_db(transaction=True)
def test_get_plays_by_player_and_room():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room5')
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player(player, 'Room5')
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    repository_play.save_play_card_swept(player, 'Room5', '04', '1', '05', '1', '06', '1')
    assert repository_play.get_plays_by_player_and_room(player, 'Room5').card2_swept == '05'


@pytest.mark.django_db(transaction=True)
def test_update_play_card_swept():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room6')
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player(player, 'Room6')
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    repository_play.save_play_card_swept(player, 'Room6', '01', '1', '02', '1', '03', '1')
    repository_play.update_play_card_swept_by_id(6, '10', '1', '12', '1', '13', '1')
    assert repository_play.get_play_by_id(6).card3_swept == '13'


@pytest.mark.django_db(transaction=True)
def test_update_play_card_purchased():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room7')
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player(player, 'Room7')
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    repository_play.save_play_card_purchased(player, 'Room7', '01', '1')
    repository_play.update_play_card_purchased_by_id(7, '21', '1')
    assert repository_play.get_play_by_id(7).card_purchased == '21'


@pytest.mark.django_db(transaction=True)
def test_update_play_card_used():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room8')
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player(player, 'Room8')
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    repository_play.save_play_card_used(player, 'Room8', '01', '1')
    repository_play.update_play_card_used_by_id(8, '31', '1')
    assert repository_play.get_play_by_id(8).card_used == '31'


@pytest.mark.django_db(transaction=True)
def test_update_play_card_location_by_id():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room9')
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player(player, 'Room9')
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    player.location = locations.Locations.OUTSIDE
    repository_play.save_play_card_used(player, 'Room9', '01', '1')
    repository_play.update_play_location_by_id(9, locations.Locations.TOKYO.value)
    assert repository_play.get_play_by_id(9).location == '1'


@pytest.mark.django_db(transaction=True)
def test_update_play_card_victory_point_by_id():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room10')
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player(player, 'Room10')
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    repository_play.save_play_card_used(player, 'Room10', '01', '1')
    repository_play.update_play_victory_points_by_id(10, constants.VICTORY_POINTS_TO_WIN)
    assert repository_play.get_play_by_id(10).victory_points == constants.VICTORY_POINTS_TO_WIN


@pytest.mark.django_db(transaction=True)
def test_update_play_card_energy_by_id():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room11')
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player(player, 'Room11')
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    repository_play.save_play_card_used(player, 'Room11', '01', '1')
    repository_play.update_play_energy_by_id(11, constants.ENERGY_HOARDER_DIVIDER)
    assert repository_play.get_play_by_id(11).energy_cube == constants.ENERGY_HOARDER_DIVIDER


@pytest.mark.django_db(transaction=True)
def test_update_play_card_health_by_id():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room12')
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player(player, 'Room12')
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    repository_play.save_play_card_used(player, 'Room12', '01', '1')
    repository_play.update_play_life_by_id(12, constants.DEFAULT_HEALTH)
    assert repository_play.get_play_by_id(12).life_points == constants.DEFAULT_HEALTH


@pytest.mark.django_db(transaction=True)
def test_delete_dice():
    repository_play = IRepositoryPlay()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room13')
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player(player, 'Room13')
    player.move_to_tokyo()
    player.update_victory_points_by(2)
    player.update_energy_by(2)
    player.update_health_by(-1)
    repository_play.save_play_card_swept(player, 'Room13', '01', '1', '02', '1', '03', '1')
    assert repository_play.delete_play_by_id(13) is None
