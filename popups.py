import pygame
from settings import *
from debug import debug
from support import *

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
        y = self.display_surface.get_size()[1] - (PROMPT_HEIGHT + PROMPT_GAP) # * len(current_prompts)

        text_surface = self.font.render(str(f"[{button}] {text}"), False, TEXT_COLOUR).convert_alpha()
        text_rect = text_surface.get_rect(center = (x, y))

        self.displayPrompt(text_rect, text_surface)
    
    def displayPrompt(self, rect, surface):
        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, rect.inflate(10, 10))
        self.display_surface.blit(surface, rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, rect.inflate(10, 10), 4)

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

            if keys[pygame.K_q]:
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

        self.selection_index = 0
        self.selection_time = None
        self.can_move_selection = True
        self.showing_details = False

        self.details_toggle_time = None
        self.details_can_toggle = True

        self.options_list = ["equipment", "inventory", "status", "system"]
        self.icons_list = import_folder("assets/graphics/ui/menu/menu_options")

        self.resource_name_list = list(resources.keys())
        self.resource_num_list = list(resources.values())
        self.resource_icon_list = import_folder("assets/graphics/ui/resources")
        self.resource_icon_list_highres = import_folder("assets/graphics/resources")

        self.menu = itemMenu()

    def selection_cooldown(self):
        if not self.can_move_selection:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 200:
                self.can_move_selection = True
        
        if not self.details_can_toggle:
            current_time = pygame.time.get_ticks()
            if current_time - self.details_toggle_time >= 200:
                self.details_can_toggle = True
    
    def input(self, player):
        keys = pygame.key.get_pressed()

        if self.can_move_selection and self.showing_details:
            if keys[pygame.K_DOWN] and self.selection_index < len(self.resource_name_list) - 1:
                self.selection_index += 1
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_UP] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()

            # if keys[pygame.K_SPACE]:
            #     self.can_move_selection = False
            #     self.selection_time = pygame.time.get_ticks()
            #     print(f"{len(self.options_list)}, {self.options_list}")
            #     self.triggered_effect(self.options_list[self.selection_index], player)
        
        if self.details_can_toggle:
            if keys[pygame.K_LSHIFT] and not self.showing_details:
                # player.resting = True
                self.showing_details = True
                self.details_can_toggle = False
                self.details_toggle_time = pygame.time.get_ticks()
                
            elif keys[pygame.K_LSHIFT] and self.showing_details:
                player.resting = False
                self.showing_details = False
                self.details_can_toggle = False
                self.details_toggle_time = pygame.time.get_ticks()
    
    # def triggered_effect(self, button, player):
    #     player.submenu_open = True

    #     if self.options_list[self.selection_index] == "inventory":
    #         player.menu_inventory = True
    #     elif self.options_list[self.selection_index] == "status":
    #         player.menu_status = True
    #     elif self.options_list[self.selection_index] == "system":
    #         player.menu_system = True
    #     elif self.options_list[self.selection_index] == "equipment":
    #         player.menu_equipment = True
    
    def displayMenu(self, player):
        colour = UPGRADE_TEXT_COLOUR
        self.input(player)
        self.selection_cooldown()

        # KINGSEEKER Display
        bg_rect_size = (150, 215)
        option_rect_size = (25, 25)
        x = (self.display_surface.get_size()[0] - 170) # - (bg_rect_size[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2) + 240
        main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])

        title_surface = self.font.render("ITEMS", True, colour)
        title_rect = title_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(5, -15))
        text_fade = pygame.Surface((title_rect.w + 10, title_rect.h + 10)).convert_alpha()
        text_fade.fill(TEXT_BG_COLOUR)
        text_fade_rect = title_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(0, -20))

        self.display_surface.blit(text_fade, text_fade_rect)
        self.display_surface.blit(title_surface, title_rect)

        for resource in self.resource_name_list:
            index = self.resource_name_list.index(resource)
            if index >= 6:
                rect = pygame.Rect(x + 90, y + (option_rect_size[1] + 5) * (self.resource_name_list.index(resource) - 6), option_rect_size[0], option_rect_size[1])
                self.menu.display(self.display_surface, self.selection_index, index, resource, rect, self.resource_num_list[index], self.showing_details)
            else:
                rect = pygame.Rect(x, y + (option_rect_size[1] + 5) * self.resource_name_list.index(resource), option_rect_size[0], option_rect_size[1])
                self.menu.display(self.display_surface, self.selection_index, index, resource, rect, self.resource_num_list[index], self.showing_details)

        if self.showing_details: self.item_details(player, self.resource_name_list[self.selection_index], pygame.font.Font(UI_FONT, 18))

        # Extra lines
        tt1_surface = self.font.render("ESC: Close items view", True, colour)
        tt1_rect = tt1_surface.get_rect(midleft = (10, 675))
        text_fade_tt1 = pygame.Surface((tt1_rect.w + 10, tt1_rect.h + 10)).convert_alpha()
        text_fade_tt1.fill(TEXT_BG_COLOUR)
        text_fade_tt1_rect = tt1_surface.get_rect(midleft = tt1_rect.midleft + pygame.math.Vector2(-5, -5))

        tt2_surface = self.font.render("SHIFT: Toggle item details", True, colour)
        tt2_rect = tt2_surface.get_rect(midleft = (10, 700))
        text_fade_tt2 = pygame.Surface((tt2_rect.w + 10, tt2_rect.h + 10)).convert_alpha()
        text_fade_tt2.fill(TEXT_BG_COLOUR)
        text_fade_tt2_rect = tt2_surface.get_rect(midleft = tt2_rect.midleft + pygame.math.Vector2(-5, -5))

        self.display_surface.blit(text_fade_tt1, text_fade_tt1_rect)
        self.display_surface.blit(tt1_surface, tt1_rect)
        self.display_surface.blit(text_fade_tt2, text_fade_tt2_rect)
        self.display_surface.blit(tt2_surface, tt2_rect)
    
    def item_details(self, player, resource, font):
        # Background
        bg_rect_size = (600, 167)
        x = (self.display_surface.get_size()[0] - 790) # - (bg_rect_size[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2) + 222
        main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, main_rect.inflate(10, 10))
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, main_rect.inflate(10, 10), 3)

        # Name
        title_surface = font.render(f"{resource.title()}", True, "white")
        title_rect = title_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(70, 15))
        text_fade = pygame.Surface((title_rect.w + 10, title_rect.h + 10)).convert_alpha()
        text_fade.fill(TEXT_BG_COLOUR)
        text_fade_rect = title_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(65, 10))
        self.display_surface.blit(text_fade, text_fade_rect)
        self.display_surface.blit(title_surface, title_rect)

        # Image
        img_rect = pygame.Rect(main_rect.topleft[0], main_rect.topleft[1], 60, 60)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, img_rect)
        index = self.resource_name_list.index(resource)
        self.display_surface.blit(self.resource_icon_list_highres[index], img_rect)

        # Category
        cat = resource_details[f"{resource}"][0]
        cat_surface = pygame.font.Font(UI_FONT, 10).render(cat, True, "white")
        cat_rect = cat_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(70, 40))
        cat_fade = pygame.Surface((cat_rect.w + 10, cat_rect.h + 10)).convert_alpha()
        cat_fade.fill(TEXT_BG_COLOUR)
        cat_fade_rect = cat_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(65, 35))
        self.display_surface.blit(cat_fade, cat_fade_rect)
        self.display_surface.blit(cat_surface, cat_rect)

        # Can by found by...
        found_text = resource_details[f"{resource}"][2]
        split_current_line = found_text.split("|")
        while len(split_current_line) < 4:
            split_current_line.append("")
        for subline in range(4):
            text_surf = pygame.font.Font(UI_FONT, 12).render(split_current_line[subline], False, "white")
            text_rect = text_surf.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(5, 75 + (subline * 15)))
            self.display_surface.blit(text_surf, text_rect)

        # separator_rect = pygame.Rect(main_rect.midleft[0] + 5, main_rect.midleft[1] + 20, 530, 1)
        # pygame.draw.rect(self.display_surface, "white", separator_rect)

        # Can be used in...
        used_text = resource_details[f"{resource}"][3]
        split_current_line = used_text.split("|")
        while len(split_current_line) < 4:
            split_current_line.append("")
        for subline in range(4):
            text_surf = pygame.font.Font(UI_FONT, 12).render(split_current_line[subline], False, "white")
            text_rect = text_surf.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(5, 115 + (subline * 15)))
            self.display_surface.blit(text_surf, text_rect)

