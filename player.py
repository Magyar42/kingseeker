import pygame
from settings import *
from support import *
from entity import Entity
from gameinfo import *
from random import randint
from debug import debug
from particles import AnimationPlayer
from popups import *

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, attackable_sprites, create_attack, destroy_attack, create_tool, destroy_tool, create_magic, trigger_death_particles, check_player_death, use_item_effect, toggle_screen_effect):
        super().__init__(groups)
        self.animation_speed = 0.15

        self.toggle_screen_effect = toggle_screen_effect
        self.animation_player = AnimationPlayer()

        self.popup = gameMenu(self.toggle_screen_effect)
        self.inv = invMenu(self.toggle_screen_effect)
        self.stat = statusMenu(self.toggle_screen_effect)
        #self.system = systemMenu(self.toggle_screen_effect)
        self.equip = equipMenu(self.toggle_screen_effect)

        self.prompt_active = False

        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("assets/graphics/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-6, HITBOX_OFFSET["player"])
        self.sprite_type = "player_sprite"

        self.import_player_assets()
        self.status = "down"

        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.using_tool = False
        self.tool_cooldown = 400
        self.tool_time = None

        self.obstacle_sprites = obstacle_sprites
        self.attackable_sprites = attackable_sprites

        # weapon
        getSlotData(right_hand_data, weapon_data)
        getSlotData(left_hand_data, tool_data)

        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.create_tool = create_tool
        self.destroy_tool = destroy_tool

        self.weapon_index = 0
        self.weapon = list(right_hand_data.values())[self.weapon_index]["item"]
        self.weapon_slot = list(right_hand_data.keys())[self.weapon_index]
        self.weapon_weight = list(right_hand_data.values())[self.weapon_index]["weight"]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.weapon_switch_cooldown = 200

        # tool
        self.tool_index = 0
        self.tool = list(left_hand_data.values())[self.tool_index]["item"]
        self.tool_slot = list(left_hand_data.keys())[self.tool_index]
        self.tool_weight = list(left_hand_data.values())[self.tool_index]["weight"]
        self.tool_type = list(left_hand_data.values())[self.tool_index]["type"]
        self.can_switch_tool = True
        self.tool_switch_time = None
        self.tool_switch_cooldown = 200

        # magic
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.magic_weight = list(magic_data.values())[self.magic_index]["weight"]
        self.can_switch_magic = True
        self.magic_switch_time = None

        # quick items
        self.qitems_index = 0
        self.qitems = []
        self.qitems_uses = []
        for i in ["slot1", "slot2", "slot3", "slot4"]:
            if qitems_data[i]['item'] != None:
                self.qitems.append(qitems_data[i]['item'])
                self.qitems_uses.append(qitems_data[i]['amount'])
        
        self.can_switch_qitems = True
        self.qitems_switch_cooldown = 200
        self.qitems_switch_time = None

        # stats
        self.stamina_light_attack_mult = 3
        self.stamina_heavy_attack_mult = 5
        self.stamina_tool_mult = 5
        self.stamina_magic_mult = 4

        self.health = player_data['dependent_variables']['health']
        self.health_target = player_data['dependent_variables']['health']
        self.health_increase = player_data['dependent_variables']['health']
        self.poise = player_data['dependent_variables']['poise']
        self.max_poise = player_data['dependent_variables']['poise']

        self.stamina = player_data['dependent_variables']['stamina']
        self.stamina_target = player_data['dependent_variables']['stamina']
        
        self.mana = player_data['dependent_variables']['mana']
        self.mana_target = player_data['dependent_variables']['mana']

        self.transition_width_h = 0
        self.transition_width_s = 0
        self.transition_width_m = 0

        self.speed = player_data['dependent_variables']['speed']
        self.xp = player_data['values']['souls']
        self.stamina_recovery_speed = player_data['dependent_variables']['stamina recovery']
        self.mana_recovery_speed = player_data['dependent_variables']['mana recovery']
        self.stamina_roll = 15

        # attributes
        self.attributes = {
            "VITALITY": 11,
            "ATTUNEMENT": 8,
            "ENDURANCE": 12,
            "STRENGTH": 13,
            "PERCEPTION": 9,
        }
        self.level = 4
        self.humanity = player_data['values']['humanity']

        self.max_attributes = {
            "VITALITY": 99,
            "ATTUNEMENT": 99,
            "ENDURANCE": 99,
            "STRENGTH": 99,
            "PERCEPTION": 99,
        }
        self.max_level = 495
        self.max_humanity = 99

        self.upgrade_equation = get_upgrade_cost(self.level)
        player_data['values']['levelup_cost'] = round(self.upgrade_equation)

        # damage timer
        self.vulnerable = True
        self.hurt_time = None
        self.invincibility_duration = 500

        # bonfire / npc
        self.resting = False
        self.at_bonfire = False
        self.npc_chatting = False
        self.engaged_npc = None

        # sound
        self.weapon_attack_sound = pygame.mixer.Sound("assets/audio/sfx/sword.wav")
        self.weapon_attack_sound.set_volume(0.1)
        self.death_sound = pygame.mixer.Sound("assets/audio/sfx/death.wav")
        self.death_sound.set_volume(0.1)
        self.qitems_use_sound = pygame.mixer.Sound("assets/audio/sfx/estus_flask.wav")
        self.qitems_use_sound.set_volume(0.3)
        self.humanity_use_sound = pygame.mixer.Sound("assets/audio/sfx/humanity_used.wav")
        self.humanity_use_sound.set_volume(0.1)

        # death
        self.trigger_death_particles = trigger_death_particles
        self.check_player_death = check_player_death
        self.dead = False
        self.lost_xp = 0
        self.lost_humanity = 0

        #self.resetPlayer()

        # rolling
        self.rolling = False
        self.roll_cooldown = 500
        self.roll_duration = None
        # self.rolling_time = 500

        # item use
        self.using_item = False
        self.item_cooldown = 500
        self.item_use_time = None
        self.use_item_effect = use_item_effect
        
        self.menu_open = False
        self.menu_inventory = False
        self.menu_status = False
        self.menu_system = False
        self.menu_equipment = False
        self.submenu_open = False

        self.can_toggle_menu = True
        self.menu_toggle_time = None
        self.menu_toggle_cooldown = 200
        self.reset_display = False

        self.stunned = False
        self.poise_broken = False
        self.broken_poise_time = None
        self.broken_poise_effect_time = 400

        self.knocked_back = False
        self.knocked_back_time = None
        self.knocked_back_length = 200

        # kingseeker
        self.ongoing_run = False
    
    def resetPlayer(self):
        self.health = player_data['dependent_variables']['health']
        self.health_target = player_data['dependent_variables']['health']
        self.health_increase = player_data['dependent_variables']['health']
        self.poise = player_data['dependent_variables']['poise']
        self.max_poise = player_data['dependent_variables']['poise']

        self.stamina = player_data['dependent_variables']['stamina']
        self.stamina_target = player_data['dependent_variables']['stamina']
        
        self.mana = player_data['dependent_variables']['mana']
        self.mana_target = player_data['dependent_variables']['mana']
    
    def import_player_assets(self):
        character_path = "assets/graphics/player/"
        self.animations = {
            "up": [],
            "down": [],
            "left": [],
            "right": [],
            "up_idle": [],
            "down_idle": [],
            "left_idle": [],
            "right_idle": [],
            "up_attack": [],
            "down_attack": [],
            "left_attack": [],
            "right_attack": [],
            "up_roll": [],
            "down_roll": [],
            "left_roll": [],
            "right_roll": [],
            "dead": [],
            "item": [],
            "stunned": [],
            # Unused
            "special1": [],
            "special2": [],
        }
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
    
    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not "idle" in self.status and not "attack" in self.status and not "roll" in self.status and not "dead" in self.status and not "item" in self.status and not "stunned" in self.status:
                self.status = self.status + "_idle"
        
        if self.attacking or self.using_tool:
            self.direction.x = 0
            self.direction.y = 0
            if not "attack" in self.status:
                if "idle" in self.status:
                    self.status = self.status.replace("_idle", "_attack")
                elif "dead" in self.status or "stunned" in self.status:
                    pass
                else:
                    self.status = self.status + "_attack"
        elif self.rolling:
            if not "roll" in self.status:
                if "idle" in self.status:
                    self.status = self.status.replace("_idle", "_roll")
                elif "dead" in self.status or "stunned" in self.status:
                    pass
                else:
                    self.frame_index = 0
                    self.status = self.status + "_roll"
        elif self.using_item:
            self.status = "item"
            self.resting = True
            self.direction.x = 0
            self.direction.y = 0

            current_item_image = pygame.transform.scale(pygame.image.load(list(qitems_data.values())[self.qitems_index]["graphic"]), (40, 40)).convert_alpha()
            x = (self.display_surface.get_size()[0] // 2) - (current_item_image.get_size()[0] // 2)
            y = (self.display_surface.get_size()[1] // 2) - (current_item_image.get_size()[1] // 2) - 40
            self.display_surface.blit(current_item_image, (x, y))

        else:
            if "attack" in self.status:
                self.status = self.status.replace("_attack", "")
            elif "roll" in self.status:
                self.status = self.status.replace("_roll", "")
    
    def reset_qitems_display(self):
        for qitem in qitems_data.keys():
            item_name = qitems_data[qitem]["item"]
            if item_name != None:
                item_cat = game_items[item_name]["category"]

                index_in_inventory = player_inventory[item_cat].index(item_name)
                num_in_inventory = player_inventory[f"{item_cat}_num"][index_in_inventory]

                qitems_data[qitem]["amount"] = num_in_inventory
        
        # Current display - update this to show changes in the CURRENT quick item
        # So, find the current item name and display the relevant amount value
        current_qitem = self.qitems[self.qitems_index]
        current_cat = game_items[current_qitem]["category"]
        item_index = player_inventory[current_cat].index(current_qitem)
        new_value = player_inventory[f"{current_cat}_num"][item_index]

        self.qitems_uses[self.qitems_index] = new_value

    def main_menu(self):
        if self.menu_open:
            self.popup.displayMenu(self)
    
    def inventory_display(self):
        if self.menu_inventory:
            self.inv.displayInventory(self)
        if self.reset_display:
            self.inv.resetDisplay()
            self.reset_display = False
    
    def status_display(self):
        if self.menu_status:
            self.stat.displayStatus(self)
    
    def system_display(self):
        if self.menu_system:
            #self.system.displaySystem(self)
            debug("TODO: System")
    
    def equipment_display(self):
        if self.menu_equipment:
            self.equip.displayEquipment(self, False)

    def input(self):
        keys = pygame.key.get_pressed()

        # if self.can_toggle_menu and not self.submenu_open:
        #     if keys[pygame.K_ESCAPE] and not self.menu_open:
        #         self.menu_open = True
        #         self.can_toggle_menu = False
        #         self.menu_toggle_time = pygame.time.get_ticks()
        #         #self.resting = True
        #     elif keys[pygame.K_ESCAPE] and self.menu_open:
        #         self.menu_open = False
        #         self.can_toggle_menu = False
        #         self.menu_toggle_time = pygame.time.get_ticks()
        #         self.resting = False
        
        # if self.submenu_open:
        #     if keys[pygame.K_ESCAPE]:
        #         self.menu_inventory = False
        #         self.menu_status = False
        #         self.menu_system = False
        #         self.menu_equipment = False
        #         self.submenu_open = False

        if not self.attacking and not self.using_tool and not self.resting and not self.rolling and not self.stunned:
            if not self.dead:
                # quick item input
                if keys[pygame.K_f] and not self.using_item:       # Todo: change to not use index, but name, so that any item can be assigned to quick use 
                    
                    if self.qitems_uses[self.qitems_index] > 0:
                        self.using_item = True
                        self.item_use_time = pygame.time.get_ticks()

                        self.use_item_effect(self.qitems_index)

                        if self.qitems_index == 0:
                            player_data['status']['current_estus'] -= 1     # Reduces amount in player data
                            player_inventory["Consumables_num"][player_inventory["Consumables"].index(self.qitems[self.qitems_index])] = player_data['status']['current_estus'] # Update inventory
                            qitems_data[f'slot{self.qitems_index + 1}']['amount'] = player_inventory["Consumables_num"][player_inventory["Consumables"].index(self.qitems[self.qitems_index])] # Update quick items
                            self.qitems_uses[self.qitems_index] = qitems_data[f'slot{self.qitems_index + 1}']['amount']  # Update display

                            self.health_increase += 300 # todo: include estus level in amount of hp recovered AND update HP numbers
                            if self.health_increase >= player_data['dependent_variables']['health']:
                                self.health_increase = player_data['dependent_variables']['health']

                            self.qitems_use_sound.play()

                        elif self.qitems_index == 1:
                            player_inventory["Consumables_num"][player_inventory["Consumables"].index(self.qitems[self.qitems_index])] -= 1 # Update inventory
                            qitems_data[f'slot{self.qitems_index + 1}']['amount'] = player_inventory["Consumables_num"][player_inventory["Consumables"].index(self.qitems[self.qitems_index])]
                            self.qitems_uses[self.qitems_index] = qitems_data[f'slot{self.qitems_index + 1}']['amount']

                            self.health_increase = player_data['dependent_variables']['health']
                            player_data['values']['humanity'] += 1

                            self.humanity_use_sound.play()

                # movement input
                if keys[pygame.K_w]:
                    self.direction.y = -1
                    self.status = "up"
                elif keys[pygame.K_s]:
                    self.direction.y = 1
                    self.status = "down"
                else:
                    self.direction.y = 0

                if keys[pygame.K_a]:
                    self.direction.x = -1
                    self.status = "left"
                elif keys[pygame.K_d]:
                    self.direction.x = 1
                    self.status = "right"
                else:
                    self.direction.x = 0
                
                # roll input
                if keys[pygame.K_e] and not self.rolling:
                    if self.stamina_target - (self.stamina_roll) >= 0:
                        self.frame_index = 0
                        if self.status == "up_idle": self.direction.y = -1
                        if self.status == "down_idle": self.direction.y = 1
                        if self.status == "left_idle": self.direction.x = -1
                        if self.status == "right_idle": self.direction.x = 1

                        self.stamina_target -= (self.stamina_roll) # Effect on stamina
                        self.rolling = True
                        self.roll_duration = pygame.time.get_ticks()
                        self.move(50, self.sprite_type)
                        #self.speed /= 2

                # attack input - light
                if player_inputs["light attack"]:
                    if self.stamina_target - (self.stamina_light_attack_mult * self.weapon_weight) >= 0:
                        self.stamina_target -= (self.stamina_light_attack_mult * self.weapon_weight) # Effect on stamina

                        self.attacking = True
                        self.attack_time = pygame.time.get_ticks()
                        self.create_attack()
                        self.weapon_attack_sound.play()
                        player_inputs["light attack"] = False

                # attack input - heavy
                if player_inputs["heavy attack"]:
                    if self.stamina_target - (self.stamina_heavy_attack_mult * self.weapon_weight) >= 0:
                        self.stamina_target -= (self.stamina_heavy_attack_mult * self.weapon_weight) # Effect on stamina

                        self.attacking = True
                        self.attack_time = pygame.time.get_ticks()
                        self.create_attack()
                        self.weapon_attack_sound.play()
                        player_inputs["heavy attack"] = False

                # todo: skill effect
                
                # tool input
                # if keys[pygame.K_LCTRL]:
                #     if self.stamina_target - (self.stamina_tool_mult * self.tool_weight) >= 0:
                #         self.stamina_target -= (self.stamina_tool_mult * self.tool_weight) # Effect on stamina

                #         self.using_tool = True
                #         self.tool_time = pygame.time.get_ticks()
                #         self.create_tool()
                #         self.weapon_attack_sound.play()

                #         print(self.tool_type)
                #         # Effects
                #         if "catalyst" in self.tool_type:
                #             if self.stamina_target - (self.stamina_magic_mult * self.magic_weight) >= 0:
                #                 self.stamina_target -= (self.stamina_magic_mult * self.magic_weight)
                                                
                #                 self.attacking = True
                #                 self.attack_time = pygame.time.get_ticks()
                #                 style = list(magic_data.keys())[self.magic_index]
                #                 strength = list(magic_data.values())[self.magic_index]["strength"] + player_data['dependent_variables']['magic damage'] + list(left_hand_data.values())[self.tool_index]["damage"]
                #                 cost = list(magic_data.values())[self.magic_index]["cost"]
                #                 self.create_magic(style, strength, cost)

                # Below removed for KINGSEEKER, as items and weapons cannot be switched
                # during a run anyway, and the UI isn't seen at Firelink
                
                # # weapon switch
                # if keys[pygame.K_RIGHT] and self.can_switch_weapon:
                #     self.can_switch_weapon = False
                #     self.weapon_switch_time = pygame.time.get_ticks()

                #     if self.weapon_index < len(list(right_hand_data.keys())) - 1:
                #         self.weapon_index += 1
                #     else:
                #         self.weapon_index = 0
                #     # self.weapon = list(weapon_data.keys())[self.weapon_index]
                #     # self.weapon_weight = list(weapon_data.values())[self.weapon_index]["weight"]
                #     self.weapon = list(right_hand_data.values())[self.weapon_index]["item"]
                #     self.weapon_weight = list(right_hand_data.values())[self.weapon_index]["weight"]
                
                # # tool switch
                # if keys[pygame.K_LEFT] and self.can_switch_tool:
                #     self.can_switch_tool = False
                #     self.tool_switch_time = pygame.time.get_ticks()

                #     if self.tool_index < len(list(left_hand_data.keys())) - 1:
                #         self.tool_index += 1
                #     else:
                #         self.tool_index = 0
                #     self.tool = list(left_hand_data.values())[self.tool_index]["item"]
                #     self.tool_weight = list(left_hand_data.values())[self.tool_index]["weight"]
                #     self.tool_type = list(left_hand_data.values())[self.tool_index]["type"]
                
                # # spell switch
                # if keys[pygame.K_UP] and self.can_switch_magic:
                #     self.can_switch_magic = False
                #     self.magic_switch_time = pygame.time.get_ticks()

                #     if self.magic_index < len(list(magic_data.keys())) - 1:
                #         self.magic_index += 1
                #     else:
                #         self.magic_index = 0
                #     self.magic = list(magic_data.keys())[self.magic_index]
                
                # # quick item switch
                # if keys[pygame.K_DOWN] and self.can_switch_qitems:
                #     self.can_switch_qitems = False
                #     self.qitems_switch_time = pygame.time.get_ticks()

                #     if self.qitems_index < len(self.qitems) - 1:
                #         self.qitems_index += 1
                #     else:
                #         self.qitems_index = 0

                #     self.qitems = []
                #     self.qitems_uses = []
                #     for i in ["slot1", "slot2", "slot3", "slot4"]:
                #         if qitems_data[i]['item'] != None:
                #             self.qitems.append(qitems_data[i]['item'])
                #             self.qitems_uses.append(qitems_data[i]['amount'])
                
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown + right_hand_data[self.weapon_slot]["cooldown"]:
                self.attacking = False
                self.destroy_attack()
                #self.destroy_tool()
        
        if self.using_tool:
            if current_time - self.tool_time >= self.tool_cooldown + left_hand_data[self.tool_slot]["cooldown"]:
                self.using_tool = False
                #self.destroy_attack()
                self.destroy_tool()

        if not self.can_toggle_menu:
            if current_time - self.menu_toggle_time >= self.menu_toggle_cooldown:
                self.can_toggle_menu = True

        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.weapon_switch_cooldown:
                self.can_switch_weapon = True
        
        if not self.can_switch_tool:
            if current_time - self.tool_switch_time >= self.tool_switch_cooldown:
                self.can_switch_tool = True
        
        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.weapon_switch_cooldown:
                self.can_switch_magic = True
        
        if not self.can_switch_qitems:
            if current_time - self.qitems_switch_time >= self.qitems_switch_cooldown:
                self.can_switch_qitems = True

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invincibility_duration:
                self.vulnerable = True

        if self.rolling:
            if current_time - self.roll_duration >= self.roll_cooldown:
                self.rolling = False
                #self.speed *= 2
        
        if self.using_item:
            if current_time - self.item_use_time >= self.item_cooldown:
                self.using_item = False
                self.resting = False
                self.status = "down_idle"
        
        if self.poise_broken:
            if current_time - self.broken_poise_time >= self.broken_poise_effect_time:
                self.poise_broken = False
                self.stunned = False
                self.poise = self.max_poise
                if not self.dead: self.status = "down_idle"

        if self.knocked_back:
            if current_time - self.knocked_back_time >= self.knocked_back_length:
                self.knocked_back = False
                self.direction *= 0

    def animate(self):
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index  >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if not self.vulnerable:
            # Flicker
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def get_full_weapon_damage(self):
        base_damage = player_data['dependent_variables']['attack']
        #weapon_damage = weapon_data[self.weapon]["damage"]
        weapon_damage = right_hand_data[list(right_hand_data.keys())[self.weapon_index]]["damage"]
        
        # todo: add check for light/heavy attack, and alter damage/stamina usage/use time accordingly

        return base_damage + weapon_damage

    def get_full_tool_damage(self):
        base_damage = player_data['dependent_variables']['attack']
        weapon_damage = left_hand_data[list(left_hand_data.keys())[self.tool_index]]["damage"]

        return base_damage + weapon_damage
    
    def get_full_magic_damage(self):
        base_damage = player_data['dependent_variables']["magic damage"]
        spell_damage = magic_data[self.magic]["strength"]

        return base_damage + spell_damage
    
    def get_value_by_index(self, index):
        return list(self.attributes.values())[index]

    def get_cost_by_index(self, index):
        # return list(self.base_upgrade_cost.values())[index]
        # self.current_upgrade_cost = self.base_upgrade_cost["VITALITY"] * self.level + randint(1, 100)
        return player_data['values']['levelup_cost']

    def stamina_recovery(self):
        if self.status != "dead":
            if self.stamina_target < player_data['dependent_variables']["stamina"]:
                self.stamina_target += self.stamina_recovery_speed
            else:
                self.stamina_target = player_data['dependent_variables']["stamina"]
    
    def mana_recovery(self):
        if self.status != "dead":
            if self.mana_target < player_data['dependent_variables']["mana"]:
                self.mana_target += self.mana_recovery_speed
            else:
                self.mana_target = player_data['dependent_variables']["mana"]

    def on_humanity_increased(self, humanity, max):
        if humanity >= max:
            humanity = 99
        return humanity
    
    def check_death(self):
        if self.health_target <= 0 and not self.dead:
            self.health_target = 0
            self.health = 0
            self.dead = True
            self.vulnerable = False
            self.status = "dead"
            self.ongoing_run = False

            self.trigger_death_particles(self.rect.center, "player")
            self.check_player_death()

            current_channel = pygame.mixer.find_channel(True)
            current_channel.play(self.death_sound)

            # Stop movements
            self.direction.y = 0
            self.direction.x = 0

            # On death effects
            player_data['status']['hollow'] = True
            player_data['values']['lost_souls'] = player_data['values']['souls']
            player_data['values']['lost_humanity'] = player_data['values']['humanity']
            player_data['values']['souls'] = 0
            player_data['values']['humanity'] = 0
            print(f"{player_data['values']['lost_souls']} souls and {player_data['values']['lost_humanity']} humanity lost")

    def check_player_poise(self, dmg):
        poise_dmg = round(dmg // 2, 1)

        # DO NOT USE for player, will use for enemy poise
        # if self.poise == 0 and not self.poise_broken:
        if self.poise - poise_dmg <= 0:
            print("Poise broken!")
            # Stop movements
            # self.direction.y = 0
            # self.direction.x = 0

            self.poise_broken = True
            self.broken_poise_time = pygame.time.get_ticks()
            self.knocked_back = True
            self.knocked_back_time = pygame.time.get_ticks()

            self.stunned = True
            self.status = "stunned"
            #self.vulnerable = False

            #self.direction *= -1

        if self.poise < self.max_poise and self.knocked_back:
            self.poise += 0.1
            self.poise = round(self.poise, 1)
            

    def update(self):
        self.enemy_collision("horizontal", self.attackable_sprites)
        self.enemy_collision("vertical", self.attackable_sprites)

        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed, self.sprite_type)
        player_data['values']['humanity'] = self.on_humanity_increased(player_data['values']['humanity'], 99)
        self.stamina_recovery()
        self.mana_recovery()
        self.check_death()
        #self.check_player_poise()

        # Todo: place the following in a method
        if self.menu_open: self.main_menu()
        if self.menu_inventory: self.inventory_display()
        if self.menu_status: self.status_display()
        if self.menu_system: self.system_display()
        if self.menu_equipment: self.equipment_display()