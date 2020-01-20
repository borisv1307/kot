class IRepositoryDice:

    def __init__(self):
        self.dice = None
        self.dice_id = None

    """
    CRUD function for Dice below
    """

    def save_dice_db(self, dice):
        self.dice = dice
        return 0

    def get_dice_db(self, dice_id):
        pass

    def update_dice_db(self, dice, dice_id):
        pass

    def delete_dice_db(self, dice_id):
        pass
