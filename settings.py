# Data and information that is required by files as a reference #
# Information here is not altered during gameplay #

from gameinfo import *

CONTROLLER_ACTIVE = False
controller_list = []
CURRENT_CONTROLLER = None

# Setup
WIDTH    = 1280
HEIGHT   = 720
FPS      = 60
TILESIZE = 64
MM_COLOUR = "#121010"

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
ITEM_BOX_SIZE = 80
ITEM_BOX_SIZE_SMALL = 60
UI_FONT = "assets/fonts/PublicPixel-z84yD.ttf"
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
UI_BORDER_COLOUR = "#111111"
TEXT_COLOUR = "#EEEEEE"
UI_SELECTED_COLOUR = "#EEEEEE"       #"#44190a"
COLOURKEY = "#ff2bf4"
HOVER_COLOUR= "#3e1403"
TEXT_BG_COLOUR = (17, 17, 17, 150)

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
    "boon_1": {"name": "Core Boon: Thunderous Roll", "category": "Warriors of Sunlight", "desc1": "Chain-lightning is emitted when rolling.", "desc2": "", "subboons": None, "is_subboon": False},

    "boon_2": {"name": "Core Boon: Lightning Strike", "category": "Warriors of Sunlight", "desc1": "Primary/secondary attack emits chain-lightning|when damaging a foe.", "desc2": "Skews damage scaling towards FAITH.", "subboons": None, "is_subboon": False},

    "boon_3": {"name": "Core Boon: Electrifying Skill", "category": "Warriors of Sunlight", "desc1": "Ability emits chain-lightning when damaging|a foe.", "desc2": "Skews damage scaling towards FAITH.", "subboons": None, "is_subboon": False},

    "boon_4": {"name": "Core Boon: Sunlight Catalyst", "category": "Warriors of Sunlight", "desc1": "Gain the Sunlight Talisman capable of|casting Miracles.", "desc2": "Skews catalyst scaling towards FAITH.", "subboons": None, "is_subboon": False},

    # General Boons
    "boon_5": {"name": "Vengeance of the Gods", "category": "Warriors of Sunlight", "desc1": "When taking damage, there is a 25% chance of|releasing a shockwave.", "desc2": "", "subboons": ["boon_9", "boon_10"], "is_subboon": False},

    "boon_6": {"name": "King of the Storm", "category": "Warriors of Sunlight", "desc1": "Chain-lighting effects bounce 2 more times.", "desc2": "", "subboons": ["boon_11", "boon_12"], "is_subboon": False},

    "boon_7": {"name": "Protection of the Sun", "category": "Warriors of Sunlight", "desc1": "Ability is replaced by Soothing Sunlight,|fully restoring health when used.", "desc2": "", "subboons": ["boon_13", "boon_14"], "is_subboon": False},

    "boon_8": {"name": "Unrelenting Drive", "category": "Warriors of Sunlight", "desc1": "Killing an enemy while health is at 100%|boosts damage by 2% for 4s.", "desc2": "This effect can stack up to 5 times.", "subboons": ["boon_15", "boon_16"], "is_subboon": False},

    # Sub Boons
    "boon_9": {"name": "Empowered Faith", "category": "Warriors of Sunlight", "desc1": "Increases shockwave chance to 75%.", "desc2": "Increases shockwave size by 25%.", "subboons": None, "is_subboon": True},
    
    "boon_10": {"name": "Divine Drivel", "category": "Warriors of Sunlight", "desc1": "Enemies hit by shockwaves are stunned for 1s.", "desc2": "", "subboons": None, "is_subboon": True},

    "boon_11": {"name": "Repulsion", "category": "Warriors of Sunlight", "desc1": "Each chain-lightning effect's damage increases per bounce.", "desc2": "The final hit from a chain-lightning effect releases a|small AoE shockwave.", "subboons": None, "is_subboon": True},
    
    "boon_12": {"name": "Electrifying Deflection", "category": "Warriors of Sunlight", "desc1": "Enemies hit by chain-lighting have a 25% of being stunned|for 1s.", "desc2": "", "subboons": None, "is_subboon": True},

    "boon_13": {"name": "Deepened Devotion", "category": "Warriors of Sunlight", "desc1": "Soothing Sunlight also fully restores mana and stamina.", "desc2": "", "subboons": None, "is_subboon": True},
    
    "boon_14": {"name": "Holy Protection", "category": "Warriors of Sunlight", "desc1": "Increases defense and speed by 30% for 6s after use.", "desc2": "", "subboons": None, "is_subboon": True},

    "boon_15": {"name": "Benevolence", "category": "Warriors of Sunlight", "desc1": "Health threshold reduced to 75%.", "desc2": "", "subboons": None, "is_subboon": True},

    "boon_16": {"name": "Stormclouds", "category": "Warriors of Sunlight", "desc1": "Effect also extends stunned duration by 0.5s.", "desc2": "", "subboons": None, "is_subboon": True},
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

# Magic Data # todo: change for kingseeker
magic_data = {
    "fire_surge": {"strength": 12, "cost": 10, "type": "Pyromancy"},
    "heal": {"strength": 5, "cost": 8, "type": "Miracle"},
    "icecrag_burst": {"strength": 9, "cost": 14, "type": "Sorcery"},
}

# Enemy Data # todo: change for kingseeker
enemy_data = {
    'squid': {'health': 100,'xp':250,'damage':90,'attack_type': 'slash', 'attack_sound':'assets/audio/sfx/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300,'xp':500,'damage':130,'attack_type': 'claw',  'attack_sound':'assets/audio/sfx/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100,'xp':250,'damage':100,'attack_type': 'thunder', 'attack_sound':'assets/audio/sfx/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70,'xp':200,'damage':80,'attack_type': 'leaf_attack', 'attack_sound':'assets/audio/sfx/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300},
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
PROMPT_HEIGHT = 30
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
covenants = ["warriors_of_sunlight", "chaos_servants", "gravelord_servants", "darkwraiths", "blades_of_the_darkmoon", "path_of_the_dragon", "royal_guard", "way_of_white"]
npc_list = ["389", "367", "345", "323", "301", "279", "257", "368", "346", "324", "302", "280", "258", "369", "347", "325", "303", "281", "259", "366"]