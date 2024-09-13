# Data and information that is updated and changed as gameplay progresses #
# Information is saved to and loaded from here #

## TODO: CHANGE THE WHOLE FILE FOR KINGSEEKER

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
    "eyes of death": 3,
    "dragon scales": 7,

    "titanite shards": 4,
    "large titanite shards": 5,
    "titanite chunks": 3,
    "titanite slabs": 0,
    "demon titanite": 1,
    "twinkling titanite": 2,
}

# Covenant Ranks
covenant_ranks = {
    "warriors of sunlight": 0,
    "blades of the darkmoon": 0,
    "darkwraiths": 0,
    "chaos servants": 0,
    "gravelord servants": 0,
    "path of the dragon": 0,
    "royal guard": 0,
    "way of white": 0,
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
    "main weapon": {
        "class": "sword", "weapon": "broadsword", "cooldown": None, "base damage": None, "weight": None, "effects": None, "infusion": None,
    },
    "catalyst": {
        "class": "pyromancy", "weapon": "pyromancy flame", "cooldown": None, "base damage": None, "weight": None, "effects": None, "infusion": None,
    },
    "weapon skill": {
        "skill": "basic_thrust", "cooldown": None, "base damage": None, "effects": None, "infusion": None,
    },
    "rings": {
        "ring 1": None, "ring 2": None,
    },
    "boons": {
        "boon 1:": None, "boon 2:": None, "boon 3:": None, "boon 4:": None, "boon 5:": None, "boon 6:": None, "boon 7:": None
    },
    "spells": {
        "spell 1": None, "spell 2": None, "spell 3": None, "spell 4": None, "spell 5": None
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
    }
}

# Hidden numbers which can be affected by boons
player_data = {
    "dependent_variables": {"health": 400, "mana": 40, "stamina": 60, "equip load": 21.5,
        "max equip load": 54.0, "speed": 5, "poise": 42.1,"att. slots": 2, "attack": 10, "magic damage": 4,
        "stamina recovery": 0.2, "mana recovery": 0.005},

    "stamina_costs": {"weapon_usage": 5, "magic_usage": 4, "rolling": 15},

    "defense": {"physical def.": 128, "magic def.": 139, "fire def.": 125, "lightning def.": 132},
}

# Player inputs (mainly used for mouse)
player_inputs = {
    "light attack": False, "heavy attack": False, "skill": False, "cast spell": False, "roll": False,
}


### below is old dark soles stuff ###
# # Player Stats # todo: comment out and use new sections
player_data = {
    "values": {"level": 7, "souls": 0, "humanity": 3, "lost_souls": 0, "lost_humanity": 0,
    "levelup_cost": 1},
    
    "dependent_variables": {"health": 400, "mana": 40, "stamina": 60, "equip load": 21.5,
        "max equip load": 54.0, "speed": 5, "poise": 42.1,"att. slots": 2, "attack": 10, "magic damage": 4,
        "stamina recovery": 0.2, "mana recovery": 0.005},

    "stamina_costs": {"weapon_usage": 5, "magic_usage": 4, "rolling": 15},
    
    "attributes": {"VITALITY": 11, "ATTUNEMENT": 8, "ENDURANCE": 9, "STRENGTH": 12, "PERCEPTION": 6},

    "defense": {"physical def.": 128, "magic def.": 139, "fire def.": 125, "lightning def.": 132},

    "resistances": {"poise": 0, "bleed res": 100, "poison res": 80, "curse res": 90, "discovery": 120},
    
    "status": {"name": "John Dark", "hollow": True, "estus": 5, "current_estus": 7, "estus_level": 1, "covenant": "None"},
    
    "unlocks": {"rite_of_kindling": False, "lordvessel": False, "bell_1": False, "bell_2": False},
}


# Bonfire Data
bonfire_data = {
    0: {'kindle_level': 1, 'warp_target': True, 'warp_node': True, 'can_warp': False, 'active': False},
}