class itemMenu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = self.font = pygame.font.Font(UI_FONT, PROMPT_FONT_SIZE)

        self.options_list = ["equipment", "inventory", "status", "system"]
        self.icons_list = import_folder("assets/graphics/ui/menu/menu_options")
        self.icons_selected_list = import_folder("assets/graphics/ui/menu/menu_options_selected")

        self.resource_name_list = list(resources.keys())
        self.resource_num_list = list(resources.values())
        self.resource_icon_list = import_folder("assets/graphics/ui/resources")

    def display_names(self, surface, name, rect, num):
        #colour = UPGRADE_TEXT_COLOUR_SELECTED if selected else UPGRADE_TEXT_COLOUR
        colour = UPGRADE_TEXT_COLOUR

        title_surface = self.font.render(str(num), True, colour)
        title_rect = title_surface.get_rect(midleft = rect.midright + pygame.math.Vector2(10, 0))

        text_fade = pygame.Surface((title_rect.w + 10, title_rect.h + 10)).convert_alpha()
        text_fade.fill(TEXT_BG_COLOUR)
        text_fade_rect = title_surface.get_rect(midleft = rect.midright + pygame.math.Vector2(5, -5))

        surface.blit(text_fade, text_fade_rect)
        surface.blit(title_surface, title_rect)

    def display(self, surface, selection_num, index, name, rect, num, trigger):
        if index == selection_num and trigger:
            pygame.draw.rect(surface, "#993614", rect, 3)
        else:
            pygame.draw.rect(surface, UI_BORDER_COLOUR, rect, 3)
        self.display_surface.blit(self.resource_icon_list[index], rect)
        self.display_names(surface, name, rect, num)

