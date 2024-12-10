# Data and information that is updated and changed as gameplay progresses #
# Information is saved to and loaded from here #

# System Settings
local_settings = {
    "gameplay": {"hard_mode": False, "soles_mode": False, "HUD": "Default"},
    "cosmetics": {"armour": 1,}
}
global_settings = {
    "Audio": {"Music": 1, "SFX": 1, "Player": 1},
    "Visuals": {"Brightness": 0.8, "Subtitles": "On"},
}

# NPC Stuff
# Name | Priority | Bool: has dialogue been played | Text
npc_conversations = {
    "firekeeper": {
        "000": {
            "name": "???", "priority": 0, "completed": False, "text": [""],
        },
        "001": {
            "name": "Fire Keeper", "priority": 100, "completed": False, "text": ["Welcome to the bonfire, Undead.", "I am the Fire Keeper.", "I tend to the flame, and to thee.", "The fire fades, and soon only dark shall|remain.", "To this end, I am at thy side.", ""],
        },
        "002": {
            "name": "Fire Keeper", "priority": 1, "completed": False, "text": ["Undead, to be human is to be a vessel|for souls.", "Sovereignless souls will become thy|strength.", "I will show thee how.", "Undead, bring me souls, plucked from|their vessels..."],
        },
        "003": {
            "name": "Fire Keeper", "priority": 99, "completed": False, "text": ["Undead, thou hast rung the First Bell of|Awakening.", "Wonderful work.", "To fulfill the prophecy, thou must now|travel to the depths of Lordran, through|the abandoned settlement of Blighttown.", "Stay cautious on your journey. I will|continue to remain here to aid thee as|ever."],
        },
    },
    # "logan": [
    #     ["???", 0, False, "Placeholder"],
    #     ["Big Hat Logan", 1, False, "...", "My thanks, my name is Logan.", "You must be an Undead."]
    # ],
    # "crestfallen": [
    #     ["???", 0, False, "Placeholder"],
    #     ["Crestfallen Warrior", 100, False, "Well, what do we have here? You must be a|new arrival.", "Let me guess. Fate of the Undead, right?|Well, you're not the first.", "Well, since you're here... Let me help you|out.", "There are actually two Bells of Awakening.", "One's up above, in the Undead Church. The|other is far, far below, in the ruins at|the base of Blighttown.", "Ring them both, and something happens... |Brilliant, right?", "Not much to go on, but I have a feeling|that won't stop you.", "Hah hah hah hah..."],
    # ],
    # "frampt": [
    #     ["???", 0, False, "Placeholder"],
    #     ["Kingseeker Frampt", 100, False, "Ahh, hello.", "Was it you who rang the Bells of|Awakening?", "I am the primordial serpent, Kingseeker|Frampt, close friend of the Great Lord|Gwyn.", "Chosen Undead, who has rung the Bells of|Awakening. I wish to elucidate your fate.", "Do you seek such enlightenment?", "Chosen Undead. Your fate...", "... is to succeed the Great Lord Gwyn.|So that you may link the Fire, cast away|the Dark, and undo the curse of the|Undead.", "To this end, you must visit Anor Londo,|and acquire the Lordvessel. "],
    # ],
}

# Meta-Progression Resources
resources = {
    "soul remnants": 30,
    "humanity sprites": 99,
    "titanite chunks": 3,
    "demon titanite": 1,
}

# Covenant Ranks
covenant_ranks = {
    "warriors of sunlight": 0,
    "blades of the darkmoon": 0,
    "darkwraiths": 0,
    "chaos servants": 0,
}

# Base attributes
player_attributes = {
    "VITALITY": 1,
    "ENDURANCE": 1,
    "STRENGTH": 1,
    "DEXTERITY": 1,
    "INTELLIGENCE": 1,
    "FAITH": 1,
}

# Gifts of Humanity
player_gifts = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
}

# Permanent Unlocks
player_unlocks = {
    "1st bell of awakening": False,
    "2nd bell of awakening": False,
    "lordvessel": False,
}

