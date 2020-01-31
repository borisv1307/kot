from game.engine.selected_dice_index_translator import decode_selected_dice_indexes


def test_decode_index():
    sample_frontend_index = [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]
    assert decode_selected_dice_indexes(sample_frontend_index) == [0, 2, 4]