# Inventory
class invMenu:
    def __init__(self, toggle_screen_effect):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, PROMPT_FONT_SIZE)
        self.title_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.bg_image = pygame.image.load("assets/graphics/ui/menu/background/large_bg.png").convert_alpha()
        self.toggle_screen_effect = toggle_screen_effect

        self.horizontal_bar = pygame.image.load("assets/graphics/ui/menu/background/horizontal_bar.png").convert_alpha()
        self.horizontal_bar_thin = pygame.image.load("assets/graphics/ui/menu/background/horizontal_bar_thin.png").convert_alpha()
        self.vertical_bar = pygame.image.load("assets/graphics/ui/menu/background/vertical_bar.png").convert_alpha()
        self.vertical_bar_thin = pygame.image.load("assets/graphics/ui/menu/background/vertical_bar_thin.png").convert_alpha()

        self.selection_index = 0
        self.selection_time = None
        self.can_move_selection = True

        self.item_selection_index = 0
        self.item_list_index = 0
        self.item_selection_time = None
        self.can_move_item_selection = True

        self.options_list = ["Consumables", "Ores", "Key Items", "Spells", "Weapons", "Armour", "Rings"]
        self.current_category = self.options_list[self.selection_index]

        self.items_list = player_inventory[self.options_list[self.selection_index]]
        self.items_list_num = player_inventory[f'{self.options_list[self.selection_index]}_num']
        self.display_list = self.items_list[slice(4)]

        self.inventory_menu = itemInv()
        self.status_menu = itemStatus()

        self.getPlayerInfo()
        self.player_attributes_surfs = []
        for stat in self.player_attributes_names:
            img = pygame.transform.scale(pygame.image.load(f"assets/graphics/ui/menu/stats/{stat}.png"), (30, 30)).convert_alpha()
            self.player_attributes_surfs.append(img)
        self.player_stats_surfs = []
        for stat in self.player_stats_names:
            img = pygame.transform.scale(pygame.image.load(f"assets/graphics/ui/menu/stats/{stat}.png"), (30, 30)).convert_alpha()
            self.player_stats_surfs.append(img)
        self.player_resistances_surfs = []
        for stat in self.player_resistances_names:
            img = pygame.transform.scale(pygame.image.load(f"assets/graphics/ui/menu/stats/{stat}.png"), (30, 30)).convert_alpha()
            self.player_resistances_surfs.append(img)

        self.separator_short = pygame.image.load("assets/graphics/ui/menu/background/separator_short.png").convert_alpha()
        self.horizontal_bar = pygame.image.load("assets/graphics/ui/menu/background/horizontal_bar.png").convert_alpha()
        self.horizontal_bar_thin = pygame.image.load("assets/graphics/ui/menu/background/horizontal_bar_thin.png").convert_alpha()
        self.corner_topright = pygame.image.load("assets/graphics/ui/menu/background/corner_topright.png").convert_alpha()
        self.corner_topleft = pygame.image.load("assets/graphics/ui/menu/background/corner_topleft.png").convert_alpha()
        self.corner_bottomright = pygame.image.load("assets/graphics/ui/menu/background/corner_bottomright.png").convert_alpha()
        self.corner_bottomleft = pygame.image.load("assets/graphics/ui/menu/background/corner_bottomleft.png").convert_alpha()
        self.connector_vertical_small = pygame.image.load("assets/graphics/ui/menu/background/connector_vertical_small.png").convert_alpha()
        self.connector_horizontal_small = pygame.image.load("assets/graphics/ui/menu/background/connector_horizontal_small.png").convert_alpha()

    def selection_cooldown(self):
        if not self.can_move_selection:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 100:
                self.can_move_selection = True

        if not self.can_move_item_selection:
            current_time = pygame.time.get_ticks()
            if current_time - self.item_selection_time >= 50:
                self.can_move_item_selection = True
    
    def input(self, player):
        keys = pygame.key.get_pressed()

        if self.can_move_selection:
            if keys[pygame.K_RIGHT] and self.selection_index < len(self.options_list) - 1:
                self.selection_index += 1
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()
                self.item_selection_index = 0
                self.item_list_index = 0

                self.items_list = player_inventory[self.options_list[self.selection_index]]
                self.display_list = self.items_list[slice(4)]
                self.current_category = self.options_list[self.selection_index]
                self.items_list_num = player_inventory[f'{self.options_list[self.selection_index]}_num']

            elif keys[pygame.K_LEFT] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()
                self.item_selection_index = 0
                self.item_list_index = 0

                self.items_list = player_inventory[self.options_list[self.selection_index]]
                self.display_list = self.items_list[slice(4)]
                self.current_category = self.options_list[self.selection_index]
                self.items_list_num = player_inventory[f'{self.options_list[self.selection_index]}_num']
        
        # Items
        if self.can_move_item_selection:

            if self.item_list_index < len(self.items_list) - 1:
                if keys[pygame.K_DOWN] and self.item_selection_index < len(self.items_list) - 1:
                    self.item_selection_index += 1
                    self.item_list_index += 1
                    self.can_move_item_selection = False
                    self.item_selection_time = pygame.time.get_ticks()

                    if self.item_selection_index >= len(self.display_list):
                        self.display_list.pop(0)
                        self.display_list.append(self.items_list[self.item_list_index])
                        self.item_selection_index -= 1

            if self.item_list_index >= 1:
                if keys[pygame.K_UP] and self.item_selection_index >= 1:
                    self.item_selection_index -= 1
                    self.item_list_index -= 1
                    self.can_move_item_selection = False
                    self.item_selection_time = pygame.time.get_ticks()

                elif keys[pygame.K_UP] and self.item_selection_index == 0:
                    self.can_move_item_selection = False
                    self.item_selection_time = pygame.time.get_ticks()

                    self.item_list_index -= 1
                    self.display_list.pop(-1)
                    self.display_list.insert(0, self.items_list[self.item_list_index])
                    # self.item_selection_index += 1

            if keys[pygame.K_SPACE]:
                self.can_move_item_selection = False
                self.item_selection_time = pygame.time.get_ticks()
                print(f"Index: {self.item_selection_index}/{self.item_list_index} | Display List: {len(self.display_list)}")
                #print(f"Current Item: {self.items_list[self.item_selection_index]}")
                # self.triggered_effect(self.options_list[self.selection_index], player)
    
    def resetDisplay(self):
        self.display_list = self.items_list[slice(4)]

    def getPlayerInfo(self):
        self.player_attributes = []
        self.player_stats = []
        self.player_resistances = []
        self.player_details = []
        
        self.player_attributes_names = []
        self.player_stats_names = []
        self.player_resistances_names = []
        self.player_details_names = []

        ## Stat Numbers ##
        # Attributes
        self.player_attributes.append(player_data['values']['level'])
        self.player_attributes.append(player_data['values']['souls'])
        for item in player_data['attributes'].values():
            self.player_attributes.append(item)
        self.player_attributes.append(player_data['values']['humanity'])

        # Stats
        for item in player_data['dependent_variables'].values():
            self.player_stats.append(item)
        for item in player_data['defense'].values():
            self.player_stats.append(item)
        self.player_stats.pop(4)
        self.player_stats.pop(8)
        self.player_stats.pop(8)
        
        # Extra Stats/Resistances
        for item in player_data['resistances'].values():
            self.player_resistances.append(item)

        ## Stat Names ##
        # Attributes
        self.player_attributes_names.append("Level")
        self.player_attributes_names.append("Souls")
        for item in player_data['attributes']:
            self.player_attributes_names.append(item)
        self.player_attributes_names.append("Humanity")

        # Stats
        for item in player_data['dependent_variables']:
            self.player_stats_names.append(item)
        for item in player_data['defense']:
            self.player_stats_names.append(item)
        self.player_stats_names.pop(4)
        self.player_stats_names.pop(8)
        self.player_stats_names.pop(8)
        
        # Extra Stats/Resistances
        for item in player_data['resistances']:
            self.player_resistances_names.append(item)

        # Other Information
        self.player_details.append(player_data['status']['name'])
        self.player_details.append(player_data['status']['covenant'])
        self.player_details_names.append("Name")
        self.player_details_names.append("Covenant")

    def displayStatus(self, player):
        self.getPlayerInfo()

        item_rect_size = (30, 30)
        x = (self.display_surface.get_size()[0] // 2) - (self.bg_image.get_size()[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (self.bg_image.get_size()[1] // 2)

        # Name + Covenant
        for option in self.player_details:
            index = self.player_details.index(option)
            rect = pygame.Rect(x + 700, y + 150 + (item_rect_size[1] + 5) * index, item_rect_size[0], item_rect_size[1])
            self.status_menu.display_names(self.display_surface, str(option), self.player_details_names, index, player, self.player_details_names[index], 200, rect)

        # Attributes
        for option in self.player_attributes:
            index = self.player_attributes.index(option)
            rect = pygame.Rect(x + 700, y + 220 + (item_rect_size[1] + 5) * index, item_rect_size[0], item_rect_size[1])
            self.status_menu.display(self.display_surface, index, str(option), self.player_attributes_names, self.player_attributes_surfs, player, 200, rect)
        
        
        # UI Elements
        self.display_surface.blit(self.corner_topleft, (x + 655, y + 105))
        self.display_surface.blit(self.corner_topright, (x + 915, y + 105))
        self.display_surface.blit(self.corner_bottomright, (x + 915, y + 500))
        self.display_surface.blit(self.corner_bottomleft, (x + 655, y + 500))
        self.display_surface.blit(self.connector_vertical_small, (x + 658, y + 140))
        self.display_surface.blit(self.connector_vertical_small, (x + 964, y + 140))
        self.display_surface.blit(self.connector_horizontal_small, (x + 715, y + 108))
        self.display_surface.blit(self.connector_horizontal_small, (x + 715, y + 552))

        self.display_surface.blit(self.separator_short, (x + 705, y + 182))
        self.display_surface.blit(self.separator_short, (x + 705, y + 217))
        self.display_surface.blit(self.separator_short, (x + 705, y + 287))
        self.display_surface.blit(self.separator_short, (x + 705, y + 462))

    def displayInventory(self, player):
        self.input(player)
        self.selection_cooldown()

        bg_rect_size = (1000, 600)
        option_rect_size = (50, 50)
        item_rect_size = (80, 80)

        x = (self.display_surface.get_size()[0] // 2) - (self.bg_image.get_size()[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (self.bg_image.get_size()[1] // 2)

        main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
        # pygame.draw.rect(self.display_surface, UI_BG_COLOUR, main_rect.inflate(10, 10))
        # pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, main_rect.inflate(10, 10), 4)

        self.display_surface.blit(self.bg_image, main_rect)

        option_bg_rect = pygame.Rect(x + 50, y + 100, 412, 62)
        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, option_bg_rect.inflate(10, 10))
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, option_bg_rect.inflate(10, 10), 4)

        for option in self.options_list:
            index = self.options_list.index(option)
            rect = pygame.Rect(x + 50 + (option_rect_size[1] + 10) * self.options_list.index(option), y + 100, option_rect_size[0], option_rect_size[1])
            self.inventory_menu.display(self.display_surface, self.selection_index, index, option, self.display_list, rect, "category", self.current_category, self.items_list_num)

        for option in self.display_list:
            index = self.display_list.index(option)
            rect = pygame.Rect(x + 50, y + 200 + (item_rect_size[1] + 10) * self.display_list.index(option), item_rect_size[0], item_rect_size[1])
            self.inventory_menu.display(self.display_surface, self.item_selection_index, index, option, self.display_list, rect, "item", self.current_category, self.items_list_num)
        
        self.display_surface.blit(self.horizontal_bar_thin, (x + 110, y + 50))
        self.display_surface.blit(self.horizontal_bar_thin, (x + 110, y + 75))
        self.display_surface.blit(self.horizontal_bar, (x + 50, y + 190))
        self.display_surface.blit(self.horizontal_bar, (x + 50, y + 280))
        self.display_surface.blit(self.horizontal_bar, (x + 50, y + 280 + (90 * 1)))
        self.display_surface.blit(self.horizontal_bar, (x + 50, y + 280 + (90 * 2)))
        self.display_surface.blit(self.horizontal_bar, (x + 50, y + 280 + (90 * 3)))
        
        self.display_surface.blit(self.vertical_bar, (x + 130, y + 190))
        self.display_surface.blit(self.vertical_bar_thin, (x + 50, y + 190))

        title_surface = self.title_font.render("Inventory", True, TEXT_COLOUR)
        title_rect = pygame.Rect(x + 110, y + 30, title_surface.get_size()[0], title_surface.get_size()[1])
        # desc_surface = self.small_font.render("Check player attributes", True, TEXT_COLOUR)
        # desc_rect = pygame.Rect(x + 110, y + 60, desc_surface.get_size()[0], desc_surface.get_size()[1])
        
        self.display_surface.blit(pygame.transform.scale(pygame.image.load("assets/graphics/ui/menu/menu_options_selected/inventory_open.png"), (60, 60)).convert_alpha(), (title_rect.x - 70, title_rect.y - 10)) 
        self.display_surface.blit(title_surface, title_rect)

        self.displayStatus(player)

