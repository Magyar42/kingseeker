# Data and information that is required by files as a reference #
# Information here is not altered during gameplay #

from gameinfo import *

# Setup
WIDTH    = 1280
HEIGHT   = 720
FPS      = 60
TILESIZE = 64
MM_COLOUR = "#121010"

HURTBOX_DEBUG = False
static_player_attacks = ["player_spin"]

# Main Menu
credits_info = [
    "== DEVELOPMENT ==",
    "Kristof 'MadeinCanada' Konig",
    "",
    "== GRAPHICAL ASSETS ==",
    "World sprites - Pixel-Boy & AAA",
    "UI sprites - Admurin",
    "Sprite edits - MadeinCanada",
    "Particle effects - Pixel-Boy & CodeManu",
    "",
    "== AUDIO ==",
    "Sound effects - Pixel-Boy & AAA",
    "Dark Souls sounds - FromSoftware [Dark Souls]",
    "Dark Souls 8-bit songs - Christopher Niskala",
    "",
    "== SPECIAL THANKS ==",
    "Clear Code on YouTube",
    "FromSoftware, for the creation of Dark Souls",
    "Supergiant Games, for the creation of Hades"
]

# UI Elements
BOSS_HP_WIDTH = 700
BOSS_HP_OFFSET = 80
BAR_HEIGHT = 20
ITEM_BOX_SIZE_BIG = 100
ITEM_BOX_SIZE = 80
ITEM_BOX_SIZE_SMALL = 60
UI_FONT = "assets/fonts/PublicPixel-z84yD.ttf"  # "assets/fonts/PublicPixel-z84yD.ttf"
BACKUP_FONT = "assets/fonts/joystix.ttf"
HUMANITY_BOX_WIDTH = 58
HUMANITY_BOX_HEIGHT = 58

UI_FONT_SIZE = 18
MAIN_MENU_FONT_SIZE = 20
MEDIUM_FONT_SIZE = 14
SMALL_FONT_SIZE = 12
TINY_FONT_SIZE = 10

# General Colours
WATER_COLOUR = "#71ddee"
UI_BG_COLOUR = "#222222"
UI_BG_LIGHT_COLOUR = "#696868"
UI_BORDER_COLOUR = "#111111"
TEXT_COLOUR = "#EEEEEE"
UI_SELECTED_COLOUR = "#5c3604"       #"#44190a"
COLOURKEY = "#ff2bf4"
HOVER_COLOUR= "#3e1403"
TEXT_BG_COLOUR = (17, 17, 17, 150)
TEXT_TITLE_COLOUR = "#FFF1D2"

# UI Colours
HEALTH_COLOUR = "#741E20"
HEALTH_COLOUR_GRADIENT = "#89272B"
STAMINA_COLOUR = "#346137"
STAMINA_COLOUR_GRADIENT = "#396B3D"
MANA_COLOUR = "#1C1E5D"
MANA_COLOUR_GRADIENT = "#272A7F"
UI_BORDER_COLOUR_ACTIVE = "#FF8208"
INV_BORDER = "#755E30"

# Weapon Data # todo: change for kingseeker
weapon_data = {
    "Broadsword": {"cooldown": 100, "damage": 15, "knockback": 2, "weight": 3},
}

