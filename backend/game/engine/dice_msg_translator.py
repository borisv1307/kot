def decode_selected_dice_indexes(payload):
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