# Bonfire Menu Options
bonfire_menu_options = {
    "Leave": True, "Level Up": True, "Attune Magic": True, "Warp": False, "Kindle": True, "Use Humanity": True,
}

# Inventory
player_inventory = {
    "Consumables": ["Darksign", "Estus Flask", "Humanity"],
    "Ores": ["Titanite Shard", "Green Titanite Shard"],
    "Key Items": [],
    "Spells": ["Fire Surge", "Heal", "Icecrag Burst"],
    "Weapons": ["Broadsword", "Ricard's Rapier", "Winged Spear", "Giant Hammer", "Dagger", "Sorcerer's Catalyst", "Tower Kite Shield"],
    "Armour": ["Knight Armour"],
    "Rings": ["Ring of Favour and Protection", "Tiny Being's Ring"],

    "Consumables_num": [1, player_data['status']['current_estus'], 3],
    "Ores_num": [11, 2],
    "Key Items_num": [],
    "Spells_num": [1, 1, 1],
    "Weapons_num": [1, 1, 1, 1, 1, 1, 1],
    "Armour_num": [1],
    "Rings_num": [1, 1],
}

# Item Dictionary
game_items = {
    # Consumables
    "Estus Flask": {
        "short_desc": "Fill with Estus at Bonfire. Fills HP.",
        "short_desc2": "The Undead treasure these dull green flasks.",
        "max": 20,
        "category": "Consumables",
    },
    "Humanity": {
        "short_desc": "Rare tiny black sprite found on corpses.",
        "short_desc2": "Use to gain 1 humanity and restore HP.",
        "max": 99,
        "category": "Consumables",
    },
    "Darksign": {
        "short_desc": "The Darksign signifies an accursed Undead.",
        "short_desc2": "Those branded with it are reborn after death.",
        "max": 1,
        "category": "Consumables",
    },
    # Armour
    "Knight Armour": {
        "short_desc": "Equipment of a lower rank knight. Despite the",
        "short_desc2": "thin metal, the grooves give added protection.",
        "max": 1,
        "category": "Armour",
    },
    # Rings
    "Ring of Favour and Protection": {
        "short_desc": "A ring symbolizing the favour and",
        "short_desc2": "protection of the goddess Fina.",
        "max": 1,
        "category": "Rings",
    },
    "Tiny Being's Ring": {
        "short_desc": "Ring made of an ancient tiny red jewel.",
        "short_desc2": "Grants small increase to HP.",
        "max": 1,
        "category": "Rings",
    },
    "Darkmoon Seance Ring": {
        "short_desc": "Ring given to disciples of the Darkmoon deity.",
        "short_desc2": "Grants an extra magic attunement slot.",
        "max": 1,
        "category": "Rings",
    },
    # Ores
    "Titanite Shard": {
        "short_desc": "Most common material for weapon reinforcement.",
        "short_desc2": "Reinforce standard weapons to +5.",
        "max": 99,
        "category": "Ores",
    },
    "Green Titanite Shard": {
        "short_desc": "Titanite shard imbued with special power.",
        "short_desc2": "Reinforce magic and divine weapons to +5.",
        "max": 99,
        "category": "Ores",
    },
    # Weapons
    "Broadsword": {
        "short_desc": "The blade of this sword emphasizes slicing.",
        "short_desc2": "Very effective against multiple enemies.",
        "max": 1,
        "category": "Weapons",
    },
    "Ricard's Rapier": {
        "short_desc": "A rapier with intricate decorations.",
        "short_desc2": "Weapon of the famous Undead Prince Ricard.",
        "max": 1,
        "category": "Weapons",
    },
    "Winged Spear": {
        "short_desc": "Long weapon effective against hard exteriors.",
        "short_desc2": "But the radius is blocked easily by shields.",
        "max": 1,
        "category": "Weapons",
    },
    "Giant Hammer": {
        "short_desc": "Wooden hammer wielded by the Giant Blacksmith.",
        "short_desc2": "Used for forging, but still quite powerful.",
        "max": 1,
        "category": "Weapons",
    },
    "Dagger": {
        "short_desc": "This dagger has only a modest attack, but",
        "short_desc2": "can be jabbed in rapid succession.",
        "max": 1,
        "category": "Weapons",
    },
    "Sorcerer's Catalyst": {
        "short_desc": "Catalyst used by sorcerers of Vinheim",
        "short_desc2": "Dragon School.",
        "max": 1,
        "category": "Weapons",
    },
    "Tower Kite Shield": {
        "short_desc": "Medium shield decorated with a tower,",
        "short_desc2": "the symbol of protection.",
        "max": 1,
        "category": "Weapons",
    },
    # Spells
    "Fire Surge": {
        "short_desc": "A pyromancy originating from a faraway land.",
        "short_desc2": "Creates static fireballs on two tiles.",
        "max": 1,
        "category": "Spells",
    },
    "Heal": {
        "short_desc": "Say a prayer to be blessed by its revelations.",
        "short_desc2": "Restores a small amount of health.",
        "max": 1,
        "category": "Spells",
    },
    "Icecrag Burst": {
        "short_desc": "Draw from the essence of the soul for power.",
        "short_desc2": "Summons a row of icy crystals.",
        "max": 1,
        "category": "Spells",
    },
    # Key Items
    "Dungeon Cell Key": {
        "short_desc": "Key to the dungeon of the Undead Asylum",
        "short_desc2": "to the North.",
        "max": 1,
        "category": "Key Items",
    },
    "Big Pilgrim's Key": {
        "short_desc": "Key to the inner door of the Undead Asylum",
        "short_desc2": "main hall. Belongs to a Chosen Undead.",
        "max": 1,
        "category": "Key Items",
    },
}

