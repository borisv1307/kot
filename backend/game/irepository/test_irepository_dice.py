import pytest

from game.dice.dice import DieValue
from game.dice.dice_handler import DiceHandler
from game.irepository.irepository_dice import IRepositoryDice
from game.irepository.irepository_game import IRepositoryGame
from game.irepository.irepository_player import IRepositoryPlayer
from game.player.player import Player


@pytest.mark.django_db(transaction=True)
def test_save_dice():
    repository_dice = IRepositoryDice()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room1')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Godzilla1', 'Room1')
    assert repository_dice.save_dice('Godzilla1', 'Room1', DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE,
                                     DieValue.TWO, DieValue.THREE, None, None, 1, None).id == 1


@pytest.mark.django_db(transaction=True)
def test_get_dice_db():
    repository_dice = IRepositoryDice()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room2')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Mantra', 'Room2')
    repository_dice.save_dice('Mantra', 'Room2', DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE, DieValue.TWO,
                              DieValue.THREE, None, None, 1, None)
    assert repository_dice.get_dice_by_id(2).dice2 == 'DieValue.TWO'


@pytest.mark.django_db(transaction=True)
def test_update_dice_db():
    repository_dice = IRepositoryDice()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room3')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Kong', 'Room3')
    repository_dice.save_dice('Kong', 'Room3', DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE, DieValue.TWO,
                              DieValue.THREE, None, None, 1, None)
    repository_dice.update_dice_by_id(3, DieValue.THREE, DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE,
                                      DieValue.TWO, None, None, 1, None)
    assert repository_dice.get_dice_by_id(3).dice2 == 'DieValue.ONE'


@pytest.mark.django_db(transaction=True)
def test_update_die_by_id():
    repository_dice = IRepositoryDice()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room4')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Kraken', 'Room4')
    repository_dice.save_dice('Kraken', 'Room4', DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE, DieValue.TWO,
                              DieValue.THREE, None, None, 1, None)
    repository_dice.update_die_by_id(4, 2, DieValue.THREE, 1)
    assert repository_dice.get_dice_by_id(4).dice2 == 'DieValue.THREE'


@pytest.mark.django_db(transaction=True)
def test_delete_dice_by_id():
    repository_dice = IRepositoryDice()
    repository_game = IRepositoryGame()
    repository_game.save_game('Room5')
    repository_player = IRepositoryPlayer()
    repository_player.save_player('Drakonis', 'Room5')
    repository_dice.save_dice('Drakonis', 'Room5', DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE,
                              DieValue.TWO, DieValue.THREE, None, None, 1, None)
    assert repository_dice.delete_dice_by_id(5) is None