class itemInv:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        # self.rect = pygame.Rect(left, top, width, height)
        # self.desc_rect = pygame.Rect(left + 90, top, width * 6.4, height)
        self.font = pygame.font.Font(UI_FONT, PROMPT_FONT_SIZE)
        self.title_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.small_font = pygame.font.Font(UI_FONT, 11)
        self.type = type

        self.icons_list = import_folder("assets/graphics/ui/menu/item_categories")
        self.icons_selected_list = import_folder("assets/graphics/ui/menu/item_categories_selected")
        self.items_list = None

    def display_names(self, surface, name):
        bg_rect_size = (1000, 600)
        x = (self.display_surface.get_size()[0] // 2) - (bg_rect_size[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2)
        colour = UPGRADE_TEXT_COLOUR

        if self.type == "category":
            title_surface = self.small_font.render(name, True, colour)
            title_rect = pygame.Rect(x + 110, y + 25, title_surface.get_size()[0], title_surface.get_size()[1])

        elif self.type == "item":
            title_surface = self.font.render(name, True, colour)
            title_rect = title_surface.get_rect(midleft = self.rect.midright + pygame.math.Vector2(15, -26))

            desc_surface = self.small_font.render(f"{game_items[name]['short_desc']}", True, colour)
            desc_rect = title_surface.get_rect(midleft = self.rect.midright + pygame.math.Vector2(15, 0))
            desc2_surface = self.small_font.render(f"{game_items[name]['short_desc2']}", True, colour)
            desc2_rect = title_surface.get_rect(midleft = self.rect.midright + pygame.math.Vector2(15, 15))

            num_surface = self.small_font.render(f"{self.items_list_num[player_inventory[self.category].index(name)]}", True, colour)
            num_rect = num_surface.get_rect(bottomright = self.rect.bottomright + pygame.math.Vector2(-5, -5))

            surface.blit(desc_surface, desc_rect)
            surface.blit(desc2_surface, desc2_rect)
            if self.category == "Consumables" or self.category == "Ores":
                surface.blit(num_surface, num_rect)

        surface.blit(title_surface, title_rect)

    def display(self, surface, selection_num, index, name, list, rect, type, item_category, num_list):
        self.category = item_category
        self.items_list_num = num_list
        self.type = type
        self.items_list = import_folder(f"assets/graphics/inventory/items/{self.category}")

        self.rect = rect
        self.desc_rect = self.rect.copy()
        self.desc_rect.left += 90
        self.desc_rect.width *= 6.4

        if self.type == "category":
            if index == selection_num:
                pygame.draw.rect(surface, UI_BORDER_COLOUR, self.rect, 4)
                self.display_surface.blit(self.icons_selected_list[index], self.rect)
                self.display_names(surface, name)
            else:
                pygame.draw.rect(surface, UI_BORDER_COLOUR, self.rect, 4)
                self.display_surface.blit(self.icons_list[index], self.rect)

        elif self.type == "item":
            if index == selection_num:
                pygame.draw.rect(surface, HOVER_COLOUR, self.rect)
                pygame.draw.rect(surface, HOVER_COLOUR, self.desc_rect)

            #self.display_surface.blit(pygame.image.load("assets/graphics/inventory/items/item_stool.png").convert_alpha(), (self.rect.x, self.rect.y + 10, self.rect.w, self.rect.h))
            self.display_surface.blit(pygame.image.load(f"assets/graphics/inventory/items/{self.category}/{list[index]}.png").convert_alpha(), self.rect) 

            self.display_names(surface, name)

# Status
class statusMenu:
    def __init__(self, toggle_screen_effect):
        self.display_surface = pygame.display.get_surface()
        self.small_font = pygame.font.Font(UI_FONT, SMALL_FONT_SIZE)
        self.font = pygame.font.Font(UI_FONT, MEDIUM_FONT_SIZE)
        self.title_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.bg_image = pygame.image.load("assets/graphics/ui/menu/background/large_bg.png").convert_alpha()
        self.toggle_screen_effect = toggle_screen_effect

        self.status_menu = itemStatus()

        # Create lists of surfaces for each stat icon
        # Index will match that of the list of names/values
        # As such, index can be used to call the image too
        self.getPlayerInfo()

        self.player_attributes_surfs = []
        for stat in self.player_attributes_names:
            img = pygame.transform.scale(pygame.image.load(f"assets/graphics/ui/menu/stats/{stat}.png"), (30, 30)).convert_alpha()
            self.player_attributes_surfs.append(img)
        self.player_stats_surfs = []
        for stat in self.player_stats_names:
            img = pygame.transform.scale(pygame.image.load(f"assets/graphics/ui/menu/stats/{stat}.png"), (30, 30)).convert_alpha()
            self.player_stats_surfs.append(img)
        self.player_resistances_surfs = []
        for stat in self.player_resistances_names:
            img = pygame.transform.scale(pygame.image.load(f"assets/graphics/ui/menu/stats/{stat}.png"), (30, 30)).convert_alpha()
            self.player_resistances_surfs.append(img)

        self.separator = pygame.image.load("assets/graphics/ui/menu/background/separator.png").convert_alpha()
        self.horizontal_bar = pygame.image.load("assets/graphics/ui/menu/background/horizontal_bar.png").convert_alpha()
        self.horizontal_bar_thin = pygame.image.load("assets/graphics/ui/menu/background/horizontal_bar_thin.png").convert_alpha()
        self.corner_topright = pygame.image.load("assets/graphics/ui/menu/background/corner_topright.png").convert_alpha()
        self.corner_topleft = pygame.image.load("assets/graphics/ui/menu/background/corner_topleft.png").convert_alpha()
        self.corner_bottomright = pygame.image.load("assets/graphics/ui/menu/background/corner_bottomright.png").convert_alpha()
        self.corner_bottomleft = pygame.image.load("assets/graphics/ui/menu/background/corner_bottomleft.png").convert_alpha()
        self.connector_vertical = pygame.image.load("assets/graphics/ui/menu/background/connector_vertical.png").convert_alpha()
        self.connector_horizontal = pygame.image.load("assets/graphics/ui/menu/background/connector_horizontal.png").convert_alpha()
    
    def getPlayerInfo(self):
        self.player_attributes = []
        self.player_stats = []
        self.player_resistances = []
        self.player_details = []
        
        self.player_attributes_names = []
        self.player_stats_names = []
        self.player_resistances_names = []
        self.player_details_names = []

        ## Stat Numbers ##
        # Attributes
        self.player_attributes.append(player_data['values']['level'])
        self.player_attributes.append(player_data['values']['souls'])
        for item in player_data['attributes'].values():
            self.player_attributes.append(item)
        self.player_attributes.append(player_data['values']['humanity'])
        self.player_attributes.append(player_data['dependent_variables']['att. slots'])

        # Stats
        for item in player_data['dependent_variables'].values():
            self.player_stats.append(item)
        for item in player_data['defense'].values():
            self.player_stats.append(item)
        self.player_stats.pop(4)
        self.player_stats.pop(6)
        self.player_stats.pop(8)
        self.player_stats.pop(8)
        
        # Extra Stats/Resistances
        for item in player_data['resistances'].values():
            self.player_resistances.append(item)

        ## Stat Names ##
        # Attributes
        self.player_attributes_names.append("Level")
        self.player_attributes_names.append("Souls")
        for item in player_data['attributes']:
            self.player_attributes_names.append(item)
        self.player_attributes_names.append("Humanity")
        self.player_attributes_names.append("att. slots")

        # Stats
        for item in player_data['dependent_variables']:
            self.player_stats_names.append(item)
        for item in player_data['defense']:
            self.player_stats_names.append(item)
        self.player_stats_names.pop(4)
        self.player_stats_names.pop(6)
        self.player_stats_names.pop(8)
        self.player_stats_names.pop(8)
        
        # Extra Stats/Resistances
        for item in player_data['resistances']:
            self.player_resistances_names.append(item)

        # Other Information
        self.player_details.append(player_data['status']['name'])
        self.player_details.append(player_data['status']['covenant'])
        self.player_details_names.append("Name")
        self.player_details_names.append("Covenant")

    def displayStatus(self, player):
        self.getPlayerInfo()

        bg_rect_size = (1000, 600)
        item_rect_size = (30, 30)
        x = (self.display_surface.get_size()[0] // 2) - (self.bg_image.get_size()[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (self.bg_image.get_size()[1] // 2)
        main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
        self.display_surface.blit(self.bg_image, main_rect)

        # option_bg_rect = pygame.Rect(x + 50, y + 100, 412, 62)
        # pygame.draw.rect(self.display_surface, UI_BG_COLOUR, option_bg_rect.inflate(10, 10))
        # pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, option_bg_rect.inflate(10, 10), 4)

        # Name + Covenant
        for option in self.player_details:
            index = self.player_details.index(option)
            rect = pygame.Rect(x + 100, y + 150 + (item_rect_size[1] + 5) * index, item_rect_size[0], item_rect_size[1])
            self.status_menu.display_names(self.display_surface, str(option), self.player_details_names, index, player, self.player_details_names[index], 300, rect)

        for option in self.player_attributes:
            index = self.player_attributes.index(option)
            rect = pygame.Rect(x + 100, y + 220 + (item_rect_size[1] + 5) * index, item_rect_size[0], item_rect_size[1])
            self.status_menu.display(self.display_surface, index, str(option), self.player_attributes_names, self.player_attributes_surfs, player, 300, rect)
        
        for option in self.player_stats:
            index = self.player_stats.index(option)
            rect = pygame.Rect(x + 570, y + 150 + (item_rect_size[1] + 5) * index, item_rect_size[0], item_rect_size[1])
            self.status_menu.display(self.display_surface, index, str(option), self.player_stats_names, self.player_stats_surfs, player, 300, rect)
        
        # UI Elements
        self.display_surface.blit(self.horizontal_bar_thin, (x + 110, y + 50))
        self.display_surface.blit(self.horizontal_bar_thin, (x + 110, y + 75))

        self.display_surface.blit(self.corner_topleft, (x + 55, y + 105))
        self.display_surface.blit(self.corner_topright, (x + 415, y + 105))
        self.display_surface.blit(self.corner_bottomright, (x + 415, y + 550))
        self.display_surface.blit(self.corner_bottomleft, (x + 55, y + 550))
        self.display_surface.blit(self.connector_vertical, (x + 58, y + 140))
        self.display_surface.blit(self.connector_vertical, (x + 464, y + 140))
        self.display_surface.blit(self.connector_horizontal, (x + 115, y + 108))
        self.display_surface.blit(self.connector_horizontal, (x + 115, y + 602))

        self.display_surface.blit(self.corner_topleft, (x + 525, y + 105))
        self.display_surface.blit(self.corner_topright, (x + 885, y + 105))
        self.display_surface.blit(self.corner_bottomright, (x + 885, y + 550))
        self.display_surface.blit(self.corner_bottomleft, (x + 525, y + 550))
        self.display_surface.blit(self.connector_vertical, (x + 528, y + 140))
        self.display_surface.blit(self.connector_vertical, (x + 934, y + 140))
        self.display_surface.blit(self.connector_horizontal, (x + 585, y + 108))
        self.display_surface.blit(self.connector_horizontal, (x + 585, y + 602))

        self.display_surface.blit(self.separator, (x + 105, y + 182))
        self.display_surface.blit(self.separator, (x + 105, y + 217))
        self.display_surface.blit(self.separator, (x + 105, y + 287))
        self.display_surface.blit(self.separator, (x + 105, y + 462))

        self.display_surface.blit(self.separator, (x + 575, y + 287))
        self.display_surface.blit(self.separator, (x + 575, y + 357))
        self.display_surface.blit(self.separator, (x + 575, y + 427))

        title_surface = self.title_font.render("Status", True, TEXT_COLOUR)
        title_rect = pygame.Rect(x + 110, y + 30, title_surface.get_size()[0], title_surface.get_size()[1])
        desc_surface = self.small_font.render("Check player attributes", True, TEXT_COLOUR)
        desc_rect = pygame.Rect(x + 110, y + 60, desc_surface.get_size()[0], desc_surface.get_size()[1])
        
        self.display_surface.blit(pygame.transform.scale(pygame.image.load("assets/graphics/ui/menu/menu_options_selected/status_open.png"), (60, 60)).convert_alpha(), (title_rect.x - 70, title_rect.y - 10)) 
        self.display_surface.blit(title_surface, title_rect)
        self.display_surface.blit(desc_surface, desc_rect)

class itemStatus:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        # self.rect = pygame.Rect(left, top, width, height)
        # self.desc_rect = pygame.Rect(left + 90, top, width * 7.5, height)
        self.font = pygame.font.Font(UI_FONT, MEDIUM_FONT_SIZE)
        self.small_font = pygame.font.Font(UI_FONT, SMALL_FONT_SIZE)

    def display_names(self, surface, name, list, index, player, type, offset, rect):
        bg_rect_size = (1000, 600)
        x = (self.display_surface.get_size()[0] // 2) - (bg_rect_size[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2)
        colour = UPGRADE_TEXT_COLOUR

        if type == "Stat":
            if list[index].upper() == "HEALTH":
                num_surface = self.font.render(f"{player.health_target}/{name}", True, colour)
            elif list[index].upper() == "MANA":
                num_surface = self.font.render(f"{round(player.mana_target)}/{name}", True, colour)
            elif list[index].upper() == "EQUIP LOAD":
                num_surface = self.font.render(f"{name}/{player_data['dependent_variables']['max equip load']}", True, colour)
            else:
                num_surface = self.font.render(name, True, colour)

            if list[index].upper() == "ATTACK":
                text_surface = self.font.render("BASE WEAPON DMG", True, colour)
            elif list[index].upper() == "MAGIC DAMAGE":
                text_surface = self.font.render("BASE SPELL DMG", True, colour)
            else:
                text_surface = self.font.render(list[index].upper(), True, colour)

            num_rect = num_surface.get_rect(midright = rect.midright + pygame.math.Vector2(offset, -1))
            text_rect = text_surface.get_rect(midleft = rect.midright + pygame.math.Vector2(10, -1))
            surface.blit(num_surface, num_rect)
            surface.blit(text_surface, text_rect)

        elif type == "Covenant":
            num_surface = self.font.render(name, True, colour)
            text_surface = self.font.render(list[index].upper(), True, colour)

            num_rect = num_surface.get_rect(midright = rect.midright + pygame.math.Vector2(offset, -1))
            text_rect = text_surface.get_rect(midleft = rect.midright + pygame.math.Vector2(-20, -1))
            surface.blit(num_surface, num_rect)
            surface.blit(text_surface, text_rect)
        
        elif type == "Name":
            num_surface = self.font.render(name, True, colour)

            num_rect = num_surface.get_rect(center = rect.midleft + pygame.math.Vector2(offset - offset * 0.45, -1))
            surface.blit(num_surface, num_rect)

    def display(self, surface, index, name, list, surf_list, player, offset, rect):
        # Still lagging somewhat due to loading and transforming ALL the images every tick
        # Lag can still be very much reduced on other classes by moving all the rects and parameters into the functions
        # and calling the class in the __init__
        self.display_surface.blit(surf_list[index], rect) 
        self.display_names(surface, name, list, index, player, "Stat", offset, rect)

# Equipment
class equipMenu:
    def __init__(self, toggle_screen_effect, updated = False):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, PROMPT_FONT_SIZE)
        self.title_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.small_font = pygame.font.Font(UI_FONT, 11)
        self.bg_image = pygame.image.load("assets/graphics/ui/menu/background/large_bg.png").convert_alpha()
        self.toggle_screen_effect = toggle_screen_effect

        self.horizontal_bar = pygame.image.load("assets/graphics/ui/menu/background/horizontal_bar.png").convert_alpha()
        self.horizontal_bar_thin = pygame.image.load("assets/graphics/ui/menu/background/horizontal_bar_thin.png").convert_alpha()
        self.vertical_bar = pygame.image.load("assets/graphics/ui/menu/background/vertical_bar.png").convert_alpha()
        self.vertical_bar_thin = pygame.image.load("assets/graphics/ui/menu/background/vertical_bar_thin.png").convert_alpha()

        #self.selection_index = 0
        self.selection_index = [0, 0]
        self.selection_time = None
        self.can_move_selection = True

        self.separator_short = pygame.image.load("assets/graphics/ui/menu/background/separator_short.png").convert_alpha()
        self.horizontal_bar = pygame.image.load("assets/graphics/ui/menu/background/horizontal_bar.png").convert_alpha()
        self.horizontal_bar_thin = pygame.image.load("assets/graphics/ui/menu/background/horizontal_bar_thin.png").convert_alpha()
        self.corner_topright = pygame.image.load("assets/graphics/ui/menu/background/corner_topright.png").convert_alpha()
        self.corner_topleft = pygame.image.load("assets/graphics/ui/menu/background/corner_topleft.png").convert_alpha()
        self.corner_bottomright = pygame.image.load("assets/graphics/ui/menu/background/corner_bottomright.png").convert_alpha()
        self.corner_bottomleft = pygame.image.load("assets/graphics/ui/menu/background/corner_bottomleft.png").convert_alpha()
        self.connector_vertical_small = pygame.image.load("assets/graphics/ui/menu/background/connector_vertical_small.png").convert_alpha()
        self.connector_horizontal_small = pygame.image.load("assets/graphics/ui/menu/background/connector_horizontal_small.png").convert_alpha()

        self.equipment_categories = []
        self.current_category = ""
        self.display_categories_list = ["Right Hand", "Left Hand", "Quick Items", "Armour", "Rings"]
        #self.icons_list = import_folder("assets/graphics/ui/menu/equipment_categories")

        self.equip_menu = itemEquip(pygame.image.load("assets/graphics/inventory/items/item_stool.png").convert_alpha())
        self.status_menu = itemStatus()

        self.getPlayerInfo()
        self.player_attributes_surfs = []
        for stat in self.player_attributes_names:
            img = pygame.transform.scale(pygame.image.load(f"assets/graphics/ui/menu/stats/{stat}.png"), (30, 30)).convert_alpha()
            self.player_attributes_surfs.append(img)

        self.display_categories_surfs = []
        for cat in self.display_categories_list:
            img = pygame.image.load(f"assets/graphics/ui/menu/equipment_categories/{cat}.png").convert_alpha()
            self.display_categories_surfs.append(img)

        self.display_updated = updated # Re-set to false whenever opening the equipment menu OR changing an item in it

    def selection_cooldown(self):
        if not self.can_move_selection:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 100:
                self.can_move_selection = True
    
    def displayCategories(self):
        x = (self.display_surface.get_size()[0] // 2) - (self.bg_image.get_size()[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (self.bg_image.get_size()[1] // 2)

        for i in self.display_categories_list:
            icon = self.display_categories_surfs[self.display_categories_list.index(i)]

            if i == "Right Hand": self.display_surface.blit(icon, (x + 55, y + 148))
            elif i == "Left Hand": self.display_surface.blit(icon, (x + 325, y + 148))
            elif i == "Quick Items": self.display_surface.blit(icon, (x + 55, y + 253))
            elif i == "Armour": self.display_surface.blit(icon, (x + 55, y + 358))
            elif i == "Rings": self.display_surface.blit(icon, (x + 235, y + 358))
    
    def input(self, player):
        keys = pygame.key.get_pressed()

        if self.can_move_selection:
            if keys[pygame.K_RIGHT] and self.selection_index[0] <= 2:
                self.selection_index[0] += 1
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()

            elif keys[pygame.K_LEFT] and self.selection_index[0] >= 1:
                self.selection_index[0] -= 1
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()
            
            elif keys[pygame.K_DOWN] and self.selection_index[1] <= 1:
                self.selection_index[1] += 1
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()

            elif keys[pygame.K_UP] and self.selection_index[1] >= 1:
                self.selection_index[1] -= 1
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE]:
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()
                # self.triggered_effect(self.options_list[self.selection_index], player)
                print(f"Item selected at {self.selection_index}.")

    def getPlayerInfo(self):
        self.player_attributes = []
        self.player_stats = []
        self.player_resistances = []
        self.player_details = []
        
        self.player_attributes_names = []
        self.player_stats_names = []
        self.player_resistances_names = []
        self.player_details_names = []

        ## Stat Numbers ##
        # Attributes
        self.player_attributes.append(player_data['values']['level'])
        self.player_attributes.append(player_data['values']['souls'])
        for item in player_data['attributes'].values():
            self.player_attributes.append(item)
        self.player_attributes.append(player_data['values']['humanity'])

        # Stats
        for item in player_data['dependent_variables'].values():
            self.player_stats.append(item)
        for item in player_data['defense'].values():
            self.player_stats.append(item)
        self.player_stats.pop(4)
        self.player_stats.pop(8)
        self.player_stats.pop(8)
        
        # Extra Stats/Resistances
        for item in player_data['resistances'].values():
            self.player_resistances.append(item)

        ## Stat Names ##
        # Attributes
        self.player_attributes_names.append("Level")
        self.player_attributes_names.append("Souls")
        for item in player_data['attributes']:
            self.player_attributes_names.append(item)
        self.player_attributes_names.append("Humanity")

        # Stats
        for item in player_data['dependent_variables']:
            self.player_stats_names.append(item)
        for item in player_data['defense']:
            self.player_stats_names.append(item)
        self.player_stats_names.pop(4)
        self.player_stats_names.pop(8)
        self.player_stats_names.pop(8)
        
        # Extra Stats/Resistances
        for item in player_data['resistances']:
            self.player_resistances_names.append(item)

        # Other Information
        self.player_details.append(player_data['status']['name'])
        self.player_details.append(player_data['status']['covenant'])
        self.player_details_names.append("Name")
        self.player_details_names.append("Covenant")

    def displayStatus(self, player):
        self.getPlayerInfo()

        item_rect_size = (30, 30)
        x = (self.display_surface.get_size()[0] // 2) - (self.bg_image.get_size()[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (self.bg_image.get_size()[1] // 2)

        # Name + Covenant
        for option in self.player_details:
            index = self.player_details.index(option)
            rect = pygame.Rect(x + 700, y + 150 + (item_rect_size[1] + 5) * index, item_rect_size[0], item_rect_size[1])
            self.status_menu.display_names(self.display_surface, str(option), self.player_details_names, index, player, self.player_details_names[index], 200, rect)

        # Attributes
        for option in self.player_attributes:
            index = self.player_attributes.index(option)
            rect = pygame.Rect(x + 700, y + 220 + (item_rect_size[1] + 5) * index, item_rect_size[0], item_rect_size[1])
            self.status_menu.display(self.display_surface, index, str(option), self.player_attributes_names, self.player_attributes_surfs, player, 200, rect)
        
        # UI Elements
        self.display_surface.blit(self.corner_topleft, (x + 655, y + 105))
        self.display_surface.blit(self.corner_topright, (x + 915, y + 105))
        self.display_surface.blit(self.corner_bottomright, (x + 915, y + 500))
        self.display_surface.blit(self.corner_bottomleft, (x + 655, y + 500))
        self.display_surface.blit(self.connector_vertical_small, (x + 658, y + 140))
        self.display_surface.blit(self.connector_vertical_small, (x + 964, y + 140))
        self.display_surface.blit(self.connector_horizontal_small, (x + 715, y + 108))
        self.display_surface.blit(self.connector_horizontal_small, (x + 715, y + 552))

        self.display_surface.blit(self.separator_short, (x + 705, y + 182))
        self.display_surface.blit(self.separator_short, (x + 705, y + 217))
        self.display_surface.blit(self.separator_short, (x + 705, y + 287))
        self.display_surface.blit(self.separator_short, (x + 705, y + 462))

    def checkCategory(self):
        cat = "None"

        if self.selection_index[1] == 0:    # Top Row
            if self.selection_index[0] == 0 or self.selection_index[0] == 1: cat = "Right Hand"
            else: cat = "Left Hand"
        elif self.selection_index[1] == 1:    # Middle Row
            cat = "Quick Items"
        elif self.selection_index[1] == 2:    # Bottom Row
            if self.selection_index[0] == 0: cat = "Armour"
            else: cat = "Rings"
        
        return cat

    def loadImages(self): 
        x = (self.display_surface.get_size()[0] // 2) - (self.bg_image.get_size()[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (self.bg_image.get_size()[1] // 2)
        option_rect_size = (50, 50)
        item_rect_size = (80, 80)

        x_index = 0
        y_index = 0
        for i in self.equipment_categories:
            for j in i:
                for k in range(len(j)):
                    current_item = j[list(j)[k]]
                
                    if current_item["graphic"] == None:
                        current_item["graphic"] = "assets/graphics/inventory/items/None.png"

                    if x_index == 4:
                        y_index += 1
                        x_index = 0
                    full_index = [x_index, y_index]

                    # Separate categories
                    if full_index[1] == 0 and full_index[0] > 1: offset = 90
                    elif full_index[1] == 2 and full_index[0] > 0: offset = 90
                    else: offset = 0

                    dest = (x + 130 + (item_rect_size[1] + 10) * x_index + offset, y + 140 + (105 * y_index))
                    rect = pygame.Rect(dest[0], dest[1], item_rect_size[0], item_rect_size[1])
                    #print(f"{x_index}, {y_index}: {current_item['item']}")

                    # Loads image into memory
                    graphic = pygame.image.load(current_item["graphic"]).convert_alpha()

                    # Displays info for all items
                    self.current_category = self.checkCategory()
                    self.equip_menu.display(self.display_surface, self.selection_index, current_item["item"], graphic, rect, full_index, "item", self.current_category, dest)

                    x_index += 1
    
    def displayEquipment(self, player, updated):
        self.input(player)
        self.selection_cooldown()

        self.equipment_categories = [
            [],
            [],
            [],
        ]
        for i in [right_hand_data, left_hand_data]:
            self.equipment_categories[0].append(i)
        for i in [qitems_data]:
            self.equipment_categories[1].append(i)
        for i in [player_armour, ring_data]:
            self.equipment_categories[2].append(i)

        bg_rect_size = (1000, 600)

        x = (self.display_surface.get_size()[0] // 2) - (self.bg_image.get_size()[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (self.bg_image.get_size()[1] // 2)

        main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
        self.display_surface.blit(self.bg_image, main_rect)
        
        self.display_surface.blit(self.horizontal_bar_thin, (x + 110, y + 50))
        self.display_surface.blit(self.horizontal_bar_thin, (x + 110, y + 75))

        self.display_surface.blit(self.horizontal_bar, (x + 50, y + 120))
        self.display_surface.blit(self.horizontal_bar, (x + 50, y + 530))
        self.display_surface.blit(self.horizontal_bar_thin, (x + 50, y + 450))
        self.display_surface.blit(self.horizontal_bar_thin, (x + 50, y + 235))
        self.display_surface.blit(self.horizontal_bar_thin, (x + 50, y + 340))
        # self.display_surface.blit(self.horizontal_bar, (x + 50, y + 280))
        # self.display_surface.blit(self.horizontal_bar, (x + 50, y + 280 + (90 * 1)))
        # self.display_surface.blit(self.horizontal_bar, (x + 50, y + 280 + (90 * 2)))
        # self.display_surface.blit(self.horizontal_bar, (x + 50, y + 280 + (90 * 3)))
        
        # self.display_surface.blit(self.vertical_bar, (x + 130, y + 190))
        # self.display_surface.blit(self.vertical_bar_thin, (x + 50, y + 190))

        title_surface = self.title_font.render("Equipment", True, TEXT_COLOUR)
        title_rect = pygame.Rect(x + 110, y + 30, title_surface.get_size()[0], title_surface.get_size()[1])
        desc_surface = self.small_font.render("Select items to equip", True, TEXT_COLOUR)
        desc_rect = pygame.Rect(x + 110, y + 60, desc_surface.get_size()[0], desc_surface.get_size()[1])
        
        self.display_surface.blit(pygame.transform.scale(pygame.image.load("assets/graphics/ui/menu/menu_options_selected/equipment_open.png"), (60, 60)).convert_alpha(), (title_rect.x - 70, title_rect.y - 10)) 
        self.display_surface.blit(title_surface, title_rect)
        self.display_surface.blit(desc_surface, desc_rect)

        self.displayStatus(player)
        self.displayCategories()
        self.loadImages() # todo: make it so images are ONLY loaded once, not every frame

class itemEquip:
    def __init__(self, underlay):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.small_font = pygame.font.Font(UI_FONT, 13)
        #self.items_list_num = num_list
        self.underlay = underlay

    def display_names(self, surface, name):
        bg_rect_size = (1000, 600)
        x = (self.display_surface.get_size()[0] // 2) - (bg_rect_size[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2)
        colour = UPGRADE_TEXT_COLOUR

        if name == None: name = "Empty"

        if self.type == "item":
            cat_surface = self.small_font.render(self.category, True, colour)
            cat_rect = cat_surface.get_rect(midleft = (x, y) + pygame.math.Vector2(70, 440))

            title_surface = self.font.render(name, True, colour)
            title_rect = title_surface.get_rect(midleft = (x, y) + pygame.math.Vector2(70, 470))

            # num_surface = self.small_font.render(f"{self.items_list_num[player_inventory[self.category].index(name)]}", True, colour)
            # num_rect = num_surface.get_rect(bottomright = self.rect.bottomright + pygame.math.Vector2(-5, -5))

            # if self.category == "Consumables":
            #     surface.blit(num_surface, num_rect)

        surface.blit(title_surface, title_rect)
        surface.blit(cat_surface, cat_rect)

    def display(self, surface, selection_num, name, graphic, rect, index, type, item_category, destination):
        self.type = type
        self.category = item_category
        self.dest = destination

        if self.type == "item":

            if index == selection_num:
                pygame.draw.rect(surface, HOVER_COLOUR, rect)
                self.display_names(surface, name)
            
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR_ACTIVE, rect, 2)
            self.display_surface.blit(self.underlay, self.dest + pygame.math.Vector2(0, 10))
            self.display_surface.blit(graphic, self.dest)

# NPC Interaction