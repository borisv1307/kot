from os.path import dirname, basename, isfile, join
import glob
from typing import List

from game.cards.card import Card


def get_class(class_string_name_and_path):
    parsed_class_string = class_string_name_and_path.split('.')
    module = ".".join(parsed_class_string[:-1])
    m = __import__(module)
    for comp in parsed_class_string[1:]:
        m = getattr(m, comp)
    return m


def get_list_vpm_cards(prepend_path):
    if not str(prepend_path).endswith("."):
        prepend_path += "."

    modules = glob.glob(join(dirname(__file__), "*.py"))
    __all__ = [basename(f)[:-3] for f in modules if isfile(f)
               and not f.endswith('__init__.py')
               and not f.__contains__('card_collector')
               and not f.__contains__('test')]

    list_card: List[Card] = []

    for module in __all__:
        parts = str(module).split('_')
        camel_case_module = ''.join(i.title() for i in parts)
        list_card.append(get_class(prepend_path + module + "." + camel_case_module)())

    return list_card


