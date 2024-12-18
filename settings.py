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

# Weapon Data
weapon_data = {
    "test": {"cooldown": 100, "damage": 15, "knockback": 2, "weight": 3},
    "Broadsword": {
        "0": { "Base Damage": 25, "Knockback": 10, "Cooldown": 0, "Recovery": 0.4, "Stamina Use": 10, "Mana Use": 0, "Scales": "STR+DEX" },

        "1": { "Base Damage": 35, "Knockback": 15, "Cooldown": 0, "Recovery": 0.5, "Stamina Use": 20, "Mana Use": 0, "Scales": "STR+DEX" },

        "2": { "Base Damage": 40, "Knockback": 10, "Cooldown": 0, "Recovery": 0.7, "Stamina Use": 25, "Mana Use": 25, "Scales": "STR+DEX" },
    },
    "Greataxe": {
        "0": { "Base Damage": 40, "Knockback": 5, "Cooldown": 0, "Recovery": 0.8, "Stamina Use": 20, "Mana Use": 0, "Scales": "STR" },

        "1": { "Base Damage": 35, "Knockback": 10, "Cooldown": 0, "Recovery": 0.7, "Stamina Use": 30, "Mana Use": 0, "Scales": "STR" },

        "2": { "Base Damage": 0, "Knockback": 10, "Cooldown": 0, "Recovery": 0.5, "Stamina Use": 40, "Mana Use": 15, "Scales": "STR" },
    },
    "Dagger": {
        "0": { "Base Damage": 20, "Knockback": 10, "Cooldown": 0, "Recovery": 0.2, "Stamina Use": 10, "Mana Use": 0, "Scales": "DEX" },

        "1": { "Base Damage": 20, "Knockback": 15, "Cooldown": 0, "Recovery": 0.2, "Stamina Use": 10, "Mana Use": 0, "Scales": "DEX" },

        "2": { "Base Damage": 0, "Knockback": 10, "Cooldown": 0, "Recovery": 0.1, "Stamina Use": 15, "Mana Use": 5, "Scales": "DEX" },
    },
}

# Weapon Upgrades - Cost
# lvl 0 = humanities
# lvl 1-3 = titanite
# lvl 4-6 = demon titanite
weapon_upgrades_cost = {
    "Broadsword": {
        "0": 0, "1": 3, "2": 5, "3": 7, "4": 2, "5": 4, "6": 6, 
    },
    "Greataxe": {
        "0": 10, "1": 3, "2": 5, "3": 7, "4": 2, "5": 4, "6": 6, 
    },
    "Dagger": {
        "0": 10, "1": 3, "2": 5, "3": 7, "4": 2, "5": 4, "6": 6, 
    },
}

# Weapon Upgrades - Requirements
weapon_upgrades_req = {
    "Broadsword": {
        "0": None, "1": None, "2": ["1"], "3": ["2"], "4": ["1"], "5": ["4"], "6": ["4", "5"], 
    },
    "Greataxe": {
        "0": None, "1": None, "2": ["1"], "3": ["2"], "4": ["1"], "5": ["4"], "6": ["4", "5"], 
    },
    "Dagger": {
        "0": None, "1": None, "2": ["1"], "3": ["2"], "4": ["1"], "5": ["4"], "6": ["4", "5"], 
    },
}

