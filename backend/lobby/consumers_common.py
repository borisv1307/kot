import pickle

from game.engine.board import BoardGame
from game.models import GameState


def reconstruct_game(data):
    username = data['user']
    room = data['room']

    game = GameState.objects.get(room_name=room)
    # deserialize then store GameState object
    state: BoardGame = pickle.loads(game.board)
    return username, room, game, state


def save_game(game, state):
    game.board = pickle.dumps(state)
    game.save()


def create_send_response_to_client(command, username, room, payload):
    content = {
        'command': command,
        'action': {
            'user': username,
            'room': room,
            'content': payload
        }
    }
    return content
