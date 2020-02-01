import pytest

from game.irepository.irepository_dice import IRepositoryDice
from game.irepository.irepository_player import IRepositoryPlayer
from game.dice_handler import DiceHandler
from game.player.player import Player


@pytest.mark.django_db(transaction=True)
def test_save_dice():
    repository_dice = IRepositoryDice()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    player.set_password('Pass')
    repository_player.save_player_db(player)
    dice = DiceHandler()
    dice.dice_values = ['1', '2', '3', '1', '2', '3']
    dice.re_rolls_left = 2
    repository_dice.save_dice_db(player, dice)
    assert repository_dice.get_dice_db(player).dice1 == '1'


@pytest.mark.django_db(transaction=True)
def test_get_dice():
    repository_dice = IRepositoryDice()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    player.set_password('Pass')
    repository_player.save_player_db(player)
    dice = DiceHandler()
    dice.dice_values = ['1', '2', '3', '1', '2', '3']
    dice.re_rolls_left = 2
    repository_dice.save_dice_db(player, dice)
    assert repository_dice.get_dice_db(player).dice2 == '2'


@pytest.mark.django_db(transaction=True)
def test_update_dice():
    repository_dice = IRepositoryDice()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla2')
    player.set_username('Test_Update1')
    player.set_password('Pass1')
    repository_player.save_player_db(player)
    dice1 = DiceHandler()
    dice1.dice_values = ['1', '2', '3', '1', '2', '3']
    dice1.re_rolls_left = 2
    repository_dice.save_dice_db(player, dice1)
    dice2 = DiceHandler()
    dice2.dice_values = ['3', '1', '2', '3', '1', '2']
    dice2.re_rolls_left = 2
    repository_dice.update_dice_db(player, dice2)
    assert repository_dice.get_dice_db(player).dice2 == '1'


@pytest.mark.django_db(transaction=True)
def test_update_die():
    repository_dice = IRepositoryDice()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla2')
    player.set_username('Test_Update1')
    player.set_password('Pass1')
    repository_player.save_player_db(player)
    dice1 = DiceHandler()
    dice1.dice_values = ['1', '2', '3', '1', '2', '3']
    dice1.re_rolls_left = 2
    repository_dice.save_dice_db(player, dice1)
    repository_dice.update_die_db(player, 2, 5, True)
    assert repository_dice.get_dice_db(player).dice2 == '5'


@pytest.mark.django_db(transaction=True)
def test_delete_dice():
    repository_dice = IRepositoryDice()
    repository_player = IRepositoryPlayer()
    player = Player()
    player.set_monster_name('Godzilla1')
    player.set_username('Test_Get')
    player.set_password('Pass')
    repository_player.save_player_db(player)
    dice = DiceHandler()
    dice.dice_values = ['1', '2', '3', '1', '2', '3']
    dice.re_rolls_left = 2
    repository_dice.save_dice_db(player, dice)
    assert repository_dice.delete_dice_db(player) is None
