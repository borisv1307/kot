import json
from typing import List

from game.cards.card import Card


def generate_player_status_summary(player_queue):
    if not player_queue.players:
        return []
    summary = [[] for i in range(len(player_queue.players))]
    count = 0
    for player in player_queue.players:
        player_summary: {} = player.generate_player_status_as_dictionary()
        summary[count] = player_summary
        count = count + 1
    return summary


def player_status_summary_to_JSON(player_queue):
    summary: [] = generate_player_status_summary(player_queue)
    return json.dumps(summary)


def json_players_hand(cards: List[Card] = []):
    json_data = []
    for card in cards:
        json_data.append(card.to_dict())
    return json.dumps(json_data)