## Player Data ##
# Quick Items Data
qitems_data = {
    "slot1": {"item": "Estus Flask", "amount": player_inventory['Consumables_num'][1], "graphic": "assets/graphics/inventory/items/Consumables/Estus Flask.png"},
    "slot2": {"item": "Humanity", "amount": player_inventory['Consumables_num'][2], "graphic": "assets/graphics/inventory/items/Consumables/Humanity.png"},
    "slot3": {"item": "Darksign", "amount": 1, "graphic": "assets/graphics/inventory/items/Consumables/Darksign.png"},
    "slot4": {"item": None, "amount": 1, "graphic": "assets/graphics/inventory/items/None.png"},
    # "slot5": {"item": None, "amount": 11, "graphic": "assets/graphics/inventory/items/None.png"},
}
# Current Right Hand
right_hand_data = {
    "slot1": {"item": None, "cooldown": None, "damage": None, "knockback": None, "weight": None, "graphic": None},
    "slot2": {"item": None, "cooldown": None, "damage": None, "knockback": None, "weight": None, "graphic": None},
}
# Current Left Hand
left_hand_data = {
    "slot1": {"item": None, "cooldown": None, "damage": None, "knockback": None, "weight": None, "type": [], "graphic": None},
    "slot2": {"item": None, "cooldown": None, "damage": None, "knockback": None, "weight": None, "type": [], "graphic": None},
}
# Attuned Spells
attuned_spells_data = {
    "slot1": {"spell": None, "strength": None, "cost": None, "weight": None, "type": None, "graphic": None},
    "slot2": {"spell": None, "strength": None, "cost": None, "weight": None, "type": None, "graphic": None},
}
# Rings Data
ring_data = {
    "slot1": {"item": "Ring of Favour and Protection", "graphic": "assets/graphics/inventory/items/Rings/Ring of Favour and Protection.png"},
    "slot2": {"item": "Tiny Being's Ring", "graphic": "assets/graphics/inventory/items/Rings/Tiny Being's Ring.png"},
    "slot3": {"item": None, "graphic": None},
}
player_armour = {
    "slot1": {"item": "Knight Armour", "defense": 10, "weight": 22, "graphic": "assets/graphics/inventory/items/Armour/Knight Armour.png"}   
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