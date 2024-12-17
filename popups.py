import pygame
from settings import *
from debug import debug
from support import *
from random import choice
from globalinfo import *

# Prompts to press a button
class Prompt:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, PROMPT_FONT_SIZE)

        self.inital_prompt_pos = (self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] -  40 )

    def createPrompt(self, type, button, text):
        # Todo: add functionality to automatically allow several prompts on screen/toggle button
        # current_prompts.append(f"{button}: {type}")

        x = self.display_surface.get_size()[0] // 2
        y = self.display_surface.get_size()[1] - (PROMPT_HEIGHT + PROMPT_GAP) - 20 # * len(current_prompts)

        text_surface = self.font.render(str(f"[{button}] {text.upper()}"), False, TEXT_TITLE_COLOUR).convert_alpha()
        text_rect = text_surface.get_rect(center = (x, y))

        self.displayPrompt(text_rect, text_surface)
    
    def displayPrompt(self, rect, surface):

        createUI(self.display_surface, rect.width, rect.height, (rect.x, rect.y), "dark")

        #pygame.draw.rect(self.display_surface, UI_BG_COLOUR, rect.inflate(10, 10))
        self.display_surface.blit(surface, rect)
        #pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, rect.inflate(10, 10), 4)

# Popup on item pickup
class ItemPopup:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, PROMPT_FONT_SIZE)

        self.inital_prompt_pos = (self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] -  40 )

    def createPrompt(self, type, button, text, num, pos):
        # Todo: add functionality to automatically allow several prompts on screen/toggle button
        # current_prompts.append(f"{button}: {type}")

        x = self.display_surface.get_size()[0] // 2
        y = self.display_surface.get_size()[1] - (PROMPT_HEIGHT * 2) * pos - 50

        text_surface = self.font.render(str(f"{text}"), False, TEXT_COLOUR)
        num_surface = self.font.render(str(f"[{num}]"), False, TEXT_COLOUR)
        text_rect = text_surface.get_rect(center = (x, y))

        display_rect = pygame.Rect(text_rect.left - 40, text_rect.top, text_rect.w + 80, text_rect.h * 3)

        self.displayPrompt(display_rect, text_surface, num_surface)
    
    def displayPrompt(self, rect, surface1, surface2):
        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, rect.inflate(10, 10))
        self.display_surface.blit(surface1, rect.midleft + pygame.math.Vector2(10, -5))
        self.display_surface.blit(surface2, rect.midright + pygame.math.Vector2(-50, -5))
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, rect.inflate(10, 10), 5)

# Bonfire Menu
class Decision:
    def __init__(self, toggle_screen_effect, menu_humanity_effects, menu_human_already_effects, menu_need_humanity_effects, menu_kindle_effects, menu_requires_human_effects, menu_fully_kindled_effects):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, PROMPT_FONT_SIZE)

        self.selection_index = 0
        self.selection_time = None
        self.can_move_selection = True

        self.toggle_screen_effect = toggle_screen_effect
        self.menu_humanity_effects = menu_humanity_effects
        self.menu_human_already_effects = menu_human_already_effects
        self.menu_need_humanity_effects = menu_need_humanity_effects
        self.menu_kindle_effects = menu_kindle_effects
        self.menu_requires_human_effects = menu_requires_human_effects
        self.menu_fully_kindled_effects = menu_fully_kindled_effects

        self.options_list = []
        self.body = None

        # self.opening_decision = True
        # self.decision_cooldown = 2000
        # self.decision_opening_time = pygame.time.get_ticks()

    def selection_cooldown(self):
        if not self.can_move_selection:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 100:
                self.can_move_selection = True

    def createDecision(self, type, player, body, option1=None, option2=None, option3=None, option4=None):
        #self.opening_decision = True
        #self.decision_opening_time = pygame.time.get_ticks()
        self.body = body
        
        if type == "Boolean":
            option1 = "Yes"
            option2 = "No"
        elif type == "Info":
            option1 = "OK"

        for item in [option1, option2, option3, option4]:
            if item != None and item not in self.options_list:
                self.options_list.append(item)
       
        self.input(player)
        self.selection_cooldown()

        bg_rect_size = (500, 70)
        option_rect_size = (500, 30)

        x = (self.display_surface.get_size()[0] // 2) - (bg_rect_size[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2) + 200

        main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, main_rect.inflate(10, 10))
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, main_rect.inflate(10, 10), 4)

        for option in self.options_list:
            index = self.options_list.index(option)
            item = Item(x, y + 90 + (option_rect_size[1] + 5) * self.options_list.index(option), option_rect_size[0], option_rect_size[1], index, self.font)
            item.display(self.display_surface, self.selection_index, option)
        
        text_body_surface = self.font.render(body, False, TEXT_COLOUR)
        text_body_rect = text_body_surface.get_rect(center = main_rect.center)
        self.display_surface.blit(text_body_surface, text_body_rect)
   
    def input(self, player):
        keys = pygame.key.get_pressed()

        if self.can_move_selection:
            if keys[pygame.K_DOWN] and self.selection_index < len(self.options_list) - 1:
                self.selection_index += 1
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_UP] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_f]:
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()
                # print(f"{len(self.options_list)}, {self.options_list}")
                self.triggered_effect(self.options_list[self.selection_index], player)

    # ALL POTENTIAL EFFECTS
    def triggered_effect(self, button, player):
        self.options_list = []

        if self.body == RESTORE_HUMANITY_TEXT:
            self.menu_humanity_effects(button)
        elif self.body == ALREADY_HUMAN_TEXT:
            self.menu_human_already_effects()
        elif self.body == NEED_HUMANITY_TEXT:
            self.menu_need_humanity_effects()
        elif self.body == KINDLE_TEXT:
            self.menu_kindle_effects(button, player)
        elif self.body == REQUIRES_HUMAN_TEXT:
            self.menu_requires_human_effects()
        elif self.body == CANNOT_KINDLE:
            self.menu_fully_kindled_effects()