# Boons Data
boon_data = {
    ## Warriors of Sunlight
    # Core Boons
    # "boon_1": {"name": "Thunderous Roll", "category": "Warriors of Sunlight", "desc1": "Chain-lightning is emitted when rolling.", "desc2": "", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_2": {"name": "Lightning Strike", "category": "Warriors of Sunlight", "desc1": "Primary/secondary attack emits|chain-lightning when damaging a foe.", "desc2": "Skews damage scaling towards FAITH.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_3": {"name": "Electrifying Skill", "category": "Warriors of Sunlight", "desc1": "Skill emits chain-lightning when damaging|a foe.", "desc2": "Skews damage scaling towards FAITH.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_4": {"name": "Sunlight Catalyst", "category": "Warriors of Sunlight", "desc1": "Gain the Sunlight Talisman capable of|casting Miracles.", "desc2": "Skews catalyst scaling towards FAITH.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    # General Boons
    "boon_5": {"name": "Vengeance of the Gods", "category": "Warriors of Sunlight", "desc1": "When taking damage, there is a 25% chance of|releasing a shockwave.", "desc2": "", "subboons": ["boon_9", "boon_10"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_6": {"name": "King of the Storm", "category": "Warriors of Sunlight", "desc1": "Chain-lighting effects bounce 2 more times.", "desc2": "", "subboons": ["boon_11", "boon_12"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_7": {"name": "Protection of the Sun", "category": "Warriors of Sunlight", "desc1": "Skill is replaced by Soothing Sunlight,|fully restoring health when used.", "desc2": "", "subboons": ["boon_13", "boon_14"], "is_subboon": False, "cat": "Boon", "parent": None},

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

    ## Chaos Servants
    # Core Boons
    # "boon_17": {"name": "Thunderous Roll", "category": "Chaos Servants", "desc1": "Chain-lightning is emitted when rolling.", "desc2": "", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_18": {"name": "Flame Strike", "category": "Chaos Servants", "desc1": "Primary/secondary attack inflicts the Burned status effect.", "desc2": "Does not affect damage scaling.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_19": {"name": "Pyro Skill", "category": "Chaos Servants", "desc1": "Skill inflicts the Burned status effect.", "desc2": "Does not affect damage scaling.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_20": {"name": "Chaos Catalyst", "category": "Chaos Servants", "desc1": "Gain the Pyromancy Flame capable of|casting Miracles.", "desc2": "Catalyst scaling is affected by all attributes, but overall impact is lesser.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    # General Boons
    "boon_21": {"name": "Blazing Flare", "category": "Chaos Servants", "desc1": "Enemies with the Burned status effect have their speed reduced by 15%.", "desc2": "", "subboons": ["boon_25", "boon_26"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_22": {"name": "Chaos Storm", "category": "Chaos Servants", "desc1": "Skill creates eruptions around you, remaining for 2s.", "desc2": "This effect has a cooldown of 10s.", "subboons": ["boon_27", "boon_28"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_23": {"name": "Forbidden Fire", "category": "Chaos Servants", "desc1": "Skill is replaced by Power Within,|temporarily increasing attack but draining health.", "desc2": "", "subboons": ["boon_29", "boon_30"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_24": {"name": "Fuelled Vigour", "category": "Chaos Servants", "desc1": "The Burned status effect can be applied up to 3 times on a single enemy.", "desc2": "", "subboons": ["boon_31", "boon_32"], "is_subboon": False, "cat": "Boon", "parent": None},

    # Sub Boons
    "boon_25": {"name": "Debilitating Fire", "category": "Chaos Servants", "desc1": "Enemies with the Burned status effect also have their defense reduced by 8%.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_21"},
    
    "boon_26": {"name": "Wildfire", "category": "Chaos Servants", "desc1": "Enemies with the Burned status effect have a chance of spreading the effect to nearby enemies.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_21"},

    "boon_27": {"name": "Embrace of Chaos", "category": "Chaos Servants", "desc1": "Chaos Storm is also triggered by primary and secondary attacks.", "desc2": "Effect cooldown reduced by 3s.", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_22"},
    
    "boon_28": {"name": "Seething Chaos", "category": "Chaos Servants", "desc1": "Eruptions have a 50% chance of inflicting the Burned status effect.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_22"},

    "boon_29": {"name": "Deepened Devotion", "category": "Chaos Servants", "desc1": "Power Within also boosts stamina recovery speed.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_23"},
    
    "boon_30": {"name": "Substitute for Strength", "category": "Chaos Servants", "desc1": "Increases effects of Power Within by 50%, but health is drained faster.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_23"},

    "boon_31": {"name": "Chance to Strike", "category": "Chaos Servants", "desc1": "Increase attack speed by 25% for 3s after inflicting the Burned status effect on a previously-unaffected enemy.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_24"},

    "boon_32": {"name": "Flame Burrow", "category": "Chaos Servants", "desc1": "Enemies take 25% more damage from the Burned status effect.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_24"},

    ## Darkwraiths
    # Core Boons
    # "boon_33": {"name": "Thunderous Roll", "category": "Darkwraiths", "desc1": "Chain-lightning is emitted when rolling.", "desc2": "", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_34": {"name": "Strike of Death", "category": "Darkwraiths", "desc1": "Primary/secondary attack siphons health|from enemies.", "desc2": "Does not affect damage scaling.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_35": {"name": "Dark Skill", "category": "Darkwraiths", "desc1": "Skill siphons health from enemies.", "desc2": "Does not affect damage scaling.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_36": {"name": "Occult Catalyst", "category": "Darkwraiths", "desc1": "Gain the Dark Hand capable of|casting Hexes.", "desc2": "Catalyst scaling is affected by all|attributes, but overall impact is lesser.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    # General Boons
    "boon_37": {"name": "Writhing Humanity", "category": "Darkwraiths", "desc1": "Taking damage releases 3 sprites around you, dealing damage.", "desc2": "", "subboons": ["boon_41", "boon_42"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_38": {"name": "Strength of the Dark Soul", "category": "Darkwraiths", "desc1": "When siphoning health, there is a 15% chance of inflicting the Hollowed status effect.", "desc2": "", "subboons": ["boon_43", "boon_44"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_39": {"name": "Black Inferno", "category": "Darkwraiths", "desc1": "Skill is replaced by Darkstorm,|creating a vortex around the player for 5s.", "desc2": "", "subboons": ["boon_45", "boon_46"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_40": {"name": "Empowered Soul", "category": "Darkwraiths", "desc1": "Each Humanity gained in a run increases poise and attack by 2%.", "desc2": "", "subboons": ["boon_47", "boon_48"], "is_subboon": False, "cat": "Boon", "parent": None},

    # Sub Boons
    "boon_41": {"name": "Collective Strength", "category": "Darkwraiths", "desc1": "Writhing Humanity releases 2 more sprites.", "desc2": "Sprites are 25% larger.", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_37"},
    
    "boon_42": {"name": "Agony", "category": "Darkwraiths", "desc1": "Sprites inflict the Hollowed status effect.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_37"},

    "boon_43": {"name": "Embrace of the Abyss", "category": "Darkwraiths", "desc1": "Health siphoning is 15% more effective.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_38"},
    
    "boon_44": {"name": "Want for Power", "category": "Darkwraiths", "desc1": "Speed and attack speed are increased by 8% for 3s after siphoning health.", "desc2": "Effect can stack up to 4 times.", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_38"},

    "boon_45": {"name": "Deepened Devotion", "category": "Darkwraiths", "desc1": "Darkstorm increases defense and attack speed by 15% for 6s after use.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_39"},
    
    "boon_46": {"name": "Imbued Humanity", "category": "Darkwraiths", "desc1": "Darkstorm also releases 5 sprites around the player.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_39"},

    "boon_47": {"name": "Human Ingenuity", "category": "Darkwraiths", "desc1": "Slightly increases number of items gained from picking up resources.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_40"},

    "boon_48": {"name": "Shared Power", "category": "Darkwraiths", "desc1": "Each Humanity gained in a run also increases the damage dealt by enemies with the Hollowed status effect by 5%.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_40"},

    ## Blades of the Darkmoon
    # Core Boons
    # "boon_49": {"name": "Thunderous Roll", "category": "Blades of the Darkmoon", "desc1": "Chain-lightning is emitted when rolling.", "desc2": "", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_50": {"name": "Enchanted Strike", "category": "Blades of the Darkmoon", "desc1": "Primary/secondary attack emits|a soul arrow.", "desc2": "Skews damage scaling towards INTELLIGENCE.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_51": {"name": "Magical Skill", "category": "Blades of the Darkmoon", "desc1": "Skill emits a soul arrow.", "desc2": "Skews damage scaling towards INTELLIGENCE.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    "boon_52": {"name": "Moonlight Catalyst", "category": "Blades of the Darkmoon", "desc1": "Gain the Sorcerer's Staff capable of|casting Sorceries.", "desc2": "Skews catalyst scaling towards INTELLIGENCE.", "subboons": None, "is_subboon": False, "cat": "Core Boon", "parent": None},

    # General Boons
    "boon_53": {"name": "[1]", "category": "Blades of the Darkmoon", "desc1": "Estus Flask also refills 50% of max mana.", "desc2": "", "subboons": ["boon_57", "boon_58"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_54": {"name": "[2]", "category": "Blades of the Darkmoon", "desc1": "Soul arrow effects release 2 additional arrows.", "desc2": "", "subboons": ["boon_59", "boon_60"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_55": {"name": "[3", "category": "Blades of the Darkmoon", "desc1": "Skill is replaced by Snap Freeze,|creating a mist that damages enemies and has a chance of inflicting the Frozen status effect.", "desc2": "", "subboons": ["boon_61", "boon_62"], "is_subboon": False, "cat": "Boon", "parent": None},

    "boon_56": {"name": "[4]", "category": "Blades of the Darkmoon", "desc1": "Gain 2 mana when inflicting the Frozen status effect.", "desc2": "", "subboons": ["boon_63", "boon_64"], "is_subboon": False, "cat": "Boon", "parent": None},

    # Sub Boons
    "boon_57": {"name": "A", "category": "Blades of the Darkmoon", "desc1": "Soul arrows deal 25% more damage and travel 30% faster.", "desc2": "Soul arrows now consume mana.", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_53"},
    
    "boon_58": {"name": "B", "category": "Blades of the Darkmoon", "desc1": "Estus Flask also boosts casting speed by 30% for 6s after use.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_53"},

    "boon_59": {"name": "C", "category": "Blades of the Darkmoon", "desc1": "Soul arrow effects now slightly home in on enemies.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_54"},
    
    "boon_60": {"name": "D", "category": "Blades of the Darkmoon", "desc1": "Soul arrow effects have a 25% chance of inflicting the Frozen status effect.", "desc2": "Soul arrow effects have a 15% larger range.", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_54"},

    "boon_61": {"name": "Deepened Devotion", "category": "Blades of the Darkmoon", "desc1": "Snap Freeze has a 50% higher chance of inflicting the Frozen status effect.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_55"},
    
    "boon_62": {"name": "F", "category": "Blades of the Darkmoon", "desc1": "Soul arrow effects deal 5% more damage for 6s for each enemy hit by Snap Freeze.", "desc2": "Snap Freeze has a 25% larger radius.", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_55"},

    "boon_63": {"name": "G", "category": "Blades of the Darkmoon", "desc1": "Gain 2 additional mana upon inflicting the Frozen status effect.", "desc2": "", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_56"},

    "boon_64": {"name": "H", "category": "Blades of the Darkmoon", "desc1": "Inflicting the Frozen status effect increases attack speed by 2% for 6s.", "desc2": "Extends Frozen duration by 25%.", "subboons": None, "is_subboon": True, "cat": "Sub-Boon", "parent": "boon_56"},
}

# Boon Categories
boons_core = {
    "warriors_of_sunlight": {
        "list": ["boon_2", "boon_3", "boon_4"]
    },
    "chaos_servants": {
        "list": ["boon_18", "boon_19", "boon_20"]
    },
    "darkwraiths": {
        "list": ["boon_34", "boon_35", "boon_36"]
    },
    "blades_of_the_darkmoon": {
        "list": ["boon_50", "boon_51", "boon_52"]
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
            9: [],
        },
        "broadsword_0": {
            0: [[64, 0, 64, 64]],
            1: [[-64, 0, 64, 64], [-32, 64, 128, 64]],
            2: [],
            3: [],
            4: [],
            5: [],
        },
        "broadsword_1": {
            0: [],
            1: [[16, 64, 32, 64], [16, 128, 32, 64]],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
        },
        "broadsword_2": {
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
            9: [],
        },
        "broadsword_0": {
            0: [[-64, 0, 64, 64]],
            1: [[64, 0, 64, 64], [-32, -64, 128, 64]],
            2: [],
            3: [],
            4: [],
            5: [],
        },
        "broadsword_1": {
            0: [],
            1: [[16, -64, 32, 64], [16, -128, 32, 64]],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
        },
        "broadsword_2": {
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
            9: [],
        },
        "broadsword_0": {
            0: [[0, 64, 64, 64]],
            1: [[0, -64, 64, 64], [-64, -32, 64, 128]],
            2: [],
            3: [],
            4: [],
            5: [],
        },
        "broadsword_1": {
            0: [],
            1: [[-64, 16, 64, 32], [-128, 16, 64, 32]],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
        },
        "broadsword_2": {
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
            9: [],
        },
        "broadsword_0": {
            0: [[0, -64, 64, 64]],
            1: [[0, 64, 64, 64], [64, -32, 64, 128]],
            2: [],
            3: [],
            4: [],
            5: [],
        },
        "broadsword_1": {
            0: [],
            1: [[64, 16, 64, 32], [128, 16, 64, 32]],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
        },
        "broadsword_2": {
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
npc_list = ["370", "389", "367", "345", "323", "301", "279", "257", "368", "346", "324", "302", "280", "258", "369", "347", "325", "303", "281", "259", "366", "344"]
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
    "the_asylum": "9",
}

# Chamber Details
NUM_CHAMBERS_PER_REGION = 7
chambers_per_region = {
    # Chambers which can be randomly loaded [starting/ending chambers of each area are NOT included]
    "firelink_shrine": [""],
    "undead_burg": ["097", "098"],
    "undead_parish": [""],
    "the_depths": [""],
    "the_asylum": ["901", "902", "904", "905"]
}
safe_rooms = [
    "000","099", "101," "199", "201", "299", "900", "903", "999"
]
reward_first_rooms = [
    "001"
]
# X01 is the START room for each region
# X99 is the END room for each region

# Chamber Rewards
chamber_rewards = { # todo: make use of the chance section
    "great_soul": { "chance": 1, "min": 2000, "max": 5000 },
    "humanity": { "chance": 1, "min": 2, "max": 4 },
    "titanite_chunk": { "chance": 0.75, "min": 2, "max": 3 },
    "demon_titanite": { "chance": 0.75, "min": 1, "max": 2 },

    # "sunlight_summon": { "chance": 0.75, "min": 1, "max": 1 },
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
    "4": [0, 1000, 2000, 3000, 4000, 5000],
    "5": [1, 1.10, 1.20, 1.30, 1.40, 1.50],
    "6": [1, 1.10, 1.20, 1.30, 1.40, 1.50],
}

# Gifts of Humanity - Costs [in humanity sprites]
humanity_gifts_costs = {
    "1": [0, 5, 10, 15, 20, "MAX"],
    "2": [0, 3, 6, 12, 24, "MAX"],
    "3": [0, 10, 20, "MAX"],
    "4": [0, 2, 4, 6, 8, 10, "MAX"],
    "5": [1, 6, 10, 14, 18, 22, "MAX"],
    "6": [1, 5, 10, 15, 20, 30, "MAX"],
}

# Gifts of Humanity - Text
humanity_gifts_text = {
    "1": { "name": "Inner Humanity", "desc": "Increases health recovered from|using the Estus Flask." },
    "2": { "name": "Enkindled Flames", "desc": "Increases the number of Estus|Flasks for use from Bonfires." },
    "3": { "name": "Greater Agility", "desc": "Increases the number of rolls|that can be performed|successively." },
    "4": { "name": "Empowered Soul", "desc": "Increases the number of Souls|the player begins with in a run." },
    "5": { "name": "Flourishing Boldness", "desc": "Increases damage dealt against|enemies afflicted by status|effects." },
    "6": { "name": "Firm Resistance", "desc": "Increases player poise,|allowing more damage to be taken|without being stunned." },
}

# Base attributes - Text
player_attributes_text = {
    "VITALITY": '>Increases base health',
    "ENDURANCE": ">Increases base stamina|>Increases stamina recovery",
    "STRENGTH": ">Increases damage for attacks|scaling with STR",
    "DEXTERITY": ">Increases damage for attacks|scaling with DEX",
    "INTELLIGENCE": ">Increases base mana|>Increases damage for attacks|scaling with INT",
    "FAITH": ">Increases base mana|>Increases damage for attacks|scaling with FAI",
}

# Weapon upgrades - Text
upgrades_text = {
    "1": 'All Attacks:|>Stamina Cost: -10%',
    "2": "Primary & Secondary:|>Recovery Time: -20%",
    "3": "Ability:|>Mana Cost: -20%",
    "4": "Primary & Secondary:|>Base Damage: +15%",
    "5": "Ability:|>Recovery Time: -15%",
    "6": "All Attacks:|>Scaling: +50%",
}

# Resource Info
resource_details = {
    "soul remnants": ["Level-up Resource", "", ">Gained after death.|>Spending Souls on levelling up increases|the amount of Soul Remnants gained.|>Can be traded for other resources.", "Souls are present in all living things, and a|powerful soul requires many to have be defeated."],

    "humanity sprites": ["Level-up Resource | Covenant Offering", "", ">Dropped by some enemies.|>Found in various locations.|>Can be spent on permanent unique bonuses|in several ways.", "Rare black sprite found on human remains. Thought|to be somehow distinct from the soul."],

    "souvenirs of reprisal": ["Covenant Offering", "Blood-drained, shrunken ear. Souvenir taken from subduing the guilty.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be offered to the Blades of the Darkmoon|to increase Covenant rank."],
    "sunlight medals": ["Covenant Offering", "Warm medal, engraved with the symbol of the Sun. Represents Lord Gwyn's firstborn, who lost the status of deity.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be offered to the Warriors of Sunlight to|increase Covenant rank."],
    "eyes of death": ["Covenant Offering", "Eyes taken from those afflicted by curses of petrification. Known to be used to spread death.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be offered to the Gravelord Servants to|increase Covenant rank."],
    "dragon scales": ["Covenant Offering", "Scales peeled from an ancient dragon. Highly sought after for its rarity.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be offered to the Path of the Dragon to|increase Covenant rank."],
    "titanite shards": ["Upgrade Material", "Most common titanite material. Etched into weapons for reinforcement.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be used to strengthen standard weapons|to +3."],
    "large titanite shards": ["Upgrade Material", "Larger and rarer titanite material. Etched into weapons for reinforcement.", "Can be found in chambers.|Can be purchased from some vendors.", "Can be used to strengthen standard weapons|to +6."],
    
    "titanite chunks": ["Upgrade Material", "", ">Found in various locations.|>Can be bought from various vendors.|>Can be used for basic permanent weapon|upgrades.", "Titanite is the heirloom of a nameless blacksmith|deity. All that remains are fragments and shards."],

    "titanite slabs": ["Upgrade Material", "Legendary titanite material of a nameless blacksmith deity. Etched into weapons for reinforcement.", ">Can be found in chambers.|Can be gained from defeating strong enemies.", "Can be used to strengthen standard weapons|to +10 and demon/twinkling weapons to +5."],

    "demon titanite": ["Upgrade Material", "", ">Dropped by Titanite Demons.|>Can be bought from various vendors.|>Can be used for advanced permanent weapon|upgrades.", "Great beasts arose from slabs of Titanite after the|blacksmith deity's death."],

    "twinkling titanite": ["Upgrade Material", "Titanite imbued with a particularly powerful energy of unknown origin.", "Can be found in chambers.|Can be gained from defeating strong enemies.", "Can be used to strengthen twinkling weapons|to +4."],
}

# UI Info
ui_data = {
    "HEALTH_BAR_WIDTH": player_data['dependent_variables']['health'] * 0.5,
    "STAMINA_BAR_WIDTH": player_data['dependent_variables']['stamina'] * 2,
    "MANA_BAR_WIDTH": player_data['dependent_variables']['mana'] * 1,
}

# Misc Lore Text
lore_misc = {
    "gifts_of_humanity": '"Once, the Lord of Light banished Dark, and all that stemmed|from humanity. And men assumed a fleeting form."',
    "level_up": '"Souls are the source of all life, and whether Undead, or even|Hollow, one continues to seek them."',
    "weapons": '"In battle, y’ weapons are yer only friends. Forge them well,|and they won’t let y’ down."',
}

LEVELUP_MULT = 200