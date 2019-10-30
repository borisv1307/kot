from backend.src.game.cards.card_type import CardType


def set_card_type(card_type):
    if str.lower(card_type) == "keep":
        return CardType.KEEP
    elif str.lower(card_type) == "discard":
        return CardType.DISCARD
    else:
        return CardType.INVALID


class Card(object):
    def __init__(self, name, cost, card_type, effect, footnote):
        self.name = name
        self.cost = cost
        self.effect = effect
        self.footnote = footnote
        self.card_type = set_card_type(card_type)

    def card_details_str(self):
        return "\nname: {0}\ncost: {1}\ntype: {2}\neffect: {3}\nfootnote: {4}".format(self.name, self.cost,
                                                                                      self.card_type,
                                                                                      self.effect, self.footnote)

    def is_valid(self):
        try:
            assert isinstance(self.name, str)
            assert isinstance(self.cost, int)
            assert isinstance(self.effect, str)
            assert isinstance(self.card_type, CardType) and self.card_type != CardType.INVALID
        except AssertionError:
            print("invalid card: " + self.card_details_str())
            return False
        return True