class Item:
    def __init__(self, left, top, width, height, index, font):
        self.rect = pygame.Rect(left, top, width, height)
        self.index = index
        self.font = font

    def display_names(self, surface, name):
        #colour = UPGRADE_TEXT_COLOUR_SELECTED if selected else UPGRADE_TEXT_COLOUR
        colour = UPGRADE_TEXT_COLOUR

        title_surface = self.font.render(name, False, colour)
        title_rect = title_surface.get_rect(center = self.rect.center)

        surface.blit(title_surface, title_rect)

    def display(self, surface, selection_num, name):
        if self.index == selection_num:
            pygame.draw.rect(surface, HOVER_COLOUR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOUR, self.rect, 4)
        else:
            pygame.draw.rect(surface, UI_BG_COLOUR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOUR, self.rect, 4)

        self.display_names(surface, name)

# Side Menu
class gameMenu:
    def __init__(self, toggle_screen_effect):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, PROMPT_FONT_SIZE)
        self.toggle_screen_effect = toggle_screen_effect

        self.details_index_items = None
        self.details_index_boons = None
        self.boon_active = False

        self.details_toggle_time = None
        self.details_can_toggle = True

        self.resource_name_list = list(resources.keys())
        self.resource_num_list = list(resources.values())
        self.resource_icon_list = import_folder("assets/graphics/ui/resources")
        self.resource_icon_list_highres = import_folder("assets/graphics/resources")

        self.menu = itemMenu()
        self.big_boon_frame = pygame.image.load("assets/graphics/ui/interface/big_box.png")

        self.boons = []
        self.boons_names = []
        # Only load boons (not sub-boons) for the display
        for current_boon in interface_details["boons"]["list"]:
            if not boon_data[current_boon]["is_subboon"]:
                current_boon_surf = pygame.image.load(f"assets/graphics/ui/interface_icons/boons/{current_boon}.png")
                self.boons.append(current_boon_surf)
                self.boons_names.append(current_boon)

    # def update_boons(self):
    #     self.boons = []
    #     self.boons_names = []
    #     # Only load boons (not sub-boons) for the display
    #     for current_boon in interface_details["boons"]["list"]:
    #         if not boon_data[current_boon]["is_subboon"]:
    #             current_boon_surf = pygame.image.load(f"assets/graphics/ui/interface_icons/boons/{current_boon}.png")
    #             self.boons.append(current_boon_surf)
    #             self.boons_names.append(current_boon)

    def selection_cooldown(self):
        if not self.details_can_toggle:
            current_time = pygame.time.get_ticks()
            if current_time - self.details_toggle_time >= 200:
                self.details_can_toggle = True
    
    # Esc Menu - Shows items + boons
    def displayMenu(self, player):

        # ITEMS Display
        bg_rect_size = (90, 140)
        option_rect_size = (32, 32)
        x = (self.display_surface.get_size()[0] - 140)
        y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2) + 250 - 60

        createUI(self.display_surface, bg_rect_size[0], bg_rect_size[1], (x, y), "dark")

        # Set to None every tick so that it displays nothing if nothing is hovered over currently
        self.details_index_items = None
        if not self.boon_active: self.details_index_boons = None
        x_pos_box = x + bg_rect_size[0] - option_rect_size[0] - 5

        pos = pygame.mouse.get_pos()
        for resource in self.resource_name_list:
            index = self.resource_name_list.index(resource)
            item_rect = pygame.Rect(x_pos_box, y + (option_rect_size[1] + 5) * self.resource_name_list.index(resource), option_rect_size[0], option_rect_size[1])
            
            if item_rect.collidepoint(pos):
                self.details_index_items = index
                selected = True
            else: selected = False
            self.menu.display(index, item_rect, selected, self.resource_num_list[index])

        # BOONS Display
        bg_rect_size = (90, 30 + (len(self.boons)) * 45)
        x = (self.display_surface.get_size()[0] - 140)
        y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2) + 250

        createUI(self.display_surface, bg_rect_size[0], bg_rect_size[1], (x, 50), "dark")

        for slot in range(len(self.boons)):
            boon_rect = pygame.Rect(1145, 50 + (slot * 45), ITEM_BOX_SIZE, ITEM_BOX_SIZE)
            
            if boon_rect.collidepoint(pos) and not self.boon_active:
                self.details_index_boons = slot
                selected = True
            else: selected = False
            self.menu.boon_display(boon_rect, selected)

            boon_img = self.boons[slot]
            self.display_surface.blit(boon_img, boon_rect)

        # DETAILS toggle
        if self.details_index_items is not None:
            self.item_details(player, self.resource_name_list[self.details_index_items], pygame.font.Font(UI_FONT, 16))
        if self.details_index_boons is not None:
            self.boon_details(player, self.boons_names[self.details_index_boons], pygame.font.Font(UI_FONT, 16))

            self.boon_active = True
            if self.boon_active: 
                # Blit again to draw on top of all boons
                # self.boon_active locks self.details_index_boons, preventing it from being changed
                active_boon_rect = pygame.Rect(1145, 50 + (self.details_index_boons * 45), ITEM_BOX_SIZE, ITEM_BOX_SIZE)
                self.menu.boon_display(active_boon_rect, True)
                active_boon_img = self.boons[self.details_index_boons]
                self.display_surface.blit(active_boon_img, active_boon_rect)

                if not active_boon_rect.collidepoint(pos):
                    # Unlocks self.details_index_boons
                    self.boon_active = False
    
    # Details Menu - Item details
    def item_details(self, player, resource, font):
        # Background
        bg_rect_size = (700, 197)
        x = (self.display_surface.get_size()[0] - 890) # - (bg_rect_size[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2) + 221
        main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
        text_rect_pos = main_rect.topleft + pygame.math.Vector2(120, 50)
        text_rect_size = (bg_rect_size[0] - 20 - 20 - 100, (bg_rect_size[1] - 80) // 2)

        createUI(self.display_surface, bg_rect_size[0], bg_rect_size[1], (x, y), "dark")
        createUI(self.display_surface, text_rect_size[0], text_rect_size[1], text_rect_pos, "basic")
        createUI(self.display_surface, text_rect_size[0], text_rect_size[1] - 35, (text_rect_pos[0], text_rect_pos[1] + text_rect_size[1] + 45), "basic")

        # Name
        title_surface = font.render(f"| {resource.upper()}", True, TEXT_TITLE_COLOUR)
        title_rect = title_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(105, 15))
        self.display_surface.blit(title_surface, title_rect)

        # Image
        index = self.resource_name_list.index(resource)
        icon_surface = self.resource_icon_list_highres[index]
        icon_rect = icon_surface.get_rect(midleft = main_rect.midleft + pygame.math.Vector2(15, 0))

        createUI(self.display_surface, 60, 60, (icon_rect.topleft))
        self.display_surface.blit(icon_surface, icon_rect)

        # Info
        found_text = resource_details[f"{resource}"][2]
        split_current_line = found_text.split("|")
        while len(split_current_line) < 4:
            split_current_line.append("")
        for subline in range(4):
            text_surf = pygame.font.Font(UI_FONT, 12).render(split_current_line[subline], False, UI_BG_COLOUR)
            text_rect = text_surf.get_rect(topleft = text_rect_pos + pygame.math.Vector2(0, (subline * 15)))
            self.display_surface.blit(text_surf, text_rect)

        # Lore
        used_text = resource_details[f"{resource}"][3]
        split_current_line = used_text.split("|")
        while len(split_current_line) < 3:
            split_current_line.append("")
        for subline in range(3):
            text_surf = pygame.font.Font(UI_FONT, 11).render(split_current_line[subline], False, UI_BG_LIGHT_COLOUR)
            text_rect = text_surf.get_rect(topleft = text_rect_pos + pygame.math.Vector2(0, text_rect_size[1] + 45 + subline * 15))
            self.display_surface.blit(text_surf, text_rect)

    # Details Menu - Boon details
    def boon_details(self, player, boon, font):
        # Background
        if boon_data[boon]["desc2"] != "": bg_rect_size = (700, 147)
        else: bg_rect_size = (700, 107)

        x = (self.display_surface.get_size()[0] - 790) - 100
        y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2) - 250
        main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
        text_rect_pos = main_rect.topleft + pygame.math.Vector2(120, 50)
        text_rect_size = (bg_rect_size[0] - 20 - 20 - 100, bg_rect_size[1] - 50 - 20 - 10)

        createUI(self.display_surface, bg_rect_size[0], bg_rect_size[1], (x, y), "dark")
        createUI(self.display_surface, text_rect_size[0], text_rect_size[1], text_rect_pos, "basic")

        # Icon
        icon_surface = pygame.image.load(f"assets/graphics/ui/interface_icons/boons_big/{boon}.png")
        icon_rect = icon_surface.get_rect(midleft = main_rect.midleft + pygame.math.Vector2(-5, 0))

        self.display_surface.blit(self.big_boon_frame, icon_rect)
        self.display_surface.blit(icon_surface, icon_rect)

        # Name
        title_surface = font.render(f"| {boon_data[f'{boon}']['name'].upper()}", True, TEXT_TITLE_COLOUR)
        title_rect = title_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(105, 15))
        self.display_surface.blit(title_surface, title_rect)

        # Desc 1
        desc1 = boon_data[f"{boon}"]["desc1"]
        split_current_line = desc1.split("|")
        while len(split_current_line) < 4:
            split_current_line.append("")
        for subline in range(4):
            text_surf = pygame.font.Font(UI_FONT, 12).render(split_current_line[subline], False, UI_BG_COLOUR)
            text_rect = text_surf.get_rect(topleft = text_rect_pos + pygame.math.Vector2(0, (subline * 15)))
            self.display_surface.blit(text_surf, text_rect)

        # Desc 2
        desc2 = boon_data[f"{boon}"]["desc2"]
        split_current_line = desc2.split("|")
        while len(split_current_line) < 4:
            split_current_line.append("")
        for subline in range(4):
            text_surf = pygame.font.Font(UI_FONT, 12).render(split_current_line[subline], False, UI_BG_COLOUR)
            text_rect = text_surf.get_rect(topleft = text_rect_pos + pygame.math.Vector2(0, 40 + subline * 15))
            self.display_surface.blit(text_surf, text_rect)

        # SUB BOONS
        self.subboons_display(boon, pygame.font.Font(UI_FONT, 12), boon_data[f'{boon}']['subboons'], bg_rect_size[1])
    
    # todo: clean up the below
    def subboons_display(self, parent_boon, font, child_boons, parent_height):
        if child_boons == None:
            # Background
            bg_rect_size = (700, 90)
            x = (self.display_surface.get_size()[0] - 790) - 100
            y = (self.display_surface.get_size()[1] // 2) - (parent_height // 2) - 250 + parent_height + 20
            main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
            # pygame.draw.rect(self.display_surface, UI_BG_COLOUR, main_rect.inflate(10, 10))
            # pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, main_rect.inflate(10, 10), 3)

            text_rect_pos = main_rect.topleft + pygame.math.Vector2(0, 30)
            text_rect_size = (bg_rect_size[0] - 20 - 20 - 100, bg_rect_size[1] - 50 - 20 - 10)

            createUI(self.display_surface, text_rect_size[0], text_rect_size[1], text_rect_pos)

            # Name
            title_surface = pygame.font.Font(UI_FONT, 12).render("No sub-boons available for Core Boons.", True, UI_BG_COLOUR)
            title_rect = title_surface.get_rect(midleft = text_rect_pos + pygame.math.Vector2(0, 5))
            self.display_surface.blit(title_surface, title_rect)
        else:
            # Background
            prev_subboon_height = 0
            for index, subboon in enumerate(child_boons):
                # If sub-boon is active, show details
                if subboon in interface_details["boons"]["list"]:
                    if boon_data[subboon]["desc2"] != "": bg_rect_size = (700, 175)
                    else: bg_rect_size = (700, 135)

                    x = (self.display_surface.get_size()[0] - 790) - 100
                    y = (self.display_surface.get_size()[1] // 2) - (parent_height // 2) - 250 + parent_height + 20 + (index * (prev_subboon_height + 20))
                    main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
                    # pygame.draw.rect(self.display_surface, UI_BG_COLOUR, main_rect.inflate(10, 10))
                    # pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, main_rect.inflate(10, 10), 3)

                    text_rect_pos = main_rect.topleft + pygame.math.Vector2(0, 30)
                    text_rect_size = (bg_rect_size[0] - 20 - 20 - 100, bg_rect_size[1] - 50 - 20 - 10)

                    createUI(self.display_surface, text_rect_size[0], text_rect_size[1], text_rect_pos)

                    # Name
                    title_surface = pygame.font.Font(UI_FONT, 14).render(f"{boon_data[f'{subboon}']['name'].upper()}", True, UI_BG_COLOUR)
                    title_rect = title_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(0, 40))
                    self.display_surface.blit(title_surface, title_rect)

                    # Desc 1
                    desc1 = boon_data[f'{subboon}']["desc1"]
                    split_current_line = desc1.split("|")
                    while len(split_current_line) < 4:
                        split_current_line.append("")
                    for subline in range(4):
                        text_surf = pygame.font.Font(UI_FONT, 12).render(split_current_line[subline], False, UI_BG_COLOUR)
                        text_rect = text_surf.get_rect(topleft = text_rect_pos + pygame.math.Vector2(0, 30 + (subline * 15)))
                        self.display_surface.blit(text_surf, text_rect)

                    # Desc 2
                    desc2 = boon_data[f'{subboon}']["desc2"]
                    split_current_line = desc2.split("|")
                    while len(split_current_line) < 4:
                        split_current_line.append("")
                    for subline in range(4):
                        text_surf = pygame.font.Font(UI_FONT, 12).render(split_current_line[subline], False, UI_BG_COLOUR)
                        text_rect = text_surf.get_rect(topleft = text_rect_pos + pygame.math.Vector2(0, 30 + 40 + subline * 15))
                        self.display_surface.blit(text_surf, text_rect)
                    
                # If sub-boon is not active, show ???
                else: 
                    # Background
                    bg_rect_size = (700, 90)
                    x = (self.display_surface.get_size()[0] - 790) - 100
                    y = (self.display_surface.get_size()[1] // 2) - (parent_height // 2) - 250 + parent_height + 20 + (index * (prev_subboon_height + 20))
                    main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])

                    text_rect_pos = main_rect.topleft + pygame.math.Vector2(0, 30)
                    text_rect_size = (bg_rect_size[0] - 20 - 20 - 100, bg_rect_size[1] - 50 - 20 - 10)

                    createUI(self.display_surface, text_rect_size[0], text_rect_size[1], text_rect_pos)

                    # Name
                    title_surface = pygame.font.Font(UI_FONT, 12).render("???", True, UI_BG_COLOUR)
                    title_rect = title_surface.get_rect(midleft = text_rect_pos + pygame.math.Vector2(0, 5))
                    self.display_surface.blit(title_surface, title_rect)
                prev_subboon_height = bg_rect_size[1] - 50 # Used to dynamically change distance between subboons

