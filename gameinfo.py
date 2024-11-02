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
npc_conversations = {
    "firekeeper": [
        ["???", 0, False, "Placeholder"],
        ["Fire Keeper", 100, False, "Welcome to the bonfire, Undead.", "I am the Fire Keeper.", "I tend to the flame, and to thee.", "The fire fades, and soon only dark shall|remain.", "To this end, I am at thy side."],
        ["Fire Keeper", 1, False, "Undead, to be human is to be a vessel|for souls.", "Sovereignless souls will become thy|strength.", "I will show thee how.", "Undead, bring me souls, plucked from|their vessels..."],
        ["Fire Keeper", 2, False, "Erm... what the sigma?"],
        ["Fire Keeper", 99, False, "Undead, thou hast rung the First Bell of|Awakening.", "Wonderful work.", "To fulfill the prophecy, thou must now|travel to the depths of Lordran, through|the abandoned settlement of Blighttown.", "Stay cautious on your journey. I will|continue to remain here to aid thee as|ever."],
    ],
    "logan": [
        ["???", 0, False, "Placeholder"],
        ["Big Hat Logan", 1, False, "...", "My thanks, my name is Logan.", "You must be an Undead."]
    ],
    "crestfallen": [
        ["???", 0, False, "Placeholder"],
        ["Crestfallen Warrior", 100, False, "Well, what do we have here? You must be a|new arrival.", "Let me guess. Fate of the Undead, right?|Well, you're not the first.", "Well, since you're here... Let me help you|out.", "There are actually two Bells of Awakening.", "One's up above, in the Undead Church. The|other is far, far below, in the ruins at|the base of Blighttown.", "Ring them both, and something happens... |Brilliant, right?", "Not much to go on, but I have a feeling|that won't stop you.", "Hah hah hah hah..."],
    ],
    "frampt": [
        ["???", 0, False, "Placeholder"],
        ["Kingseeker Frampt", 100, False, "Ahh, hello.", "Was it you who rang the Bells of|Awakening?", "I am the primordial serpent, Kingseeker|Frampt, close friend of the Great Lord|Gwyn.", "Chosen Undead, who has rung the Bells of|Awakening. I wish to elucidate your fate.", "Do you seek such enlightenment?", "Chosen Undead. Your fate...", "... is to succeed the Great Lord Gwyn.|So that you may link the Fire, cast away|the Dark, and undo the curse of the|Undead.", "To this end, you must visit Anor Londo,|and acquire the Lordvessel. "],
    ],
}

# Meta-Progression Resources
resources = {
    "soul remnants": 99,
    "humanities": 11,

    "souvenirs of reprisal": 2,
    "sunlight medals": 3,

    "titanite shards": 4,
    "titanite chunks": 3,
    "titanite slabs": 0,
    "demon titanite": 1,
}

# Covenant Ranks
covenant_ranks = {
    "warriors of sunlight": 0,
    "blades of the darkmoon": 0,
    "darkwraiths": 0,
    "chaos servants": 0,
}

# Resource Info
resource_details = {
    "soul remnants": ["Level-up Resource", "Remains of a powerful soul belonging to a great warrior.", "Gained after death, amount scaling with the|number of level-ups in a run.", "Can be spent at the Fire Keeper to gain|permanent level-ups."],
    "humanities": ["Level-up Resource | Covenant Offering", "Rare black sprite found on corpses, distinct from the soul that resides within all creatures.", "Can be found in chambers.|Can be gained from defeating strong enemies.", "Can be spent at the Firelink bonfire to gain|permanent unique effects.|Can be offered to the Chaos Servants and|Darkwraiths to increase Covenant rank."],

    "souvenirs of reprisal": ["Covenant Offering", "Blood-drained, shrunken ear. Souvenir taken from subduing the guilty.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be offered to the Blades of the Darkmoon|to increase Covenant rank."],
    "sunlight medals": ["Covenant Offering", "Warm medal, engraved with the symbol of the Sun. Represents Lord Gwyn's firstborn, who lost the status of deity.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be offered to the Warriors of Sunlight to|increase Covenant rank."],
    "eyes of death": ["Covenant Offering", "Eyes taken from those afflicted by curses of petrification. Known to be used to spread death.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be offered to the Gravelord Servants to|increase Covenant rank."],
    "dragon scales": ["Covenant Offering", "Scales peeled from an ancient dragon. Highly sought after for its rarity.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be offered to the Path of the Dragon to|increase Covenant rank."],

    "titanite shards": ["Upgrade Material", "Most common titanite material. Etched into weapons for reinforcement.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be used to strengthen standard weapons|to +3."],
    "large titanite shards": ["Upgrade Material", "Larger and rarer titanite material. Etched into weapons for reinforcement.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be used to strengthen standard weapons|to +6."],
    "titanite chunks": ["Upgrade Material", "Highly valuable titanite material found only in Lordran. Etched into weapons for reinforcement.", "Can be found in chambers.", "Can be used to strengthen standard weapons|to +9."],
    "titanite slabs": ["Upgrade Material", "Legendary titanite material of a nameless blacksmith deity. Etched into weapons for reinforcement.", "Can be found in chambers.|Can be gained from defeating strong enemies.", "Can be used to strengthen standard weapons|to +10 and demon/twinkling weapons to +5."],
    "demon titanite": ["Upgrade Material", "Special titanite stolen from a faceless stone beast known as a Titanite Demon.", "Can be found in chambers.|Can be gained from defeating strong enemies.", "Can be used to strengthen demon weapons to +4."],
    "twinkling titanite": ["Upgrade Material", "Titanite imbued with a particularly powerful energy of unknown origin.", "Can be found in chambers.|Can be gained from defeating strong enemies.", "Can be used to strengthen twinkling weapons|to +4."],
}

