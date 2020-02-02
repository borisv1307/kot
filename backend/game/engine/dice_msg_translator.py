def decode_selected_dice_indexes(payload):
    """
    Front end sends the list of selected dice as a list of pairs, the value and a boolean flag for selected.
    For example:
    [['1','True'] , ['a', 'False'],  ['h','True'] ... ]
    This function translates this message to just a list of selected dice to re-roll like the MT expects in the
    DiceHandler. So above becomes [0, 2 ... ]
    """
    i = 0
    indexes = []
    for index in payload:
        if index[1]:
            indexes.append(i)
        i += 1
    return indexes


def dice_values_message_create(values):
    msg = []
    for val in values:
        translated_val = translate_enum_to_frontend_val(val.name)
        msg.append([translated_val, False])
    return msg


def translate_enum_to_frontend_val(enum_val):
    enum_values = ['ONE', 'TWO', 'THREE', 'ATTACK', 'HEAL', 'ENERGY']
    frontend_values = ['1', '2', '3', 'a', 'h', 'e']
    return frontend_values[enum_values.index(enum_val)]
