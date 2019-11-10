from os.path import dirname, basename, isfile, join
import glob
from typing import List

from game.cards.card import Card
from game.cards.discard_card import DiscardCard


def get_class( kls ):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m


def get_list_vpm_cards(prepend_path):
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


