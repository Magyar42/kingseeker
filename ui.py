import pygame
from settings import *
from gameinfo import *

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

        # Convert Weapon Dictionary
        self.weapon_graphics = []
        for weapon in right_hand_data.values():
            path = weapon["graphic"]
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)
        
        # Convert Tool Dictionary
        self.tool_graphics = []
        for tool in left_hand_data.values():
            path = tool["graphic"]
            tool = pygame.image.load(path).convert_alpha()
            self.tool_graphics.append(tool)
        
        # Convert Magic Dictionary
        self.magic_graphics = []
        for magic in magic_data.values():
            path = magic["graphic"]
            magic = pygame.image.load(path).convert_alpha()
            self.magic_graphics.append(magic)
        
        # Convert Quick Items Dictionary
        self.qitems_graphics = []
        for item in qitems_data.values():
            path = item["graphic"]
            item = pygame.transform.scale(pygame.image.load(path), (64, 64)).convert_alpha()
            self.qitems_graphics.append(item)

        self.human_form_overlay = pygame.transform.scale(pygame.image.load("assets/graphics/ui/enkindled.png"), (110, 110)).convert_alpha()

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
        # humanity = int(humanity)
        if humanity < 10:
            humanity = "0" + str(humanity)

        text_surface = self.humanity_font.render(str(humanity), False, TEXT_COLOUR)
        text_rect = text_surface.get_rect(center = (self.humanity_counter_rect.centerx + 1, self.humanity_counter_rect.centery - 1))

        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, self.humanity_counter_rect.inflate(10, 10))
        self.display_surface.blit(text_surface, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, self.humanity_counter_rect.inflate(10, 10), 3)

        self.enkindled_ui_overlay(text_rect)

    def selection_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        # pygame.draw.rect(self.display_surface, UI_BG_COLOUR, bg_rect)
        if has_switched:
            itembox_surf = pygame.image.load(f"{self.box_path}/item_box_selected.png").convert_alpha()
            self.display_surface.blit(itembox_surf, bg_rect)
            # pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR_ACTIVE, bg_rect, 3)
        else:
            itembox_surf = pygame.image.load(f"{self.box_path}/item_box.png").convert_alpha()
            self.display_surface.blit(itembox_surf, bg_rect)
            # pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, bg_rect, 3)
        return bg_rect

    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(170, 565, has_switched)
        weapon_surface = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(weapon_surface, weapon_rect)
    
    def tool_overlay(self, tool_index, has_switched):
        bg_rect = self.selection_box(70, 565, has_switched)
        tool_surface = self.tool_graphics[tool_index]
        tool_rect = tool_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(tool_surface, tool_rect)
    
    def magic_overlay(self, magic_index, has_switched, player):
        bg_rect = self.selection_box(120, 520, has_switched)
        magic_surface = self.magic_graphics[magic_index]
        magic_rect = magic_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(magic_surface, magic_rect)
        if "catalyst" not in player.tool_type:
            self.display_surface.blit(pygame.image.load("assets/graphics/ui/inactive_overlay.png"), magic_rect)
    
    def item_overlay(self, item_index, has_switched, uses):
        bg_rect = self.selection_box(120, 610, has_switched)
        item_surface = self.qitems_graphics[item_index]
        item_rect = item_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(item_surface, item_rect)

        # amount_rect = pygame.Rect(120, 685, ITEM_BOX_SIZE, 25)
        # pygame.draw.rect(self.display_surface, UI_BG_COLOUR, amount_rect)
        # if has_switched:
        #     pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR_ACTIVE, amount_rect, 3)
        # else:
        #     pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, amount_rect, 3)
        # 
        text_surface = self.tooltip_font.render(str(uses), False, TEXT_COLOUR)
        text_rect = text_surface.get_rect(midright = item_rect.bottomright + pygame.math.Vector2(3, -5))
        self.display_surface.blit(text_surface, text_rect)
    
    # KINGSEEKER STUFF #
    def item_display(self, player, has_switched, uses):
        bg_rect = self.selection_box(170, 635, has_switched)
        item_surface = self.qitems_graphics[0]
        item_rect = item_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(item_surface, item_rect)
        text_surface = self.tooltip_font.render(str(uses), False, TEXT_COLOUR)
        text_rect = text_surface.get_rect(midright = item_rect.bottomright + pygame.math.Vector2(3, -5))
        self.display_surface.blit(text_surface, text_rect)

    def primary_attack_display(self, player, has_switched):
        bg_rect = self.selection_box(70, 545, has_switched)
        weapon_surface = self.weapon_graphics[0]
        weapon_rect = weapon_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(weapon_surface, weapon_rect)
    
    def secondary_attack_display(self, player, has_switched):
        bg_rect = self.selection_box(120, 590, has_switched)
        weapon_surface = self.weapon_graphics[0]
        weapon_rect = weapon_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(weapon_surface, weapon_rect)

    def tool_display(self, player, has_switched):
        bg_rect = self.selection_box(170, 545, has_switched)
        tool_surface = self.tool_graphics[1]
        tool_rect = tool_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(tool_surface, tool_rect)

    def skill_display(self, player, has_switched):
        bg_rect = self.selection_box(220, 590, has_switched)
        skill_surface = self.magic_graphics[1]
        skill_rect = skill_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(skill_surface, skill_rect)
    
    def show_boons(self, player):
        if player.menu_open:
            boon_surf = pygame.image.load(f"{self.box_path}/item_box.png").convert_alpha()
            for slot in range(7):
                # if slot % 2 == 1: y_add = 45
                # else: y_add = 0
                boon_rect = pygame.Rect(1180 - (slot * 35), 10, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
                self.display_surface.blit(boon_surf, boon_rect)
        
    def show_spells(self, player):
        spell_surf = pygame.transform.scale(pygame.image.load(f"{self.box_path}/item_box.png"), (60, 60)).convert_alpha()
        for slot in range(4):
            spell_rect = pygame.Rect(20, 200 + (slot * 65), ITEM_BOX_SIZE, ITEM_BOX_SIZE)
            self.display_surface.blit(spell_surf, spell_rect)

    def enkindled_ui_overlay(self, rect):
        if not player_data['status']['hollow']:
            outline_rect = pygame.Rect(self.humanity_counter_rect.x - 26, self.humanity_counter_rect.y - 26, self.humanity_counter_rect.w, self.humanity_counter_rect.h)

            self.display_surface.blit(self.human_form_overlay, outline_rect)
    
    def display(self, player):
        self.update_bars()

        self.show_bar(player, player.health_target, player_data['dependent_variables']["health"], self.health_bar_rect, HEALTH_COLOUR, self.health_bar_grad_rect, HEALTH_COLOUR_GRADIENT)
        self.show_bar(player, player.stamina_target, player_data['dependent_variables']["stamina"], self.stamina_bar_rect, STAMINA_COLOUR, self.stamina_bar_grad_rect, STAMINA_COLOUR_GRADIENT)
        self.show_bar(player, player.mana_target, player_data['dependent_variables']["mana"], self.mana_bar_rect, MANA_COLOUR, self.mana_bar_grad_rect, MANA_COLOUR_GRADIENT)

        self.show_boons(player) # todo
        self.show_spells(player)

        self.skill_display(player, not player.can_switch_magic)
        self.tool_display(player, not player.can_switch_tool)
        self.primary_attack_display(player, not player.can_switch_weapon)
        self.secondary_attack_display(player, not player.can_switch_weapon)
        self.item_display(player, not player.can_switch_qitems, player.qitems_uses[player.qitems_index])

        self.show_xp(player_data['values']['souls'])
        self.show_humanity(player_data['values']['humanity'])
        # self.weapon_overlay(player.weapon_index, not player.can_switch_weapon) # Main item display
        # self.tool_overlay(player.tool_index, not player.can_switch_tool) # Secondary item display
        # self.magic_overlay(player.magic_index, not player.can_switch_magic, player) # Spell display
        #self.item_overlay(player.qitems_index, not player.can_switch_qitems, player.qitems_uses[player.qitems_index]) # Quick Item Display