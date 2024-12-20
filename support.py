from csv import reader
import os, pygame
from settings import *

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ",")
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
    
# def import_folder(path):
#     surface_list = []

#     for _, __, image_files in os.walk(path):
#         for image in image_files:
#             full_path = path + "/" + image
#             image_surface = pygame.image.load(full_path).convert_alpha()
#             image_surface.set_colorkey(COLOURKEY)
#             surface_list.append(image_surface)
#     return surface_list

def import_folder(path, scale = False, num = (0, 0)):
    surface_list = []

    for _, __, image_files in os.walk(path):
        for image in image_files:
            full_path = os.path.join(path, image)
            if not scale: image_surface = pygame.image.load(full_path).convert_alpha()
            else: image_surface = pygame.transform.scale(pygame.image.load(full_path), (num)).convert_alpha()
            image_surface.set_colorkey(COLOURKEY)
            surface_list.append((image, image_surface))  # Store the filename along with the surface

    # Sort the list alphabetically by filename
    surface_list.sort(key=lambda x: x[0])

    # Extract just the surfaces, discarding the filenames
    surface_list = [item[1] for item in surface_list]

    return surface_list

def centreImageNum(num1, num2):
    image_width = (WIDTH//2) - num1//2
    image_height = (HEIGHT//2) - num2//2
    return image_width, image_height

def centreImage(image):
    image_width = (WIDTH//2) - image.get_width()//2
    image_height = (HEIGHT//2) - image.get_height()//2
    return image_width, image_height

def get_upgrade_cost(level):
    upgrade_equation = 0.02 * level **3 + 3.06 * level **2 + 105.6 * level - 895
    # upgrade_equation = self.base_upgrade_cost["VITALITY"] * self.level + randint(1, 100)
    return upgrade_equation

def restore_estus():
    player_core_info["values"]["current estus"] = player_core_info["values"]["max estus"]

def get_attribute_num(stat):
    stat_path = f"assets/map/stats/{stat}.txt"
    item_list = []

    with open(stat_path, 'r') as input_file:
        stat_info = input_file.readlines()
    
    for i in stat_info:
        i = i.replace(",\n", "").split(",")
        item_list.append(i)

    # print(f"Current Level: {item_list[player_data['attributes'][stat]][0]}\nHP Gain from next Level Up: {item_list[player_data['attributes'][stat] + 1][2]}")
    return int(item_list[player_data['attributes'][stat]][2])

def getSlotData(slot, data): #right_hand_data # todo: be abke to change what items to show/have, not use index
    iteminfo = [list(data.keys())[0]]

    checklist = ["cooldown", "damage", "knockback", "weight", "graphic"]
    if data == tool_data: checklist = ["cooldown", "damage", "knockback", "weight", "type", "graphic"]

    for i in checklist:
         iteminfo.append(list(data.values())[0][i])
            
    for item in slot["slot1"]:
        index = list(slot["slot1"]).index(item)
        slot["slot1"][item] = iteminfo[index]
    # print(slot["slot1"])

    iteminfo = [list(data.keys())[1]]
    for i in checklist:
         iteminfo.append(list(data.values())[1][i])
        
    for item in slot["slot2"]:
        index = list(slot["slot2"]).index(item)
        slot["slot2"][item] = iteminfo[index]
    # print(slot["slot2"])

# Create a dynamically-sized UI background
# Widens given width/height by 20px by default
def createUI(surface, width, height, pos, type="", padding = 20):
    # Set UI type/padding
    if type != "": type = "_" + type

    # Load images
    path = "assets/graphics/ui/interface"
    bg_topleft = pygame.image.load(f"{path}/bg_topleft{type}.png").convert_alpha()
    bg_topright = pygame.image.load(f"{path}/bg_topright{type}.png").convert_alpha()
    bg_bottomleft = pygame.image.load(f"{path}/bg_bottomleft{type}.png").convert_alpha()
    bg_bottomright = pygame.image.load(f"{path}/bg_bottomright{type}.png").convert_alpha()
    bg_border = pygame.image.load(f"{path}/bg_border{type}.png").convert_alpha()
    bg_body = pygame.image.load(f"{path}/bg_body{type}.png").convert_alpha()

    # Find necessary values
    corner_width = bg_topleft.get_width()
    corner_height = bg_topleft.get_height()
    border_width = width - (2 * corner_width)
    border_height = height - (2 * corner_height)

    # Scale body and border
    bg_border_top = pygame.transform.scale(bg_border, (border_width + 40, 10)).convert_alpha()
    bg_border_bottom =  pygame.transform.rotate(pygame.transform.scale(bg_border, (border_width + 40, 10)), 180).convert_alpha()
    bg_border_left =  pygame.transform.rotate(pygame.transform.scale(bg_border, (border_height + 40, 10)), 90).convert_alpha()
    bg_border_right =  pygame.transform.rotate(pygame.transform.scale(bg_border, (border_height + 40, 10)), -90).convert_alpha()
    bg_body_resized = pygame.transform.scale(bg_body, (border_width + 40 + 16, border_height + 40 + 16)).convert_alpha()

    # Blit surfaces
    surface.blit(bg_topleft, (pos[0] - padding, pos[1] - padding))
    surface.blit(bg_topright, (pos[0] + corner_width + border_width + padding, pos[1] - padding))
    surface.blit(bg_bottomleft, (pos[0] - padding, pos[1] + corner_height + border_height + padding))
    surface.blit(bg_bottomright, (pos[0] + corner_width + border_width + padding, pos[1] + corner_height + border_height + padding))

    surface.blit(bg_border_top, (pos[0] + corner_width - padding, pos[1] + 2 - padding))
    surface.blit(bg_border_bottom, (pos[0] + corner_width - padding, pos[1] + (2 * corner_height) + border_height - 10 - 2 + padding))
    surface.blit(bg_border_left, (pos[0] + 2 - padding, pos[1] + corner_height - padding))
    surface.blit(bg_border_right, (pos[0] + (2 * corner_width) + border_width - 10 - 2 + padding, pos[1] + corner_height - padding))

    surface.blit(bg_body_resized, (pos[0] - 8, pos[1] - 8))

def getBoxStatus(active_cond, locked_cond, hover_cond, id, usage, num=False):
    num_icon = None
    locked = False

    if usage == "upgrades":
        current_weapon = player_core_info['values']['current weapon']
        required_upgrades = weapon_upgrades_req[current_weapon][str(id)]

        if required_upgrades != None:
            for req in required_upgrades:
                if not weapon_upgrades[current_weapon][req]: locked = True

    
    if active_cond:
        icon = pygame.image.load("assets/graphics/ui/interface/square_box_active.png").convert_alpha()
        if num: num_icon = pygame.image.load(f"assets/graphics/ui/button_icons/{id}_active.png").convert_alpha()
    
    elif locked_cond or locked:
        icon = pygame.image.load("assets/graphics/ui/interface/square_box_grey.png").convert_alpha()
        if num: num_icon = pygame.image.load(f"assets/graphics/ui/button_icons/{id}.png").convert_alpha()
    
    elif hover_cond:
        icon = pygame.image.load("assets/graphics/ui/interface/square_box_selected.png").convert_alpha()
        if num: num_icon = pygame.image.load(f"assets/graphics/ui/button_icons/{id}.png").convert_alpha()

        if player_inputs["light attack"]:
            if usage == "upgrades":
                current_weapon = player_core_info['values']['current weapon']
                cost = weapon_upgrades_cost[current_weapon][str(id)]

                weapon_upgrades[current_weapon][str(id)] = 1
                resources["titanite chunks"] -= cost
                player_inputs["light attack"] = False
    
    else:
        icon = pygame.image.load("assets/graphics/ui/interface/square_box.png").convert_alpha()
        if num: num_icon = pygame.image.load(f"assets/graphics/ui/button_icons/{id}.png").convert_alpha()

    return icon, num_icon

# Called when weapon changes - copies weapon info to player info so that details can be dynamically
# updated in a run
def set_player_weapon_details(weapon):
    # todo: clean up by using a loop

    # Primary Attack
    player_core_info["light_attack"]["name"] = f"{weapon.lower()}_light"
    player_core_info["light_attack"]["cooldown"] = weapon_data[weapon]["0"]["Recovery"] * 1000 # in ms
    player_core_info["light_attack"]["base damage"] = weapon_data[weapon]["0"]["Base Damage"]
    player_core_info["light_attack"]["knockback"] = weapon_data[weapon]["0"]["Knockback"]
    player_core_info["light_attack"]["stamina_use"] = weapon_data[weapon]["0"]["Stamina Use"]

    # Secondary Attack
    player_core_info["heavy_attack"]["name"] = f"{weapon.lower()}_heavy"
    player_core_info["heavy_attack"]["cooldown"] = weapon_data[weapon]["1"]["Recovery"] * 1000 # in ms
    player_core_info["heavy_attack"]["base damage"] = weapon_data[weapon]["1"]["Base Damage"]
    player_core_info["heavy_attack"]["knockback"] = weapon_data[weapon]["1"]["Knockback"]
    player_core_info["heavy_attack"]["stamina_use"] = weapon_data[weapon]["1"]["Stamina Use"]

    # Ability
    player_core_info["skill"]["name"] = f"{weapon.lower()}_skill"
    player_core_info["skill"]["cooldown"] = weapon_data[weapon]["2"]["Recovery"] * 1000 # in ms
    player_core_info["skill"]["base damage"] = weapon_data[weapon]["2"]["Base Damage"]
    player_core_info["skill"]["knockback"] = weapon_data[weapon]["2"]["Knockback"]
    player_core_info["skill"]["stamina_use"] = weapon_data[weapon]["2"]["Stamina Use"]
    player_core_info["skill"]["mana_use"] = weapon_data[weapon]["2"]["Mana Use"]

def update_dialogue_completion(npc, id):
    npc_conversations[npc][id]["completed"] = True