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
    # Level 1
    "boon_1": {"name": "Lightning Step", "category": "Warriors of Sunlight", "desc1": "Moving into foes inflicts weak lightning|damage.", "desc2": "Scales with FAITH", "lvl": "LVL 1"},
    "boon_2": {"name": "Primary Infusion: Lightning", "category": "Warriors of Sunlight", "desc1": "Primary attack emits chain lightning when|damaging a foe.", "desc2": "Scales with FAITH", "lvl": "LVL 1"},
    "boon_3": {"name": "Secondary Infusion: Lightning", "category": "Warriors of Sunlight", "desc1": "Secondary attack causes a lightning|bolt to strike nearby foes.", "desc2": "Scales with FAITH", "lvl": "LVL 1"},
    "boon_4": {"name": "Catalyst Infusion: Lightning", "category": "Warriors of Sunlight", "desc1": "Transforms catalyst into a talisman|capable of casting divine miracles.", "desc2": "Scales with FAITH", "lvl": "LVL 1"},
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
covenants = ["warriors_of_sunlight", "chaos_servants", "darkwraiths", "blades_of_the_darkmoon"]
npc_list = ["389", "367", "345", "323", "301", "279", "257", "368", "346", "324", "302", "280", "258", "369", "347", "325", "303", "281", "259", "366", "344"]

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
NUM_CHAMBERS_PER_REGION = 3
chambers_per_region = {
    # Chambers which can be randomly loaded [starting chambers of each area are NOT included]
    "undead_burg": ["001", "002"],
    "undead_parish": [""],
    "the_depths": [""],
}
safe_rooms = [
    "000", "099", "100," "199", "200", "299"
]
# X00 is the START room for each region
# X99 is the END room for each region

# Chamber Rewards
chamber_rewards = { # todo: make sure of the chance section
    "humanity": { "chance": 1, "min": 2, "max": 5 },
    "great_soul": { "chance": 1, "min": 2000, "max": 5000 },
    "titanite_shard": { "chance": 1, "min": 2, "max": 4 },
    "titanite_chunk": { "chance": 0.75, "min": 2, "max": 3 },
    "titanite_slab": { "chance": 0.25, "min": 1, "max": 1 },
    "demon_titanite": { "chance": 0.75, "min": 2, "max": 4 },
    "sunlight_medal": { "chance": 1, "min": 2, "max": 4 },
    "souvenir_of_reprisal": { "chance": 1, "min": 2, "max": 4 },

    "sunlight_summon": { "chance": 0.75, "min": 1, "max": 1 },
    "darkwraith_summon": { "chance": 0.75, "min": 1, "max": 1 },
    "chaos_summon": { "chance": 0.75, "min": 1, "max": 1 },
    "darkmoon_summon": { "chance": 0.75, "min": 1, "max": 1 },
    "velkas_tome": { "chance": 0.5, "min": 1, "max": 1 },

    "vendor": { "chance": 0.5, "min": 1, "max": 1 },
}