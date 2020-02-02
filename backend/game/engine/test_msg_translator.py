from game.dice.dice import DieValue
from game.dice.dice_handler import DiceHandler
from game.engine.dice_msg_translator import decode_selected_dice_indexes, dice_values_message_create, \
    translate_enum_to_frontend_val


def test_decode_index():
    sample_frontend_index = [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]
    assert decode_selected_dice_indexes(sample_frontend_index) == [0, 2, 4]


def test_translate_dice_vals():
    dh = DiceHandler()
    dh.roll_initial(6, 3)
    vals = dh.dice_values
    msg = dice_values_message_create(vals)
    print(msg)


def test_translate_enum_to_frontend_val():
    # for val in ['ONE', 'TWO', 'THREE', 'ATTACK', 'HEAL', 'ENERGY']
    # frontend_values = ['1', '2', '3', 'a', 'h', 'e']
    assert translate_enum_to_frontend_val(DieValue.ONE.name) == '1'
    assert translate_enum_to_frontend_val(DieValue.TWO.name) == '2'
    assert translate_enum_to_frontend_val(DieValue.THREE.name) == '3'
    assert translate_enum_to_frontend_val(DieValue.ATTACK.name) == 'a'
    assert translate_enum_to_frontend_val(DieValue.HEAL.name) == 'h'
    assert translate_enum_to_frontend_val(DieValue.ENERGY.name) == 'e'
