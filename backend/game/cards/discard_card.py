from backend.game.cards.card import Card


class DiscardCard(Card):
    def __init__(self, name, cost, effect):
        super().__init__(name, cost, effect)

