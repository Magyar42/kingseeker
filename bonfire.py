import pygame
from settings import *
from support import *
from popups import Prompt
from popups import Decision
from support import restore_estus
from gameinfo import *
from particles import AnimationPlayer

from debug import debug

class Bonfire(pygame.sprite.Sprite):
    def __init__(self, id, pos, groups, restart_world, check_humanity_restored, check_bonfire_lit, check_bonfire_rest, toggle_menu, toggle_screen_effect, kindle_bonfire_visuals):
        super().__init__(groups)
        self.font = pygame.font.Font(UI_FONT, MEDIUM_FONT_SIZE)
        self.display_surface = pygame.display.get_surface()
        self.frame_index = 0
        self.animation_speed = 0.10
        self.sprite_type = "bonfire"

        self.import_graphics("bonfire")
        self.id = id
        if bonfire_data[self.id]['active']:
            self.status = "idle"
        else:
            self.status = "unlit"
        self.image = self.animations[self.status][self.frame_index]

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-20, -30)

        self.use_radius = 100

        self.using_bonfire = False
        self.bonfire_cooldown = 400
        self.bonfire_use_time = None

        self.restart_world = restart_world
        self.check_bonfire_rest = check_bonfire_rest
        self.check_humanity_restored = check_humanity_restored
        self.check_bonfire_lit = check_bonfire_lit
        self.toggle_menu = toggle_menu
        self.toggle_screen_effect = toggle_screen_effect
        self.kindle_bonfire_visuals = kindle_bonfire_visuals

        self.prompt = Prompt()
        self.animation_player = AnimationPlayer()
        self.bonfireButtons = pygame.sprite.Group()
        self.popup = Decision(self.toggle_screen_effect, self.menu_humanity_effects,
                              self.menu_human_already_effects, self.menu_need_humanity_effects,
                              self.menu_kindle_effects, self.menu_requires_human_effects, self.menu_fully_kindled_effects)

        self.selection_index = 0
        self.selection_time = None
        self.can_move_selection = True

        self.current_menu_options = []
        for item in bonfire_menu_options.keys():
            if bonfire_menu_options[item]:
                self.current_menu_options.append(item)
        
        self.spending_humanity = False
        self.display_already_human = False
        self.need_humanity = False
        self.kindling_bonfire = False
        self.display_must_be_human = False
        self.display_max_kindled = False
    
    def import_graphics(self, name):
        self.animations = {
            "idle": [],
            "kindle": [],
            "warp": [],
            "unlit": [],
        }
        main_path = f"assets/graphics/interactable_entities/{name}/"
        for animation in self.animations.keys():
            full_path = main_path + animation
            self.animations[animation] = import_folder(full_path)
    
    def animate(self):
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index  >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
    
    def get_player_dist(self, player):
        bonfire_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(player.rect.center)

        distance = (player_vector - bonfire_vector).magnitude()

        return distance

    def player_interact(self, player):
        player_distance = self.get_player_dist(player)
        if player_distance <= self.use_radius:

            # Using an active bonfire
            if self.status == "idle":
                if not player.resting and not player.menu_open:
                    self.prompt.createPrompt("Checkpoint", "Q", "Rest at bonfire")

                if not self.using_bonfire:
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_q] and not player.resting:
                        self.rest_effects(player)

            # Lighting an inactive bonfire
            if self.status == "unlit":
                if not player.resting and not player.menu_open:
                    self.prompt.createPrompt("Checkpoint", "Q", "Light bonfire")
                
                if not self.using_bonfire:
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_q] and not player.resting:
                        self.light_bonfire_effects()

    def light_bonfire_effects(self):
        self.using_bonfire = True
        self.bonfire_use_time = pygame.time.get_ticks()

        self.status = "idle"
        bonfire_data[self.id]['active'] = True
        self.check_bonfire_lit()
    
    def rest_effects(self, player):
        self.using_bonfire = True
        self.bonfire_use_time = pygame.time.get_ticks()

        player.direction.x = 0
        player.direction.y = 0

        self.check_bonfire_rest()
        player.resting = True
        player.at_bonfire = True
        player.status = "down_idle"

        restore_estus(player, bonfire_data[self.id]['kindle_level'])
        player.health_increase = player_data['dependent_variables']["health"]
        player.stamina_target = player_data['dependent_variables']["stamina"]
        player.mana_target = player_data['dependent_variables']["mana"]
        # self.bonfire_menu(player)

    def input(self, player):
        keys = pygame.key.get_pressed()

        if self.can_move_selection:
            if keys[pygame.K_DOWN] and self.selection_index < len(self.current_menu_options) - 1:
                self.selection_index += 1
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_UP] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE]:
                self.can_move_selection = False
                self.selection_time = pygame.time.get_ticks()
                # print(f"Button {self.selection_index}: {self.current_menu_options[self.selection_index]}")
                self.trigger(player, self.current_menu_options[self.selection_index])
    
    def trigger(self, player, button):
        if button == "Leave":
            player.resting = False
            player.at_bonfire = False
        elif button == "Level Up":
            self.toggle_menu()
        elif button == "Attune Magic":
            print("TODO: Magic attunement")
        elif button == "Warp":
            print("TODO: Warping")
        elif button == "Kindle":
            self.kindling_bonfire = True
            self.toggle_screen_effect()
            self.status = "kindle"
        elif button == "Use Humanity":
            self.spending_humanity = True
            self.toggle_screen_effect()

    def kindle_effect(self, player):
        self.kindle_bonfire_visuals(self.rect.center)

        bonfire_data[self.id]["kindle_level"] += 1
        restore_estus(player, bonfire_data[self.id]['kindle_level'])

        self.status = "idle"
        self.toggle_screen_effect()
    
    def menu_kindle(self, player):
        if self.kindling_bonfire:
            self.popup.createDecision("Boolean", player, KINDLE_TEXT)

    def menu_kindle_effects(self, choice, player):
        if choice == "Yes":
            if player_data['status']['hollow'] == True:
                self.display_must_be_human = True
                self.kindling_bonfire = False
                self.status = "idle"
            elif bonfire_data[self.id]["kindle_level"] >= 4 or bonfire_data[self.id]["kindle_level"] >= 2 and not player_data["unlocks"]["rite_of_kindling"]:
                self.display_max_kindled = True
                self.kindling_bonfire = False
                self.status = "idle"
            elif player_data['values']['humanity'] > 0:
                self.kindle_effect(player)
                player_data['values']['humanity'] -= 1
                self.kindling_bonfire = False
            else:
                self.need_humanity = True
                self.kindling_bonfire = False
                self.status = "idle"
        elif choice == "No":
            self.kindling_bonfire = False
            self.toggle_screen_effect()
            self.status = "idle"
    
    def menu_requires_human(self, player):
        if self.display_must_be_human:
            self.popup.createDecision("Info", player, REQUIRES_HUMAN_TEXT)

    def menu_requires_human_effects(self):
        self.display_must_be_human = False
        self.toggle_screen_effect()

    def menu_fully_kindled(self, player):
        if self.display_max_kindled:
            self.popup.createDecision("Info", player, CANNOT_KINDLE)

    def menu_fully_kindled_effects(self):
        self.display_max_kindled = False
        self.toggle_screen_effect()

    def menu_humanity(self, player):
        if self.spending_humanity:
            # self.toggle_screen_effect()
            # self.popup.update()
            self.popup.createDecision("Boolean", player, RESTORE_HUMANITY_TEXT)

    def menu_humanity_effects(self, choice):
        if choice == "Yes":
            if player_data['status']['hollow'] == False:
                self.display_already_human = True
                self.spending_humanity = False
            elif player_data['values']['humanity'] > 0:
                player_data['status']['hollow'] = False
                player_data['values']['humanity'] -= 1
                self.check_humanity_restored()
                self.spending_humanity = False
                self.toggle_screen_effect()
            else:
                self.need_humanity = True
                self.spending_humanity = False
        elif choice == "No":
            self.spending_humanity = False
            self.toggle_screen_effect()

    def menu_human_already(self, player):
        if self.display_already_human:
            self.popup.createDecision("Info", player, ALREADY_HUMAN_TEXT)

    def menu_human_already_effects(self):
        self.display_already_human = False
        self.toggle_screen_effect()
    
    def menu_need_humanity(self, player):
        if self.need_humanity:
            self.popup.createDecision("Info", player, NEED_HUMANITY_TEXT)
    
    def menu_need_humanity_effects(self):
        self.need_humanity = False
        self.toggle_screen_effect()

    def selection_cooldown(self):
        if not self.can_move_selection:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 100:
                self.can_move_selection = True

    def bonfire_menu(self, player):
        if player.at_bonfire:
            self.input(player)
            self.selection_cooldown()

            bg_rect_size = (200, 300)
            item_rect_size = (200, 30)

            x = (self.display_surface.get_size()[0] // 2) - (bg_rect_size[1])
            y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2)

            menu_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
            pygame.draw.rect(self.display_surface, UI_BG_COLOUR, menu_rect.inflate(10, 10))
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, menu_rect.inflate(10, 10), 3)

            for option in self.current_menu_options:
                # item_rect = pygame.Rect(x, y + (item_rect_size[1]) * self.current_menu_options.index(item), item_rect_size[0], item_rect_size[1])
                # pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, item_rect.inflate(-10, -10))
                # item_surface = self.font.render(item, False, TEXT_COLOUR)
                # self.display_surface.blit(item_surface, item_rect)

                index = self.current_menu_options.index(option)
                item = Item(x, y + (item_rect_size[1] + 10) * self.current_menu_options.index(option), item_rect_size[0], item_rect_size[1], index, self.font, self.toggle_menu)
                item.display(self.display_surface, self.selection_index, option)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.using_bonfire:
            if current_time - self.bonfire_use_time >= self.bonfire_cooldown:
                self.using_bonfire = False
    
    def update(self):
        self.animate()
        self.cooldowns()
    
    def bonfire_update(self, player):
        self.player_interact(player)
        self.bonfire_menu(player)
    
    def bonfire_popup_update(self, player):
        if self.spending_humanity: self.menu_humanity(player)
        if self.display_already_human: self.menu_human_already(player)
        if self.need_humanity: self.menu_need_humanity(player)
        if self.kindling_bonfire: self.menu_kindle(player)
        if self.display_must_be_human: self.menu_requires_human(player)
        if self.display_max_kindled: self.menu_fully_kindled(player)

class Item:
    def __init__(self, left, top, width, height, index, font, toggle_menu):
        self.rect = pygame.Rect(left, top, width, height)
        self.index = index
        self.font = font

        self.toggle_menu = toggle_menu

    def display_names(self, surface, name):
        #colour = UPGRADE_TEXT_COLOUR_SELECTED if selected else UPGRADE_TEXT_COLOUR
        colour = UPGRADE_TEXT_COLOUR

        title_surface = self.font.render(name, False, colour)
        title_rect = title_surface.get_rect(midleft = self.rect.midleft + pygame.math.Vector2(10, 0))

        surface.blit(title_surface, title_rect)

    def display(self, surface, selection_num, name):
        if self.index == selection_num:
            pygame.draw.rect(surface, HOVER_COLOUR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOUR, self.rect, 4)
        else:
            pygame.draw.rect(surface, UI_BG_COLOUR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOUR, self.rect, 4)

        self.display_names(surface, name)