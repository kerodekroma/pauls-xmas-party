from enum import Enum, auto

class GAME_STATES(Enum):
    MAIN_MENU = auto()
    INIT_HISTORY = auto()
    PICK_PLAYER = auto()
    TOURNAMENT_TREE = auto()
    GAMEPLAY = auto()
    WIN_HISTORY = auto()
    LOSE_HISTORY = auto()