class itemMenu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = self.font = pygame.font.Font(UI_FONT, PROMPT_FONT_SIZE)

        self.icons_list = import_folder("assets/graphics/ui/menu/menu_options")
        self.icons_selected_list = import_folder("assets/graphics/ui/menu/menu_options_selected")

        self.resource_name_list = list(resources.keys())
        self.resource_num_list = list(resources.values())
        self.resource_icon_list = import_folder("assets/graphics/ui/resources")

    def display_names(self, surface, rect, num):
        #colour = UPGRADE_TEXT_COLOUR_SELECTED if selected else UPGRADE_TEXT_COLOUR
        colour = TEXT_TITLE_COLOUR

        title_surface = self.font.render(str(num), True, colour)
        title_rect = title_surface.get_rect(midright = rect.midleft + pygame.math.Vector2(-10, 0))
        surface.blit(title_surface, title_rect)

    def display(self, index, rect, selected, num):
        if selected: itembox_surf = pygame.image.load("assets/graphics/ui/interface/square_box_selected.png").convert_alpha()
        else: itembox_surf = pygame.image.load("assets/graphics/ui/interface/square_box.png").convert_alpha()
        self.display_surface.blit(itembox_surf, rect)
        
        self.display_surface.blit(self.resource_icon_list[index], rect)
        self.display_names(self.display_surface, rect, num)

    def boon_display(self, rect, selected):
        if selected: itembox_surf = pygame.image.load("assets/graphics/ui/interface/item_box_selected.png").convert_alpha()
        else: itembox_surf = pygame.image.load("assets/graphics/ui/interface/item_box.png").convert_alpha()
        self.display_surface.blit(itembox_surf, rect)

