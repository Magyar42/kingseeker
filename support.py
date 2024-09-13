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

def restore_estus(player, level):
    player_data['status']['estus'] = 5 * level

    player_data['status']['current_estus'] = player_data['status']['estus']
    qitems_data[f'slot{player.qitems_index + 1}']['amount'] = player_data['status']['current_estus']
    if player.qitems[player.qitems_index] == "Estus Flask":
        player.qitems_uses[player.qitems_index] = qitems_data[f'slot{player.qitems_index + 1}']['amount']

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

#def sortInventoryStacks():
    # for each item in inventory
    # go to dictionary and get stack amount
    # return back to inventory and divide item into stack amounts

def checkControllerInput():
    if len(controller_list) != 0:
        CURRENT_CONTROLLER = controller_list(0)

        if CURRENT_CONTROLLER.get_button(0): print("Button 0 pressed")
        if CURRENT_CONTROLLER.get_button(1): print("Button 1 pressed")
        if CURRENT_CONTROLLER.get_button(2): print("Button 2 pressed")
        if CURRENT_CONTROLLER.get_button(3): print("Button 3 pressed")