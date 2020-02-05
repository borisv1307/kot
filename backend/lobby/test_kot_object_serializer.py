import json
import re

from game.dice.dice_handler import DiceHandler
from lobby.kot_object_serializer import KOTObjectSerializer


def test_serialize():
    """duplicate of test in test_dice_handler, placed here as well to demonstrate serializer is tested and to allow
    easy to find example of using serializer """
    dh = DiceHandler()
    dh.roll_initial(6, 3)
    print("\n\n")
    print("re rolls left = {}".format(dh.re_rolls_left))
    encoded_dh = json.dumps(dh.serialize_kot_obj(), cls=KOTObjectSerializer)
    print("the json data is:\n{}".format(encoded_dh))
    assert re.match(".*dice_handler.*dice_values.*(die_val.*){6}re_rolls_left.*", encoded_dh, )