# Boons Menu
class BoonsMenu:
    def __init__(self, toggle_screen_effect, enable_player_control):
        self.display_surface = pygame.display.get_surface()
        self.font16 = pygame.font.Font(UI_FONT, 16)
        self.font14 = pygame.font.Font(UI_FONT, 14)
        self.font12 = pygame.font.Font(UI_FONT, 12)

        self.toggle_screen_effect = toggle_screen_effect
        self.enable_player_control = enable_player_control

        self.boon_icons = []
        self.big_boon_frame = pygame.image.load("assets/graphics/ui/interface/big_box.png")
        self.big_boon_frame_selected = pygame.image.load("assets/graphics/ui/interface/big_box_selected.png")
    
    def generate_boons(self, covenant):
        player_boons = interface_details["boons"]["list"]
        core_boons = boons_core[covenant]["list"]

        # Set bool - if false, only core boons can be chosen from
        core_boons_set = False
        for boon in player_boons:
            if boon in core_boons:
                core_boons_set = True
                break
        
        boons_choice = []
        trimmed_boons_list = []
        if not core_boons_set: # Use core boons only

            # Add all core boons to pool of available boons
            for boon in core_boons:
                if boon not in player_boons:
                    trimmed_boons_list.append(boon)

        else: # Use core + general boons
            boons_list = list(boon_data.keys())
            for boon in boons_list:
                
                ## [Remove unavailable sub-boons]
                # If any boons available are sub-boons...
                if boon_data[boon]["is_subboon"] == True:
                    print(f"found a subboon: {boon}")

                    # ... find their parent boon...
                    for parent_boon in boons_list:
                        if boon_data[parent_boon]["subboons"] != None:
                            if boon in boon_data[parent_boon]["subboons"]:
                                # ... and if their parent boon is NOT owned (or the sub-boon itself IS), remove the subboon from the list
                                print(f"found a subboon: {boon}'s PARENT: {parent_boon}")
                                if parent_boon in player_boons and boon not in player_boons:
                                    trimmed_boons_list.append(boon)
                                    print(f"subboon {boon} allowed to join selection")
                                    break
                
                ## [Remove already-selected boons]
                elif boon not in player_boons:
                    print(f"boon/subboon {boon} is not already owned, added to selection")
                    trimmed_boons_list.append(boon)
            
        # Find 3 random options from trimmed list
        for selection in range(3):
            new_boon = choice(trimmed_boons_list)
            boons_choice.append(new_boon)
            trimmed_boons_list.remove(new_boon)
        print(boons_choice)

        self.boon_icons = []
        # Only load boons (not sub-boons) for the display
        for current_boon in boons_choice:
            if not boon_data[current_boon]["is_subboon"]:
                current_boon_surf = pygame.image.load(f"assets/graphics/ui/interface_icons/boons_big/{current_boon}.png")
            else:
                current_boon_surf = pygame.image.load("assets/graphics/ui/interface_icons/boons_big/general_subboon.png")
            self.boon_icons.append(current_boon_surf)
        
        return boons_choice

    def display(self, options_list):
        prev_height = 0
        for num, boon in enumerate(options_list):
            added_height = self.boon_details(boon, num, prev_height)
            prev_height += added_height

    def boon_details(self, boon, num, prev_height):
        # Background
        if boon_data[boon]["desc2"] != "":
            bg_rect_size = (700, 167)
        else:
            bg_rect_size = (700, 127)

        x = (self.display_surface.get_size()[0] // 2) - (bg_rect_size[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - 280 + prev_height

        main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
        text_rect_pos = main_rect.topleft + pygame.math.Vector2(135, 80)
        text_rect_size = (bg_rect_size[0] - 20 - 20 - 100 - 15, bg_rect_size[1] - 50 - 10 - 20 - 20)

        # Icon + BG [Updates with hover]
        # icon_surface = pygame.image.load(f"assets/graphics/ui/interface_icons/boons_big/{boon}.png")
        icon_surface = self.boon_icons[num]
        icon_rect = icon_surface.get_rect(midleft = main_rect.midleft + pygame.math.Vector2(5, 0))

        pos = pygame.mouse.get_pos()
        hit = main_rect.collidepoint(pos)
        if hit:
            if player_inputs["light attack"]:
                createUI(self.display_surface, bg_rect_size[0], bg_rect_size[1], (x, y), "green_dark")
                self.add_boon(boon) # If LMB pressed, select boon
            else:
                createUI(self.display_surface, bg_rect_size[0], bg_rect_size[1], (x, y), "green")
            self.display_surface.blit(self.big_boon_frame_selected, icon_rect)
        else:
            createUI(self.display_surface, bg_rect_size[0], bg_rect_size[1], (x, y), "dark")
            self.display_surface.blit(self.big_boon_frame, icon_rect)
        self.display_surface.blit(icon_surface, icon_rect)

        createUI(self.display_surface, text_rect_size[0], text_rect_size[1], text_rect_pos, "basic")

        # Name
        title_surface = self.font16.render(f"| {boon_data[f'{boon}']['name'].upper()}", True, TEXT_TITLE_COLOUR)
        title_rect = title_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(115, 15))
        self.display_surface.blit(title_surface, title_rect)
         
        # Subtext 
        if boon_data[f'{boon}']['parent'] != None: 
            parent = boon_data[f'{boon}']['parent'] 
            subtext = f"{boon_data[f'{boon}']['cat']} | {boon_data[f'{parent}']['name']}" 
        else: 
            subtext = boon_data[f'{boon}']['cat'] 
 
        cat_surface = self.font12.render(f"| {subtext.upper()}", True, TEXT_TITLE_COLOUR) 
        cat_rect = cat_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(116, 40)) 
        self.display_surface.blit(cat_surface, cat_rect) 

        # Desc 1
        desc1 = boon_data[f"{boon}"]["desc1"]
        split_current_line = desc1.split("|")
        while len(split_current_line) < 4:
            split_current_line.append("")
        for subline in range(4):
            text_surf = self.font12.render(split_current_line[subline], False, UI_BG_COLOUR)
            text_rect = text_surf.get_rect(topleft = text_rect_pos + pygame.math.Vector2(0, (subline * 15)))
            self.display_surface.blit(text_surf, text_rect)

        # Desc 2
        desc2 = boon_data[f"{boon}"]["desc2"]
        split_current_line = desc2.split("|")
        while len(split_current_line) < 4:
            split_current_line.append("")
        for subline in range(4):
            text_surf = self.font12.render(split_current_line[subline], False, UI_BG_COLOUR)
            text_rect = text_surf.get_rect(topleft = text_rect_pos + pygame.math.Vector2(0, 40 + subline * 15))
            self.display_surface.blit(text_surf, text_rect)
        
        return bg_rect_size[1] + 40

    def add_boon(self, boon):
        interface_details["boons"]["list"].append(boon)
        self.enable_player_control()
        player_inputs["light attack"] = False

