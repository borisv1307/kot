# import pytest
#
# from game.irepository.irepository_dice import IRepositoryDice
# from game.irepository.irepository_player import IRepositoryPlayer
# from game.irepository.irepository_game import IRepositoryGame
# from game.dice_handler import DiceHandler
# from game.player.player import Player
# from game.dice.dice import DieValue
#
#
# @pytest.mark.django_db(transaction=True)
# def test_save_dice():
#     repository_dice = IRepositoryDice()
#     repository_game = IRepositoryGame()
#     repository_game.save_game('Room1')
#     repository_player = IRepositoryPlayer()
#     player = Player()
#     player.set_monster_name('Godzilla1')
#     player.set_username('Test_Get')
#     repository_player.save_player(player, 'Room1')
#     assert repository_dice.save_dice(player, 'Room1', DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE,
#                                      DieValue.TWO, DieValue.THREE, 0, 0, 1) == 1
#
#
# @pytest.mark.django_db(transaction=True)
# def test_get_dice_db():
#     repository_dice = IRepositoryDice()
#     repository_game = IRepositoryGame()
#     repository_game.save_game('Room2')
#     repository_player = IRepositoryPlayer()
#     player = Player()
#     player.set_monster_name('Godzilla1')
#     player.set_username('Test_Get')
#     repository_player.save_player(player, 'Room2')
#     dice = DiceHandler()
#     repository_dice.save_dice(player, 'Room2', DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE,
#                               DieValue.TWO, DieValue.THREE, 0, 0, 1)
#     assert repository_dice.get_dice_by_id(2).dice2 == 'DieValue.TWO'
#
#
# @pytest.mark.django_db(transaction=True)
# def test_update_dice_db():
#     repository_dice = IRepositoryDice()
#     repository_game = IRepositoryGame()
#     repository_game.save_game('Room3')
#     repository_player = IRepositoryPlayer()
#     player = Player()
#     player.set_monster_name('Godzilla2')
#     player.set_username('Test_Update1')
#     repository_player.save_player(player, 'Room3')
#     repository_dice.save_dice(player, 'Room3', DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE,
#                               DieValue.TWO, DieValue.THREE, 0, 0, 1)
#     repository_dice.update_dice_by_id(3, DieValue.THREE, DieValue.ONE, DieValue.TWO, DieValue.THREE,
#                                       DieValue.ONE, DieValue.TWO, 0, 0, 1)
#     assert repository_dice.get_dice_by_id(3).dice2 == 'DieValue.ONE'
#
#
# @pytest.mark.django_db(transaction=True)
# def test_update_die_by_id():
#     repository_dice = IRepositoryDice()
#     repository_game = IRepositoryGame()
#     repository_game.save_game('Room4')
#     repository_player = IRepositoryPlayer()
#     player = Player()
#     player.set_monster_name('Godzilla2')
#     player.set_username('Test_Update1')
#     repository_player.save_player(player, 'Room4')
#     repository_dice.save_dice(player, 'Room4', DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE,
#                               DieValue.TWO, DieValue.THREE, 0, 0, 1)
#     repository_dice.update_die_by_id(4, 2, DieValue.THREE, 1)
#     assert repository_dice.get_dice_by_id(4).dice2 == 'DieValue.THREE'
#
#
# @pytest.mark.django_db(transaction=True)
# def test_delete_dice_by_id():
#     repository_dice = IRepositoryDice()
#     repository_game = IRepositoryGame()
#     repository_game.save_game('Room5')
#     repository_player = IRepositoryPlayer()
#     player = Player()
#     player.set_monster_name('Godzilla1')
#     player.set_username('Test_Get')
#     repository_player.save_player(player, 'Room5')
#     repository_dice.save_dice(player, 'Room5', DieValue.ONE, DieValue.TWO, DieValue.THREE, DieValue.ONE,
#                               DieValue.TWO, DieValue.THREE, 0, 0, 1)
#     assert repository_dice.delete_dice_by_id(5) is None
