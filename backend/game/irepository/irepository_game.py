class IRepositoryGame:
    def __init__(self):
        self.game = None
        self.game_id = None

    """
    CRUD function for Game below
    """

    def save_game_db(self, game):
        self.game = game
        pass

    def get_game_db(self, game_id):
        pass

    def update_game_db(self, game, game_id):
        pass

    def delete_game_db(self, game_id):
        pass
