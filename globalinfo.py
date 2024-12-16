# Data and information that is set by the player #
# Information is saved between saves #

import pygame

controls_data = {
    "move up": "W",
    "move down": "S",
    "move left": "A",
    "move right": "D",

    "primary attack": "LMB",
    "secondary attack": "RMB",
    "cast spell": "MMB",
    "weapon skill": "Q",

    "roll": "SFT",
    "use flask": "E",
    "interact": "F",
}

controls_keys = {

}

difficulty_data = {
    "enemy data":{
        "base health": 1,
        "base attack": 1,
        "base speed": 1,
    },
    "player data":{
        "base health": 1,
        "base attack": 1,
        "base speed": 1,
    },
    "costs data": {
        "cost multiplier": 1,
        "reward multiplier": 1,
    }
}

global_settings = {
    "audio": {"music": 1, "effects": 1, "misc.": 1},
    "visuals": {"gamma": 0.8},
}