# Boons Data
boon_data = {
    ## Warriors of Sunlight
    # Core Boons
    "boon_1": {"name": "Thunderous Roll", "category": "Warriors of Sunlight", "desc1": "Chain-lightning is emitted|when rolling.", "desc2": "", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_2": {"name": "Lightning Strike", "category": "Warriors of Sunlight", "desc1": "Primary/secondary attack emits|chain-lightning when damaging a foe.", "desc2": "Skews damage scaling towards FAITH.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_3": {"name": "Electrifying Skill", "category": "Warriors of Sunlight", "desc1": "Ability emits chain-lightning when damaging|a foe.", "desc2": "Skews damage scaling towards FAITH.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_4": {"name": "Sunlight Catalyst", "category": "Warriors of Sunlight", "desc1": "Gain the Sunlight Talisman capable of|casting Miracles.", "desc2": "Skews catalyst scaling towards FAITH.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    # General Boons
    "boon_5": {"name": "Vengeance of the Gods", "category": "Warriors of Sunlight", "desc1": "When taking damage, there is a 25% chance of|releasing a shockwave.", "desc2": "", "subboons": ["boon_9", "boon_10"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_6": {"name": "King of the Storm", "category": "Warriors of Sunlight", "desc1": "Chain-lighting effects bounce 2 more times.", "desc2": "", "subboons": ["boon_11", "boon_12"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_7": {"name": "Protection of the Sun", "category": "Warriors of Sunlight", "desc1": "Ability is replaced by Soothing Sunlight,|fully restoring health when used.", "desc2": "", "subboons": ["boon_13", "boon_14"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_8": {"name": "Unrelenting Drive", "category": "Warriors of Sunlight", "desc1": "Killing an enemy while health is at 100%|boosts damage by 2% for 4s.", "desc2": "This effect can stack up to 5 times.", "subboons": ["boon_15", "boon_16"], "is_subboon": False, "cat": "Boon", "parent": None},

    # Sub Boons
    "boon_9": {"name": "Empowered Faith", "category": "Warriors of Sunlight", "desc1": "Increases shockwave chance by 50% and|shockwave size by 25%.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_5"},
    
    "boon_10": {"name": "Divine Drivel", "category": "Warriors of Sunlight", "desc1": "Enemies hit by shockwaves are stunned for|1s.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_5"},

    "boon_11": {"name": "Repulsion", "category": "Warriors of Sunlight", "desc1": "Each chain-lightning effect's damage|increases per bounce.", "desc2": "The final hit from a chain-lightning effect|releases a small shockwave.", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_6"},
    
    "boon_12": {"name": "Electrifying Deflection", "category": "Warriors of Sunlight", "desc1": "Enemies hit by chain-lighting have a 25% of|being stunned for 1s.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_6"},

    "boon_13": {"name": "Deepened Devotion", "category": "Warriors of Sunlight", "desc1": "Soothing Sunlight also fully restores mana|and stamina.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_7"},
    
    "boon_14": {"name": "Holy Protection", "category": "Warriors of Sunlight", "desc1": "Increases defense and speed by 30% for 6s after use.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_7"},

    "boon_15": {"name": "Benevolence", "category": "Warriors of Sunlight", "desc1": "Health threshold reduced to 75%.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_8"},

    "boon_16": {"name": "Stormclouds", "category": "Warriors of Sunlight", "desc1": "Effect also extends stunned duration by 0.5s.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_8"},
}

# Boon Categories
boons_core = {
    "warriors_of_sunlight": {
        "list": ["boon_1", "boon_2", "boon_3", "boon_4"]
    },
}

# Velka's Blessings # todo: finish
velka_boons = {
    # Modifiers 
    "general_modifiers": {
        "list": None
    },
    "warriors_of_sunlight_modifiers": {
        "list": ["wos_chain_lightning", "wos_stunned", "wos_shockwave", "wos_weapon_faith", "wos_catalyst_faith"]
    },
    "chaos_servants_modifiers": {
        "list": None
    },
    "darkwraiths_modifiers": {
        "list": None
    },
    "blades_of_the_darkmoon_modifiers": {
        "list": None
    },

    # Spells
    "warriors_of_sunlight_spells": {
        "list": ["bountiful_light", "wrath_of_the_gods", "lightning_spear", "white_corona", "lightning_stake"]
    },
    "chaos_servants_spells": {
        "list": None
    },
    "darkwraiths_spells": {
        "list": None
    },
    "blades_of_the_darkmoon_spells": {
        "list": None
    },
}

# Attack Hurtboxes # x offset from player|y offset from player|width|height
attack_hurtbox_data = {
    "down":{
        "player_spin": {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
        },
        "sword_1": {
            0: [[64, 0, 64, 64]],
            1: [[-64, 0, 64, 64], [-32, 64, 128, 64]],
            2: [],
            3: [],
            4: [],
            5: [],
        },
        "sword_2": {
            0: [],
            1: [[16, 64, 32, 64], [16, 128, 32, 64]],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
        },
        "sword_skill": {
            0: [],
            1: [[64, 0, 64, 64]],
            2: [[-64, 0, 64, 64], [-32, 64, 128, 64]],
            3: [[0, -64, 64, 64], [-64, -32, 64, 128]],
            4: [[64, 0, 64, 64], [-32, -64, 128, 64]],
            5: [[0, 64, 64, 64], [64, -32, 64, 128]],
            6: [],
            7: [],
            8: [],
        },
    },
    "up":{
        "player_spin": {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
        },
        "sword_1": {
            0: [[-64, 0, 64, 64]],
            1: [[64, 0, 64, 64], [-32, -64, 128, 64]],
            2: [],
            3: [],
            4: [],
            5: [],
        },
        "sword_2": {
            0: [],
            1: [[16, -64, 32, 64], [16, -128, 32, 64]],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
        },
        "sword_skill": {
            0: [],
            1: [[-64, 0, 64, 64]],
            2: [[64, 0, 64, 64], [-32, -64, 128, 64]],
            3: [[0, 64, 64, 64], [64, -32, 64, 128]],
            4: [[-64, 0, 64, 64], [-32, 64, 128, 64]],
            5: [[0, -64, 64, 64], [-64, -32, 64, 128]],
            6: [],
            7: [],
            8: [],
        },
    },
    "left":{
        "player_spin": {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
        },
        "sword_1": {
            0: [[0, 64, 64, 64]],
            1: [[0, -64, 64, 64], [-64, -32, 64, 128]],
            2: [],
            3: [],
            4: [],
            5: [],
        },
        "sword_2": {
            0: [],
            1: [[-64, 16, 64, 32], [-128, 16, 64, 32]],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
        },
        "sword_skill": {
            0: [],
            1: [[0, 64, 64, 64]],
            2: [[0, -64, 64, 64], [-64, -32, 64, 128]],
            3: [[64, 0, 64, 64], [-32, -64, 128, 64]],
            4: [[0, 64, 64, 64], [64, -32, 64, 128]],
            5: [[-64, 0, 64, 64], [-32, 64, 128, 64]],
            6: [],
            7: [],
            8: [],
        },
    },
    "right":{
        "player_spin": {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
        },
        "sword_1": {
            0: [[0, -64, 64, 64]],
            1: [[0, 64, 64, 64], [64, -32, 64, 128]],
            2: [],
            3: [],
            4: [],
            5: [],
        },
        "sword_2": {
            0: [],
            1: [[64, 16, 64, 32], [128, 16, 64, 32]],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
        },
        "sword_skill": {
            0: [],
            1: [[0, -64, 64, 64]],
            2: [[0, 64, 64, 64], [64, -32, 64, 128]],
            3: [[-64, 0, 64, 64], [-32, 64, 128, 64]],
            4: [[0, -64, 64, 64], [-64, -32, 64, 128]],
            5: [[64, 0, 64, 64], [-32, -64, 128, 64]],
            6: [],
            7: [],
            8: [],
        },
    },
}

# Magic Data # todo: change for kingseeker
magic_data = {
    "fire_surge": {"strength": 12, "cost": 20, "type": "Pyromancy"},
    "heal": {"strength": 20, "cost": 20, "type": "Miracle"},
    "icecrag_burst": {"strength": 9, "cost": 24, "type": "Sorcery"},
}

# Enemy Data # todo: change for kingseeker
enemy_data = {
    'squid': {'health': 100,'xp':250,'damage':90,'attack_type': 'slash', 'attack_sound':'assets/audio/sfx/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300,'xp':500,'damage':130,'attack_type': 'claw',  'attack_sound':'assets/audio/sfx/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100,'xp':250,'damage':100,'attack_type': 'thunder', 'attack_sound':'assets/audio/sfx/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70,'xp':200,'damage':80,'attack_type': 'leaf_attack', 'attack_sound':'assets/audio/sfx/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300},

    'undead_warrior': {'health': 75, 'defense': 0.25, 'poise': 4, 'xp': 200,'damage': 40,
                       'attack_type': 'slash', 'attack_sound':'assets/audio/sfx/attack/slash.wav', 'speed': 4, 'attack_radius': 100, 'notice_radius': 200},
}

# Pop-ups
current_prompts = []
PROMPT_HEIGHT = 20
PROMPT_GAP = 10
PROMPT_FONT_SIZE = 14

# Upgrade Menu
UPGRADE_TEXT_COLOUR_SELECTED = "#111111"
UPGRADE_TEXT_COLOUR = "#EEEEEE"
BAR_COLOUR = "#EEEEEE"
BAR_COLOUR_SELECTED= "#111111"
UPGRADE_BG_COLOUR_SELECTED = "#EEEEEE"

# Hitbox Offset
HITBOX_OFFSET = {
    "player": -26,
    "object": -40,
    "grass": -10,
    "invisible": 0,
}

# Misc
covenants = ["warriors_of_sunlight", "chaos_servants", "darkwraiths", "blades_of_the_darkmoon", "velka"]
npc_list = ["389", "367", "345", "323", "301", "279", "257", "368", "346", "324", "302", "280", "258", "369", "347", "325", "303", "281", "259", "366", "344"]
pillar_list = ["386", "364", "342", "320", "298"]
boon_summons = ["sunlight_summon", "chaos_summon", "darkwraith_summon", "darkmoon_summon", "velkas_tome"]
resources_names = ["soul_remnants", "humanity sprites", "souvenirs of reprisal", "sunlight medals", "titanite shards", "titanite chunks", "titanite slabs", "demon titanite"]

# Region Values
region_values = {
    "undead_burg": "0",
    "undead_parish": "1",
    "the_depths": "2",
    "blighttown": "3",
    "catacombs": "4",
    "valley_of_drakes": "5",
    "new_londo_ruins": "6",
}

# Chamber Details
NUM_CHAMBERS_PER_REGION = 4
chambers_per_region = {
    # Chambers which can be randomly loaded [starting/ending chambers of each area are NOT included]
    "firelink_shrine": [""],
    "undead_burg": ["097", "098"],
    "undead_parish": [""],
    "the_depths": [""],
}
safe_rooms = [
    "000","099", "101," "199", "201", "299"
]
reward_first_rooms = [
    "001"
]
# X01 is the START room for each region
# X99 is the END room for each region

# Chamber Rewards
chamber_rewards = { # todo: make sure of the chance section
    # "great_soul": { "chance": 1, "min": 2000, "max": 5000 },
    # "humanity": { "chance": 1, "min": 2, "max": 5 },
    # "titanite_chunk": { "chance": 0.75, "min": 2, "max": 3 },
    # "demon_titanite": { "chance": 0.75, "min": 2, "max": 4 },

    "sunlight_summon": { "chance": 0.75, "min": 1, "max": 1 },
    # "darkwraith_summon": { "chance": 0.75, "min": 1, "max": 1 },
    # "chaos_summon": { "chance": 0.75, "min": 1, "max": 1 },
    # "darkmoon_summon": { "chance": 0.75, "min": 1, "max": 1 },
    # "velkas_tome": { "chance": 0.5, "min": 1, "max": 1 },

    # "vendor": { "chance": 0.5, "min": 1, "max": 1 },
}

# Gifts of Humanity - Values
humanity_gifts_defines = {
    "1": [200, 400, 600, 800, 1000],
    "2": [1, 2, 3, 4, 5],
    "3": [1, 2, 3],
    "4": [0, 1000, 2000, 3000, 4000],
    "5": [1, 1.10, 1.20, 1.30, 1.40],
    "6": [1, 1.10, 1.20, 1.30, 1.40],
}

# Gifts of Humanity - Costs [in humanity sprites]
humanity_gifts_costs = {
    "1": [0, 5, 10, 15, 20],
    "2": [0, 3, 6, 12, 24],
    "3": [0, 10, 20],
    "4": [0, 2, 4, 6, 8, 10],
    "5": [1, 6, 10, 14, 18, 22],
    "6": [1, 5, 10, 15, 20, 30],
}

# Gifts of Humanity - Text
humanity_gifts_text = {
    "1": { "name": "Inner Humanity", "desc": "test description! sigma sigma on the wall" },
    "2": { "name": "Enkindled Flames", "desc": "test description! sigma sigma on the wall" },
    "3": { "name": "Greater Attunement", "desc": "test description! sigma sigma on the wall" },
    "4": { "name": "Empowered Soul", "desc": "test description! sigma sigma on the wall" },
    "5": { "name": "Flourishing Boldness", "desc": "test description! sigma sigma on the wall" },
    "6": { "name": "Firm Resistance", "desc": "test description! sigma sigma on the wall" },
}

# Resource Info
resource_details = {
    "soul remnants": ["Level-up Resource", "", ">Gained after death.|>Spending Souls on levelling up increases|the amount of Soul Remnants gained.|>Can be spent on permanent level-ups.", "Souls are present in all living things, and a|powerful soul requires many to have be defeated."],

    "humanity sprites": ["Level-up Resource | Covenant Offering", "", ">Dropped by some enemies.|>Found in various locations.|>Can be spent on permanent unique bonuses|in several ways.", "Rare black sprite found on human remains. Thought|to be somehow distinct from the soul."],

    "souvenirs of reprisal": ["Covenant Offering", "Blood-drained, shrunken ear. Souvenir taken from subduing the guilty.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be offered to the Blades of the Darkmoon|to increase Covenant rank."],
    "sunlight medals": ["Covenant Offering", "Warm medal, engraved with the symbol of the Sun. Represents Lord Gwyn's firstborn, who lost the status of deity.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be offered to the Warriors of Sunlight to|increase Covenant rank."],
    "eyes of death": ["Covenant Offering", "Eyes taken from those afflicted by curses of petrification. Known to be used to spread death.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be offered to the Gravelord Servants to|increase Covenant rank."],
    "dragon scales": ["Covenant Offering", "Scales peeled from an ancient dragon. Highly sought after for its rarity.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be offered to the Path of the Dragon to|increase Covenant rank."],
    "titanite shards": ["Upgrade Material", "Most common titanite material. Etched into weapons for reinforcement.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be used to strengthen standard weapons|to +3."],
    "large titanite shards": ["Upgrade Material", "Larger and rarer titanite material. Etched into weapons for reinforcement.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be used to strengthen standard weapons|to +6."],
    
    "titanite chunks": ["Upgrade Material", "", ">Found in various locations.|>Can be bought from various vendors.|>Can be used to permanently upgrade|standard weapons.", "Titanite is the heirloom of a nameless blacksmith|deity. All that remains are fragments and shards."],

    "titanite slabs": ["Upgrade Material", "Legendary titanite material of a nameless blacksmith deity. Etched into weapons for reinforcement.", ">Can be found in chambers.|Can be gained from defeating strong enemies.", "Can be used to strengthen standard weapons|to +10 and demon/twinkling weapons to +5."],

    "demon titanite": ["Upgrade Material", "", ">Dropped by Titanite Demons.|>Can be bought from various vendors.|>Can be used to permanently upgrade|infernal weapons.", "Great beasts arose from slabs of Titanite after the|blacksmith deity's death."],

    "twinkling titanite": ["Upgrade Material", "Titanite imbued with a particularly powerful energy of unknown origin.", "Can be found in chambers.|Can be gained from defeating strong enemies.", "Can be used to strengthen twinkling weapons|to +4."],
}

# UI Info
ui_data = {
    "HEALTH_BAR_WIDTH": player_data['dependent_variables']['health'] * 0.5,
    "STAMINA_BAR_WIDTH": player_data['dependent_variables']['stamina'] * 2,
    "MANA_BAR_WIDTH": player_data['dependent_variables']['mana'] * 1,
}