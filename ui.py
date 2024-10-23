import pygame
from settings import *
from gameinfo import *
from support import centreImage, centreImageNum

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.humanity_font = pygame.font.Font(UI_FONT, 26)
        self.tooltip_font = pygame.font.Font(UI_FONT, SMALL_FONT_SIZE)

        self.box_path = "assets/graphics/ui/interface"
        self.transition_speed = 5

        # Bars Setup
        self.health_bar_rect = pygame.Rect(90, 10, ui_data['HEALTH_BAR_WIDTH'], BAR_HEIGHT)
        self.mana_bar_rect = pygame.Rect(90, 34, ui_data['MANA_BAR_WIDTH'], BAR_HEIGHT)
        self.stamina_bar_rect = pygame.Rect(90, 58, ui_data['STAMINA_BAR_WIDTH'], BAR_HEIGHT)

        self.health_bar_grad_rect = pygame.Rect(90, 10, ui_data['HEALTH_BAR_WIDTH'], BAR_HEIGHT // 2)
        self.mana_bar_grad_rect = pygame.Rect(90, 34, ui_data['MANA_BAR_WIDTH'], BAR_HEIGHT // 2)
        self.stamina_bar_grad_rect = pygame.Rect(90, 58, ui_data['STAMINA_BAR_WIDTH'], BAR_HEIGHT // 2)

        # Extras
        self.humanity_counter_rect = pygame.Rect(20, 15, HUMANITY_BOX_WIDTH, HUMANITY_BOX_HEIGHT)

        self.human_form_overlay = pygame.transform.scale(pygame.image.load("assets/graphics/ui/enkindled.png"), (110, 110)).convert_alpha()

        # KINGSEEKER
        # TODO: move to somewhere else so that it updates after each loading from firelink, as well as after each boon gained
        self.estus_surf = pygame.image.load("assets/graphics/ui/interface_icons/inputs/estus.png")
        self.input_types = []
        for input_type in ["light_attack", "heavy_attack", "skill", "catalyst"]:
            current_tool = interface_details[f"{input_type}"]["name"]
            current_tool_surf = pygame.image.load(f"assets/graphics/ui/interface_icons/inputs/{current_tool}.png")
            self.input_types.append(current_tool_surf)
            # f"self.{input_type}_img" = pygame.image.load(f"assets/graphics/ui/interface_icons/inputs/{current_tool}.png")
        
        self.spells = []
        for spell_num in range(1, 4):
            current_spell = interface_details["spells"][spell_num]
            current_spell_surf = pygame.image.load(f"assets/graphics/ui/interface_icons/spells/{current_spell}.png")
            self.spells.append(current_spell_surf)

        self.boons = []
        for boon_num in range(1, 8):
            current_boon = interface_details["boons"][boon_num]
            current_boon_surf = pygame.image.load(f"assets/graphics/ui/interface_icons/boons/{current_boon}.png")
            self.boons.append(current_boon_surf)

        self.overlay_img = pygame.image.load(f"assets/graphics/ui/interface/item_box_overlay.png")
        self.spell_underlay = pygame.image.load(f"assets/graphics/ui/interface/spell_underlay.png")
        self.input_underlay = pygame.image.load(f"assets/graphics/ui/interface/input_underlay.png")
        self.estus_counter = pygame.image.load(f"assets/graphics/ui/interface/counter_box.png")

    def update_bars(self):
        self.health_bar_rect = pygame.Rect(90, 10, ui_data['HEALTH_BAR_WIDTH'], BAR_HEIGHT)
        self.mana_bar_rect = pygame.Rect(90, 34, ui_data['MANA_BAR_WIDTH'], BAR_HEIGHT)
        self.stamina_bar_rect = pygame.Rect(90, 58, ui_data['STAMINA_BAR_WIDTH'], BAR_HEIGHT)

        self.health_bar_grad_rect = pygame.Rect(90, 10, ui_data['HEALTH_BAR_WIDTH'], BAR_HEIGHT // 2)
        self.mana_bar_grad_rect = pygame.Rect(90, 34, ui_data['MANA_BAR_WIDTH'], BAR_HEIGHT // 2)
        self.stamina_bar_grad_rect = pygame.Rect(90, 58, ui_data['STAMINA_BAR_WIDTH'], BAR_HEIGHT // 2)

    def show_bar(self, player, current, max, bg_rect, colour, grad, grad_colour):
        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, bg_rect)
        transition_colour = "#fca503"
        self.transition_width_h = player.transition_width_h
        self.transition_width_s = player.transition_width_s
        self.transition_width_m = player.transition_width_m

        ratio = current / max
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        if current == player.health_target:
            transition_rect = pygame.Rect(current_rect.right, 10, self.transition_width_h, BAR_HEIGHT)
            pygame.draw.rect(self.display_surface, transition_colour, transition_rect)
        elif current == player.stamina_target:
            transition_rect = pygame.Rect(current_rect.right, 58, self.transition_width_s, BAR_HEIGHT)
            pygame.draw.rect(self.display_surface, transition_colour, transition_rect)
        elif current == player.mana_target:
            transition_rect = pygame.Rect(current_rect.right, 34, self.transition_width_m, BAR_HEIGHT)
            pygame.draw.rect(self.display_surface, transition_colour, transition_rect)
        
        pygame.draw.rect(self.display_surface, colour, current_rect)

        if grad != None:
            grad_rect = grad
            grad_rect.width = current_width
            pygame.draw.rect(self.display_surface, grad_colour, grad_rect)

        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, bg_rect, 3)

    def show_xp(self, xp):
        x = self.display_surface.get_size()[0] - 35
        y = self.display_surface.get_size()[1] - 20

        text_surface = self.font.render(str(int(xp)), False, TEXT_COLOUR)
        text_rect = text_surface.get_rect(bottomright = (x, y))

        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, text_rect.inflate(20, 20))
        self.display_surface.blit(text_surface, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, text_rect.inflate(20, 20), 3)
    
    def show_humanity(self, humanity):
        if humanity < 10:
            humanity = "0" + str(humanity)

        text_surface = self.humanity_font.render(str(humanity), False, TEXT_COLOUR)
        text_rect = text_surface.get_rect(center = (self.humanity_counter_rect.centerx + 1, self.humanity_counter_rect.centery - 1))

        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, self.humanity_counter_rect.inflate(10, 10))
        self.display_surface.blit(text_surface, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, self.humanity_counter_rect.inflate(10, 10), 3)

        self.enkindled_ui_overlay(text_rect)
    
    # KINGSEEKER STUFF #
    def selection_box(self, left, top, triggered):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)

        if triggered: itembox_surf = pygame.image.load(f"{self.box_path}/item_box_selected.png").convert_alpha()
        else: itembox_surf = pygame.image.load(f"{self.box_path}/item_box.png").convert_alpha()
        self.display_surface.blit(itembox_surf, bg_rect)
        
        return bg_rect
    
    def selection_box_small(self, left, top, triggered):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE_SMALL, ITEM_BOX_SIZE_SMALL)

        if triggered: itembox_surf = pygame.image.load(f"{self.box_path}/spell_box_selected.png").convert_alpha()
        else: itembox_surf = pygame.image.load(f"{self.box_path}/spell_box.png").convert_alpha()
        self.display_surface.blit(itembox_surf, bg_rect)
        
        return bg_rect
    
    def box_cooldown(self, rect, active):
        if active:
            self.display_surface.blit(self.overlay_img, rect)

    def spell_box(self, rect, selected):
        # bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)

        if selected: itembox_surf = pygame.image.load(f"{self.box_path}/spell_box_selected.png").convert_alpha()
        else: itembox_surf = pygame.image.load(f"{self.box_path}/spell_box.png").convert_alpha()
        self.display_surface.blit(itembox_surf, rect)
    
    def estus_display(self, player, triggered, uses):

        # Main box
        bg_rect = self.selection_box_small(30, 590 + 20, triggered)
        item_surface = self.estus_surf
        item_rect = item_surface.get_rect(center = bg_rect.center)
        self.display_surface.blit(item_surface, item_rect)

        # Counter
        bg_rect = pygame.Rect(item_rect.bottomright[0] - 10, item_rect.bottomright[1] - 10, 30, 30)
        text_surface = self.tooltip_font.render(str(uses), False, TEXT_COLOUR)
        num_rect = text_surface.get_rect(center = bg_rect.center)
        self.display_surface.blit(self.estus_counter, bg_rect)
        self.display_surface.blit(text_surface, num_rect)

    def primary_attack_display(self, player, triggered):
        bg_rect = self.selection_box(70, 545, triggered)
        light_attack_surface = self.input_types[0]
        light_attack_rect = light_attack_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(light_attack_surface, light_attack_rect)
        self.box_cooldown(light_attack_rect, triggered)
    
    def secondary_attack_display(self, player, triggered):
        bg_rect = self.selection_box(115, 590, triggered)
        heavy_attack_surface = self.input_types[1]
        heavy_attack_rect = heavy_attack_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(heavy_attack_surface, heavy_attack_rect)
        self.box_cooldown(heavy_attack_rect, triggered)

    def catalyst_display(self, player, triggered):
        bg_rect = self.selection_box(175, 545, triggered)
        catalyst_surface = self.input_types[3]
        catalyst_rect = catalyst_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(catalyst_surface, catalyst_rect)
        self.box_cooldown(catalyst_rect, triggered)

    def skill_display(self, player, triggered):
        bg_rect = self.selection_box(220, 590, triggered)
        skill_surface = self.input_types[2]
        skill_rect = skill_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(skill_surface, skill_rect)
        self.box_cooldown(skill_rect, triggered)
    
    def show_boons(self, player):
        if player.menu_open:
            boon_surf = pygame.image.load(f"{self.box_path}/item_box.png").convert_alpha()
            for slot in range(7):
                # if slot % 2 == 1: y_add = 45
                # else: y_add = 0
                boon_rect = pygame.Rect(1180 - (slot * 35), 10, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
                self.display_surface.blit(boon_surf, boon_rect)

                boon_img = self.boons[slot]
                self.display_surface.blit(boon_img, boon_rect)
        
    def show_spells(self, player, index):
        # spell_surf = pygame.transform.scale(pygame.image.load(f"{self.box_path}/spell_box.png"), (60, 60)).convert_alpha()
        base_y = centreImageNum(60, 60)[1] - 65
        x = 10 + self.spell_underlay.get_width() // 2 - 30
        for slot in range(3):
            if index == slot: selected = True
            else: selected = False

            spell_rect = pygame.Rect(x, base_y + (slot * 65), ITEM_BOX_SIZE, ITEM_BOX_SIZE)
            self.spell_box(spell_rect, selected)

            spell_img = self.spells[slot]
            self.display_surface.blit(spell_img, spell_rect)

    def enkindled_ui_overlay(self, rect):
        if not interface_details['values']['hollow']:
            outline_rect = pygame.Rect(self.humanity_counter_rect.x - 26, self.humanity_counter_rect.y - 26, self.humanity_counter_rect.w, self.humanity_counter_rect.h)

            self.display_surface.blit(self.human_form_overlay, outline_rect)
    
    def show_underlays(self):
        # Spells
        y = centreImage(self.spell_underlay)[1]
        self.display_surface.blit(self.spell_underlay, (10, y))

        # Inputs
        self.display_surface.blit(self.input_underlay, (60, 535))
        self.display_surface.blit(self.input_underlay, (165, 535))
    
    def display(self, player):
        self.update_bars()
        self.show_underlays()

        self.show_bar(player, player.health_target, player_data['dependent_variables']["health"], self.health_bar_rect, HEALTH_COLOUR, self.health_bar_grad_rect, HEALTH_COLOUR_GRADIENT)
        self.show_bar(player, player.stamina_target, player_data['dependent_variables']["stamina"], self.stamina_bar_rect, STAMINA_COLOUR, self.stamina_bar_grad_rect, STAMINA_COLOUR_GRADIENT)
        self.show_bar(player, player.mana_target, player_data['dependent_variables']["mana"], self.mana_bar_rect, MANA_COLOUR, self.mana_bar_grad_rect, MANA_COLOUR_GRADIENT)

        self.show_boons(player) # todo
        self.show_spells(player, player.spell_index)

        # todo for all inputs: have timer for use time AND cooldown after separate
        # here, the box outline should go orange for the use time, not the cooldown
        self.skill_display(player, player.using_skill)
        self.catalyst_display(player, player.casting_spell)
        self.primary_attack_display(player, player.light_attacking)
        self.secondary_attack_display(player, player.heavy_attacking)
        self.estus_display(player, player.drinking_estus, interface_details["values"]["current estus"])

        self.show_xp(interface_details['values']['souls'])
        self.show_humanity(interface_details['values']['active humanities'])