# Base attributes
player_attributes = {
    "Vigour": 1,
    "Endurance": 1,
    "Attunement": 1,
    "Strength": 1,
    "Dexterity": 1,
    "Intelligence": 1,
    "Faith": 1,
}

# Permanent Unlocks
player_unlocks = {
    "rite of kindling": False,
    "1st bell of awakening": False,
    "2nd bell of awakening": False,
    "lordvessel": False,
    "soul of the gravelord": False,
    "soul of the paledrake": False,
    "soul of the chaos witch": False,
    "soul of the four kings": False,
    "kiln of the first flame": False,
}

# Player details for per run
interface_details = {
    "light_attack": {
        "class": "sword", "name": "broadsword_light", "cooldown": 100, "base damage": 15, "knockback": 1, "weight": 3, "effects": None, "infusion": None,
    },
    "heavy_attack": {
        "class": "sword", "name": "broadsword_heavy", "cooldown": 200, "base damage": 25, "knockback": 1, "weight": 5, "effects": None, "infusion": None,
    },
    "catalyst": {
        "class": "pyromancy", "name": "pyromancy_flame", "cooldown": 100, "base damage": 5, "weight": 0, "effects": None, "infusion": None,
    },
    "skill": {
        "name": "skill_1", "cooldown": None, "base damage": None, "effects": None, "infusion": None,
    },
    "rings": {
        "ring 1": None, "ring 2": None,
    },
    "boons": {
        "list": ["boon_1", "boon_2", "boon_3", "boon_4"],
    },
    "spells": {
        1: "heal", 2: "fire_surge", 3: "icecrag_burst",
    },
    "values": {
        "estus level": 1,
        "souls": 0,
        "lost souls": 0,
        "active humanities": 0,
        "lost humanities": 0,
        "max estus": 3,
        "current estus": 3,
        "levelup cost": 1,
        "hollow": True,
    }
}

# Hidden numbers which can be affected by boons
player_data = {
    "dependent_variables": {"health": 400, "mana": 100, "stamina": 60, "equip load": 21.5,
        "max equip load": 54.0, "speed": 5, "poise": 42.1,"att. slots": 2, "attack": 10, "magic mult": 1,
        "stamina recovery": 0.2, "mana recovery": 0.005},

    "stamina_costs": {"weapon_usage": 5, "magic_usage": 4, "rolling": 15},

    "defense": {"physical def.": 128, "magic def.": 139, "fire def.": 125, "lightning def.": 132},
}

# Player inputs (mainly used for mouse)
player_inputs = {
    "light attack": False, "heavy attack": False, "skill": False, "cast spell": False, "roll": False, "scroll spell": False, "scroll direction": 0,
}

# Bonfire Data
bonfire_data = {
    0: {'kindle_level': 1, 'warp_target': True, 'warp_node': True, 'can_warp': False, 'active': False},
}

# Bonfire Menu Options
bonfire_menu_options = {
    "Leave": True, "Level Up": True, "Attune Magic": True, "Warp": False, "Kindle": True, "Use Humanity": True,
}

# UI Info
ui_data = {
    "HEALTH_BAR_WIDTH": player_data['dependent_variables']['health'] * 0.5,
    "STAMINA_BAR_WIDTH": player_data['dependent_variables']['stamina'] * 2,
    "MANA_BAR_WIDTH": player_data['dependent_variables']['mana'] * 1,
}

# Item Pickups
ground_item_list = [
    [0, "Humanity", 2],
    [0, "Estus Flask", 1],
    [0, "Darkmoon Seance Ring", 1],
    [0, "Titanite Shard", 2, "Green Titanite Shard", 1],
]

# Chests
chest_list = [0,0,0,0,0]

# Levers
# maybe add the effects?
lever_list = [0,0,0,0]

# Messages
message_list = {
    1: ["Be wary of beast. In,", "short, time for running."]
}