# Player details for per run
interface_details = {
    "light_attack": {
        "class": "sword", "name": "broadsword_light", "cooldown": 520, "base damage": 15, "knockback": 0, "stamina_use": 15,
    },
    "heavy_attack": {
        "class": "sword", "name": "broadsword_heavy", "cooldown": 750, "base damage": 30, "knockback": 1, "stamina_use": 25,
    },
    "catalyst": {
        "class": "pyromancy", "name": "pyromancy_flame", "cooldown": 5000, "base damage": 5,
    },
    "skill": {
        "name": "skill_1", "cooldown": 400, "base damage": 10, "stamina_use": 25,
    },
    # "rings": {
    #     "ring 1": None, "ring 2": None,
    # },
    "boons": {
        "list": ["boon_5", "boon_6", "boon_9", "boon_11"],
    },
    "spells": {
        1: "heal", 2: "fire_surge", 3: "icecrag_burst",
    },
    "values": {
        "estus level": 1,
        "souls": 0,
        "lost souls": 0,
        "max estus": 3,
        "current estus": 3,
        "levelup cost": 1,
    }
}

# Hidden numbers which can be affected by boons
player_data = {
    "dependent_variables": {"health": 200, "mana": 50, "stamina": 50, "speed": 5, "defense": 0.25, "poise": 40, "attack": 5, "magic mult": 1, "stamina recovery": 0.2, "mana recovery": 0},

    "stamina_costs": {"weapon_usage": 5, "magic_usage": 4, "rolling": 15},
}

# Player inputs (mainly used for mouse)
player_inputs = {
    "light attack": False, "heavy attack": False, "skill": False, "cast spell": False, "roll": False, "scroll spell": False, "scroll direction": 0,
}

# Enemy Spawn Types
enemy_spawn_template = {
    "undead_burg": {
        "01": { "type": "waves", "min_enemies": 4, "max_enemies": 5, "min_waves": 2, "max_waves": 2, "whitelisted_enemies": ["undead_warrior"], "scaling": 0.5, "drop_mult": 1, "selection_mult": 1 },
        # "02": { "type": "constant", "min_enemies": 6, "max_enemies": 6, "min_waves": 0, "max_waves": 0, "whitelisted_enemies": ["squid", "spirit"], "scaling": 0.5, "drop_mult": 1, "selection_mult": 0.75 },
        # # "03": { "type": "boss", "min_enemies": 1, "max_enemies": 1, "min_waves": 0, "max_waves": 0, "whitelisted_enemies": ["raccoon"], "scaling": 0.75, "drop_mult": 1.5, "selection_mult": 0.5 },
        # "04": { "type": "waves", "min_enemies": 6, "max_enemies": 8, "min_waves": 2, "max_waves": 4, "whitelisted_enemies": ["bamboo", "spirit", "squid"], "scaling": 0.5, "drop_mult": 1, "selection_mult": 1 },
        # "05": { "type": "waves", "min_enemies": 5, "max_enemies": 6, "min_waves": 2, "max_waves": 3, "whitelisted_enemies": ["spirit"], "scaling": 0.5, "drop_mult": 1, "selection_mult": 1 },
        # "06": { "type": "constant", "min_enemies": 6, "max_enemies": 7, "min_waves": 3, "max_waves": 3, "whitelisted_enemies": ["bamboo"], "scaling": 0.5, "drop_mult": 1, "selection_mult": 1 },
    },
    "undead_parish": {
        "01": { "type": "waves", "min_enemies": 4, "max_enemies": 5, "min_waves": 2, "max_waves": 2, "whitelisted_enemies": ["bamboo", "spirit"], "scaling": 0.5, "drop_mult": 1, "selection_mult": 1 },
        "02": { "type": "constant", "min_enemies": 5, "max_enemies": 6, "min_waves": 0, "max_waves": 0, "whitelisted_enemies": ["squid", "spirit"], "scaling": 0.5, "drop_mult": 1, "selection_mult": 0.75 },
    },
    "the_depths": {
        "01": { "type": "waves", "min_enemies": 4, "max_enemies": 5, "min_waves": 2, "max_waves": 2, "whitelisted_enemies": ["bamboo", "spirit"], "scaling": 0.5, "drop_mult": 1, "selection_mult": 1 },
        "02": { "type": "constant", "min_enemies": 6, "max_enemies": 6, "min_waves": 0, "max_waves": 0, "whitelisted_enemies": ["squid", "spirit"], "scaling": 0.5, "drop_mult": 1, "selection_mult": 0.75 },
    },
}

# Current Chamber - Spawn Details
# Dynamically updated at the creation of each chamber
chamber_enemy_info = {
    "type": "",
    "total_enemies": "",
    "enemy_list": [], # Each element in the list represents an enemy -> (position, type)

    # Waves
    "num_waves": "",
    "enemies_per_wave": "",
    "remainder_enemies": "",

    # Constant
    "initial_num": "",
}