import pytest

from game.irepository.irepository_dice import IRepositoryDice
from game.irepository.irepository_player import IRepositoryPlayer
from game.dice_handler import DiceHandler
from game.player.player import Player
from game.dice.dice import DieValue


@pytest.mark.django_db(transaction=True)
def test_save_dice():
    repository_dice = IRepositoryDice()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player_db(player)
    dice = DiceHandler()
    dice.dice_values = [DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE, DieValue.TWO, DieValue.THREE]
    dice.re_rolls_left = 2
    repository_dice.save_dice_db(player, dice)
    assert repository_dice.get_dice_db(player).dice1 == 'DieValue.ONE'


@pytest.mark.django_db(transaction=True)
def test_get_dice():
    repository_dice = IRepositoryDice()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player_db(player)
    dice = DiceHandler()
    dice.dice_values = [DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE, DieValue.TWO, DieValue.THREE]
    dice.re_rolls_left = 2
    repository_dice.save_dice_db(player, dice)
    assert repository_dice.get_dice_db(player).dice2 == 'DieValue.TWO'


@pytest.mark.django_db(transaction=True)
def test_update_dice():
    repository_dice = IRepositoryDice()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla2')
    player.set_username('Test_Update1')
    repository_player.save_player_db(player)
    dice1 = DiceHandler()
    dice1.dice_values = [DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE, DieValue.TWO, DieValue.THREE]
    dice1.re_rolls_left = 2
    repository_dice.save_dice_db(player, dice1)
    dice2 = DiceHandler()
    dice2.dice_values = [DieValue.THREE, DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE, DieValue.TWO]
    dice2.re_rolls_left = 2
    repository_dice.update_dice_db(player, dice2)
    assert repository_dice.get_dice_db(player).dice2 == 'DieValue.ONE'


@pytest.mark.django_db(transaction=True)
def test_update_die():
    repository_dice = IRepositoryDice()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla2')
    player.set_username('Test_Update1')
    repository_player.save_player_db(player)
    dice1 = DiceHandler()
    dice1.dice_values = [DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE, DieValue.TWO, DieValue.THREE]
    dice1.re_rolls_left = 2
    repository_dice.save_dice_db(player, dice1)
    repository_dice.update_die_db(player, 2, DieValue.THREE, True)
    assert repository_dice.get_dice_db(player).dice2 == 'DieValue.THREE'


@pytest.mark.django_db(transaction=True)
def test_delete_dice():
    repository_dice = IRepositoryDice()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    repository_player.save_player_db(player)
    dice = DiceHandler()
    dice.dice_values = [DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE, DieValue.TWO, DieValue.THREE]
    dice.re_rolls_left = 2
    repository_dice.save_dice_db(player, dice)
    assert repository_dice.delete_dice_db(player) is None