# Pause Menu
class pauseMenu:
    def __init__(self, exit_effect):
        self.display_surface = pygame.display.get_surface()
        self.font18 = pygame.font.Font(UI_FONT, 18) 
        self.font16 = pygame.font.Font(UI_FONT, 16) 
        self.font14 = pygame.font.Font(UI_FONT, 14) 
        self.font12 = pygame.font.Font(UI_FONT, 12) 
        self.font11 = pygame.font.Font(UI_FONT, 11) 

        self.exit_effect = exit_effect

        self.click_time = None
        self.clicked = False

        self.options_list = ["resume game", "difficulty", "controls", "settings", "exit game"]
        self.difficulty_submenu = False
        self.controls_submenu = False
        self.settings_submenu = False
        self.any_submenu_open = False

        self.assigning_key = None

    def selection_cooldown(self):
        if self.clicked:
            current_time = pygame.time.get_ticks()
            if current_time - self.click_time >= 100:
                self.clicked = False
    
    # PAUSE MENU
    def pauseMenu(self, player):
        bg_rect_size = self.draw_bg()

        for num, option in enumerate(self.options_list):
            self.menu_details(option, num, bg_rect_size, player)

        self.update()
    
    def draw_bg(self, width = 240, height = 300, title = ""):
        bg_rect_size = (width, height) 
        bg_x = (self.display_surface.get_size()[0] // 2) - (bg_rect_size[0] // 2)
        bg_y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2)
 
        main_rect = pygame.Rect(bg_x, bg_y, bg_rect_size[0], bg_rect_size[1]) 
        createUI(self.display_surface, bg_rect_size[0], bg_rect_size[1], (bg_x, bg_y), "dark")

        if title != "":
            title_surface = self.font18.render(f"| {title.upper()}", True, TEXT_TITLE_COLOUR)
            title_rect = title_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(10, 20))
            self.display_surface.blit(title_surface, title_rect)

        return bg_rect_size

    def menu_details(self, option, num, bg, player):
        item_rect_size = (220, 10) 
        x = (self.display_surface.get_size()[0] // 2) - (item_rect_size[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (item_rect_size[1] // 2) - (bg[1] // 2) + (num * 60) + 30

        main_rect = pygame.Rect(x, y, item_rect_size[0], item_rect_size[1]) 
        collide_rect = pygame.Rect(x - 20, y - 20, item_rect_size[0] + 40, item_rect_size[1] + 40) 
        text_rect_pos = main_rect.topleft
        text_rect_size = (item_rect_size[0], item_rect_size[1]) 

        # Rect updates
        pos = pygame.mouse.get_pos() 
        hit = collide_rect.collidepoint(pos) 
        if hit: createUI(self.display_surface, text_rect_size[0], text_rect_size[1], text_rect_pos, "green") 
        else: createUI(self.display_surface, text_rect_size[0], text_rect_size[1], text_rect_pos) 

        if hit and player_inputs["light attack"] and not self.any_submenu_open:
            match num:
                case 0: self.close_menu(player)
                case 1: self.difficulty_submenu = True
                case 2: self.controls_submenu = True
                case 3: self.settings_submenu = True
                case 4: self.exit_game(player)

            self.clicked = True 
            self.click_time = pygame.time.get_ticks()
            player_inputs["light attack"] = False

        # Name 
        name_surface = self.font16.render(f"| {option.upper()}", True, UI_BG_COLOUR) 
        name_rect = name_surface.get_rect(midleft = main_rect.midleft + pygame.math.Vector2(0, 0))
        self.display_surface.blit(name_surface, name_rect)
    
    ## CONTROLS SUBMENU
    def controlsMenu(self):
        self.any_submenu_open = True
        bg_rect_size = self.draw_bg(720, 400, "controls")

        for num, option in enumerate(controls_data):
            self.controls_details(option, num, bg_rect_size)

    def controls_details(self, option, num, bg):
        # Individual Controls
        item_rect_size = (220, 10) 
        x = (self.display_surface.get_size()[0] // 2) - (item_rect_size[0] // 2) - 240 + 20
        y = (self.display_surface.get_size()[1] // 2) - (item_rect_size[1] // 2) - (bg[1] // 2) + (num * 60) + 30 + 40

        if num >= 6:
            x += 240 + 20 + 100
            y = (self.display_surface.get_size()[1] // 2) - (item_rect_size[1] // 2) - (bg[1] // 2) + ((num-6) * 60) + 30 + 40

        main_rect = pygame.Rect(x, y, item_rect_size[0], item_rect_size[1]) 
        text_rect_pos = main_rect.topleft
        text_rect_size = (item_rect_size[0], item_rect_size[1]) 

        createUI(self.display_surface, text_rect_size[0], text_rect_size[1], text_rect_pos, "basic") 

        # Name 
        name_surface = self.font14.render(f"{option.upper()}", True, UI_BG_COLOUR) 
        name_rect = name_surface.get_rect(midleft = main_rect.midleft + pygame.math.Vector2(0, 0))
        self.display_surface.blit(name_surface, name_rect)

        self.control_input(option, num, item_rect_size, bg)
    
    def control_input(self, option, num, item_rect_size, bg):
        # Control Inputs
        input_rect_size = (30, 10) 
        x = (self.display_surface.get_size()[0] // 2) - (item_rect_size[0] // 2) - 240 + 20 + 240
        y = (self.display_surface.get_size()[1] // 2) - (item_rect_size[1] // 2) - (bg[1] // 2) + (num * 60) + 30 + 40

        if num >= 6:
            x += 240 + 20 + 100 # + 240
            y = (self.display_surface.get_size()[1] // 2) - (item_rect_size[1] // 2) - (bg[1] // 2) + ((num-6) * 60) + 30 + 40

        main_rect_input = pygame.Rect(x, y, input_rect_size[0], input_rect_size[1]) 
        collide_rect = pygame.Rect(x + 5, y - 20, input_rect_size[0] + 40, input_rect_size[1] + 40) 
        text_rect_input_pos = main_rect_input.topleft + pygame.math.Vector2(25, 0)
        text_rect_input_size = (input_rect_size[0], input_rect_size[1]) 

        pos = pygame.mouse.get_pos() 
        hit = collide_rect.collidepoint(pos) 
        # if hit: createUI(self.display_surface, text_rect_input_size[0], text_rect_input_size[1], text_rect_input_pos, "green") 
        # else: createUI(self.display_surface, text_rect_input_size[0], text_rect_input_size[1], text_rect_input_pos)
        if hit and player_inputs["light attack"]:
            createUI(self.display_surface, text_rect_input_size[0], text_rect_input_size[1], text_rect_input_pos, "green_dark") 
            self.assigning_key = option
            player_inputs["light attack"] = False
        elif hit: 
            createUI(self.display_surface, text_rect_input_size[0], text_rect_input_size[1], text_rect_input_pos, "green") 
        else:
            createUI(self.display_surface, text_rect_input_size[0], text_rect_input_size[1], text_rect_input_pos) 

        # Name 
        name_surface = self.font14.render(f"{controls_data[option].upper()}", True, UI_BG_COLOUR) 
        name_rect = name_surface.get_rect(midleft = main_rect_input.midleft + pygame.math.Vector2(20, 0))
        self.display_surface.blit(name_surface, name_rect)

    ## DIFFICULLTY SUBMENU
    def difficultyMenu(self):
        self.any_submenu_open = True
        bg_rect_size = self.draw_bg(848, 400, "difficulty")

        for num, option in enumerate(difficulty_data):
            self.difficulty_details(option, num, bg_rect_size)
    
    def difficulty_details(self, option, num, bg):
        # Individual Diff. Settings
        item_rect_size = (200, 10) 
        x = (self.display_surface.get_size()[0] // 2) - (item_rect_size[0] // 2) - 240 + 20 - 64
        y = (self.display_surface.get_size()[1] // 2) - (item_rect_size[1] // 2) - (bg[1] // 2) + (num * 60) + 30 + 40

        if num >= 6:
            x += 240 + 20 + 100 + 64
            y = (self.display_surface.get_size()[1] // 2) - (item_rect_size[1] // 2) - (bg[1] // 2) + ((num-6) * 60) + 30 + 40

        main_rect = pygame.Rect(x, y, item_rect_size[0], item_rect_size[1]) 
        text_rect_pos = main_rect.topleft
        text_rect_size = (item_rect_size[0], item_rect_size[1]) 

        createUI(self.display_surface, text_rect_size[0], text_rect_size[1], text_rect_pos, "basic") 

        # Name 
        name_surface = self.font14.render(f"{option.upper()}", True, UI_BG_COLOUR) 
        name_rect = name_surface.get_rect(midleft = main_rect.midleft + pygame.math.Vector2(0, 0))
        self.display_surface.blit(name_surface, name_rect)

        self.difficulty_display(option, num, item_rect_size, bg)
    
    def difficulty_display(self, option, num, item_rect_size, bg):
        # Diff. values display
        input_rect_size = (50, 10) 
        x = (self.display_surface.get_size()[0] // 2) - (item_rect_size[0] // 2) - 240 + 20 + 220 - 32
        y = (self.display_surface.get_size()[1] // 2) - (item_rect_size[1] // 2) - (bg[1] // 2) + (num * 60) + 30 + 40

        if num >= 6:
            x += 240 + 20 + 100 + 32 + 32
            y = (self.display_surface.get_size()[1] // 2) - (item_rect_size[1] // 2) - (bg[1] // 2) + ((num-6) * 60) + 30 + 40

        main_rect_input = pygame.Rect(x, y, input_rect_size[0], input_rect_size[1]) 
        collide_rect = pygame.Rect(x + 5, y - 20, input_rect_size[0] + 40, input_rect_size[1] + 40) 
        text_rect_input_pos = main_rect_input.topleft + pygame.math.Vector2(25, 0)
        text_rect_input_size = (input_rect_size[0], input_rect_size[1]) 

        createUI(self.display_surface, text_rect_input_size[0], text_rect_input_size[1], text_rect_input_pos, "basic") 

        # todo: clean up both buttons
    
        # Button [add]
        button_rect = pygame.Rect(main_rect_input.right + 50, main_rect_input.top - 8, 32, 32) 
        pos = pygame.mouse.get_pos() 
        button_hit = button_rect.collidepoint(pos) 

        right_icon = pygame.image.load("assets/graphics/ui/button_icons/right.png").convert_alpha() 
        button_surf = pygame.image.load("assets/graphics/ui/interface/tall_box.png").convert_alpha()
        if button_hit and self.clicked: 
            button_surf = pygame.image.load("assets/graphics/ui/interface/tall_box_active.png").convert_alpha() 
            right_icon = pygame.image.load("assets/graphics/ui/button_icons/right_active.png").convert_alpha() 
        elif button_hit: 
            if player_inputs["light attack"] and not self.clicked and difficulty_data[option] < 2: 
                difficulty_data[option] = round(difficulty_data[option] + 0.1, 1) 
 
                self.clicked = True 
                self.click_time = pygame.time.get_ticks() 
                player_inputs["light attack"] = False
            else: player_inputs["light attack"] = False
            button_surf = pygame.image.load("assets/graphics/ui/interface/tall_box_selected.png").convert_alpha() 
 
        button_rect = button_surf.get_rect(midleft = main_rect_input.midright + pygame.math.Vector2(50, 0)) 
        icon_rect = button_surf.get_rect(midleft = main_rect_input.midright + pygame.math.Vector2(50, 9)) 
        self.display_surface.blit(button_surf, button_rect) 
        self.display_surface.blit(right_icon, icon_rect)

        # Button [subtract]
        button_rect = pygame.Rect(main_rect_input.left - 30, main_rect_input.top - 8, 32, 32) 
        pos = pygame.mouse.get_pos() 
        button_hit = button_rect.collidepoint(pos) 

        left_icon = pygame.image.load("assets/graphics/ui/button_icons/left.png").convert_alpha() 
        button_surf = pygame.image.load("assets/graphics/ui/interface/tall_box.png").convert_alpha()
        if button_hit and self.clicked: 
            button_surf = pygame.image.load("assets/graphics/ui/interface/tall_box_active.png").convert_alpha() 
            left_icon = pygame.image.load("assets/graphics/ui/button_icons/right_active.png").convert_alpha() 
        elif button_hit: 
            if player_inputs["light attack"] and not self.clicked and difficulty_data[option] > 0.1: 
                difficulty_data[option] = round(difficulty_data[option] - 0.1, 1) 
 
                self.clicked = True 
                self.click_time = pygame.time.get_ticks() 
                player_inputs["light attack"] = False
            else: player_inputs["light attack"] = False
            button_surf = pygame.image.load("assets/graphics/ui/interface/tall_box_selected.png").convert_alpha() 
 
        button_rect = button_surf.get_rect(midleft = main_rect_input.midleft + pygame.math.Vector2(-30, 0)) 
        icon_rect = button_surf.get_rect(midleft = main_rect_input.midleft + pygame.math.Vector2(-30, 9)) 
        self.display_surface.blit(button_surf, button_rect) 
        self.display_surface.blit(left_icon, icon_rect) 

        # Name 
        name_surface = self.font14.render(f"x{difficulty_data[option]}", True, UI_BG_COLOUR) 
        name_rect = name_surface.get_rect(midleft = main_rect_input.midleft + pygame.math.Vector2(20, 0))
        self.display_surface.blit(name_surface, name_rect)

    ## OTHER
    def close_menu(self, player):
        player.esc_open = False
        player.any_interface_open = False
        player.resting = False
    
    def exit_game(self, player):
        self.close_menu(player)
        print("Saving and returning to main menu.")
        self.exit_effect()

    def check_return(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.difficulty_submenu = False
            self.controls_submenu = False
            self.settings_submenu = False
            self.any_submenu_open = False


    def update(self):
        self.selection_cooldown()
        if self.controls_submenu: self.controlsMenu()
        if self.difficulty_submenu: self.difficultyMenu()
        if self.any_submenu_open: self.check_return()