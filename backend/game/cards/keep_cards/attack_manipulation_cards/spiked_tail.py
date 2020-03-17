from game.cards.keep_card import KeepCard


class SpikedTail(KeepCard):
    def __init__(self):
        super().__init__("Spiked Tail", 5,
                         "If you roll at least one [attack], add [attack] to your roll")

    def special_effect(self, player_that_bought_the_card, attack_die_value):
        pass

    def attack_dice_special_effect(self, player_that_bought_the_card, attack_die_value):
        if attack_die_value >= 1:
            return attack_die_value + 1
        else:
            return attack_die_value
