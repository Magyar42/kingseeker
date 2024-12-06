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

# Boss Data # todo: change for kingseeker
boss_data = {
    'asylum_demon': {
        'health': 800,
        'xp': 2000,
        'damage': 20,
        'attack_type': 'slash',
        'attack_sound': 'assets/audio/sfx/attack/slash.wav',
        'speed': 2,
        'resistance': 100,
        'attack_radius': 100,
        'notice_radius': 500,
        'attack_types': ['slam', 'swing', 'swing_down', 'fly'],
        'drops': ["Humanity", 1, "Big Pilgrim's Key", 1],
    },
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

# Decision Data
RESTORE_HUMANITY_TEXT = "Offer humanity and undo Hollowing?"
KINDLE_TEXT = "Offer humanity and kindle flame?"
ALREADY_HUMAN_TEXT = "You are already in Human form."
NEED_HUMANITY_TEXT = "You do not have any humanity."
REQUIRES_HUMAN_TEXT = "Must be in Human form."
CANNOT_KINDLE = "Cannot kindle flame further."

# misc
covenants = ["warriors_of_sunlight", "chaos_servants", "darkwraiths", "blades_of_the_darkmoon", "velka"]
npc_list = ["389", "367", "345", "323", "301", "279", "257", "368", "346", "324", "302", "280", "258", "369", "347", "325", "303", "281", "259", "366", "344"]
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

    # "souvenir_of_reprisal": { "chance": 1, "min": 2, "max": 4 },
    # "sunlight_medal": { "chance": 1, "min": 2, "max": 4 },

    # "titanite_shard": { "chance": 1, "min": 2, "max": 4 },
    # "titanite_chunk": { "chance": 0.75, "min": 2, "max": 3 },
    # "titanite_slab": { "chance": 0.25, "min": 1, "max": 1 },
    # "demon_titanite": { "chance": 0.75, "min": 2, "max": 4 },

    "sunlight_summon": { "chance": 0.75, "min": 1, "max": 1 },
    # "darkwraith_summon": { "chance": 0.75, "min": 1, "max": 1 },
    # "chaos_summon": { "chance": 0.75, "min": 1, "max": 1 },
    # "darkmoon_summon": { "chance": 0.75, "min": 1, "max": 1 },
    # "velkas_tome": { "chance": 0.5, "min": 1, "max": 1 },

    # "vendor": { "chance": 0.5, "min": 1, "max": 1 },
}