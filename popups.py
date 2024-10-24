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

        self.boon_index = 0
        self.boon_time = None
        self.can_move_boon = True

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

        self.boons = []
        for current_boon in interface_details["boons"]["list"]:
            current_boon_surf = pygame.image.load(f"assets/graphics/ui/interface_icons/boons/{current_boon}.png")
            self.boons.append(current_boon_surf)

    def selection_cooldown(self):
        if not self.can_move_selection:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 200:
                self.can_move_selection = True

        if not self.can_move_boon:
            current_time = pygame.time.get_ticks()
            if current_time - self.boon_time >= 200:
                self.can_move_boon = True
        
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
        
        if self.can_move_boon and self.showing_details:
            if keys[pygame.K_LEFT] and self.boon_index < len(interface_details["boons"]["list"]) - 1:
                self.boon_index += 1
                self.can_move_boon = False
                self.boon_time = pygame.time.get_ticks()
            elif keys[pygame.K_RIGHT] and self.boon_index >= 1:
                self.boon_index -= 1
                self.can_move_boon = False
                self.boon_time = pygame.time.get_ticks()

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
    
    # Esc Menu - Shows items + boons
    def displayMenu(self, player):
        colour = UPGRADE_TEXT_COLOUR
        self.input(player)
        self.selection_cooldown()

        # ITEMS Display
        bg_rect_size = (150, 215)
        option_rect_size = (25, 25)
        x = (self.display_surface.get_size()[0] - 170) # - (bg_rect_size[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2) + 300
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
            if index >= 4:
                rect = pygame.Rect(x + 90, y + (option_rect_size[1] + 5) * (self.resource_name_list.index(resource) - 4), option_rect_size[0], option_rect_size[1])
                self.menu.display(self.display_surface, self.selection_index, index, resource, rect, self.resource_num_list[index], self.showing_details)
            else:
                rect = pygame.Rect(x, y + (option_rect_size[1] + 5) * self.resource_name_list.index(resource), option_rect_size[0], option_rect_size[1])
                self.menu.display(self.display_surface, self.selection_index, index, resource, rect, self.resource_num_list[index], self.showing_details)

        # BOONS Display
        shown_boons = len(self.boons)
            
        for slot in range(shown_boons):
            if self.boon_index == slot: selected = True
            else: selected = False

            boon_rect = pygame.Rect(1170, 30 + (slot * 35), ITEM_BOX_SIZE, ITEM_BOX_SIZE)
            self.menu.boon_display(boon_rect, selected)

            boon_img = self.boons[slot]
            self.display_surface.blit(boon_img, boon_rect)

        # EXTRA lines
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

        # DETAILS toggle
        if self.showing_details:
            self.item_details(player, self.resource_name_list[self.selection_index], pygame.font.Font(UI_FONT, 18))
            self.boon_details(player, interface_details["boons"]["list"][self.boon_index], pygame.font.Font(UI_FONT, 18))
    
    # Shift Menu - Item details
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

    # Shift Menu - Boon details
    def boon_details(self, player, boon, font):
        # Background
        bg_rect_size = (600, 167)
        x = (self.display_surface.get_size()[0] - 790) # - (bg_rect_size[0] // 2)
        y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2) - 250
        main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, main_rect.inflate(10, 10))
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, main_rect.inflate(10, 10), 3)

        # Name
        title_surface = font.render(f"{boon_data[f"{boon}"]["name"]}", True, "white")
        title_rect = title_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(70, 15))
        text_fade = pygame.Surface((title_rect.w + 10, title_rect.h + 10)).convert_alpha()
        text_fade.fill(TEXT_BG_COLOUR)
        text_fade_rect = title_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(65, 10))
        self.display_surface.blit(text_fade, text_fade_rect)
        self.display_surface.blit(title_surface, title_rect)

        # Category
        cat = f"{boon_data[f"{boon}"]["category"]} | {boon_data[f"{boon}"]["lvl"]}"
        cat_surface = pygame.font.Font(UI_FONT, 10).render(cat, True, "white")
        cat_rect = cat_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(70, 40))
        cat_fade = pygame.Surface((cat_rect.w + 10, cat_rect.h + 10)).convert_alpha()
        cat_fade.fill(TEXT_BG_COLOUR)
        cat_fade_rect = cat_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(65, 35))
        self.display_surface.blit(cat_fade, cat_fade_rect)
        self.display_surface.blit(cat_surface, cat_rect)

        # Desc 1
        desc1 = boon_data[f"{boon}"]["desc1"]
        split_current_line = desc1.split("|")
        while len(split_current_line) < 4:
            split_current_line.append("")
        for subline in range(4):
            text_surf = pygame.font.Font(UI_FONT, 12).render(split_current_line[subline], False, "white")
            text_rect = text_surf.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(5, 75 + (subline * 15)))
            self.display_surface.blit(text_surf, text_rect)

        # Desc 2
        desc2 = boon_data[f"{boon}"]["desc2"]
        split_current_line = desc2.split("|")
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
            pygame.draw.rect(surface, "#FF8208", rect, 3)
        else:
            pygame.draw.rect(surface, UI_BORDER_COLOUR, rect, 3)
        self.display_surface.blit(self.resource_icon_list[index], rect)
        self.display_names(surface, name, rect, num)

    def boon_display(self, rect, selected):
        if selected: itembox_surf = pygame.image.load("assets/graphics/ui/interface/item_box_selected.png").convert_alpha()
        else: itembox_surf = pygame.image.load("assets/graphics/ui/interface/item_box.png").convert_alpha()
        self.display_surface.blit(itembox_surf, rect)