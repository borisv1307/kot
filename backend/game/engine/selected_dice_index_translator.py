def decode_selected_dice_indexes(payload):
    i = 0
    indexes = []
    for index in payload:
        if index[1]:
            indexes.append(i)
        i += 1
    return indexes
