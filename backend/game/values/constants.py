import os

# directories
CARDS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# ints
DEFAULT_DICE_TO_ROLL = 6
DEFAULT_RE_ROLL_COUNT = 2
DEFAULT_HEALTH = 10
DEATH_HIT_POINT = 0
DEFAULT_ENERGY_CUBE = 0
CARD_STORE_SIZE_LIMITER = 3
ENERGY_HOARDER_DIVIDER = 6
SWEEP_CARD_STORE_COST = 2
VICTORY_POINTS_TO_WIN = 20

# strings
OUT_OF_CARDS_MSG = "No more cards available to shuffle"
INSUFFICIENT_FUNDS_MSG = "Insufficient energy to purchase card"
INSUFFICIENT_FUNDS_TO_SWEEP_MSG = "Insufficient energy to sweep the card store"
