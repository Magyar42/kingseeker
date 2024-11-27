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
    def __init__(self, pos, groups, obstacle_sprites, attackable_sprites, create_attack, destroy_attack, create_magic, trigger_death_particles, check_player_death, use_item_effect, toggle_screen_effect):
        super().__init__(groups)
        self.animation_speed = 0.15

        self.toggle_screen_effect = toggle_screen_effect
        self.animation_player = AnimationPlayer()

        self.popup = gameMenu(self.toggle_screen_effect)
        self.prompt_active = False

        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("assets/graphics/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-6, HITBOX_OFFSET["player"])
        self.sprite_type = "player_sprite"

        self.import_player_assets()
        self.status = "down"

        # Determines how long the player "freezes" when performing an attack
        self.attacking = False
        self.attack_cooldown = 300
        self.attack_time = None

        # Determines the cooldown between skill attacks
        self.using_skill = False
        self.skill_cooldown = 5000
        self.skill_use_time = None

        # Determines the cooldown between magic attacks
        self.casting_spell = False
        self.spell_cooldown = 2000
        self.spell_use_time = None

        # Determines the cooldown between light attacks
        self.light_attacking = False
        self.light_attack_cooldown = 520
        self.light_attack_time = None

        # Determines the cooldown between heavy attacks
        self.heavy_attacking = False
        self.heavy_attack_cooldown = 750
        self.heavy_attack_time = None

        self.obstacle_sprites = obstacle_sprites
        self.attackable_sprites = attackable_sprites

        # weapon
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack

        self.weapon = interface_details["light_attack"]["name"].split("_")[0]
        self.weapon_weight = interface_details["light_attack"]["weight"]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.weapon_switch_cooldown = 200

        # magic
        self.catalyst = interface_details["catalyst"]["name"]
        self.create_magic = create_magic
        self.spell_index = 0
        self.current_spell = interface_details["spells"][self.spell_index+1]
        self.scrolling_spells = False
        self.spell_scroll_cooldown = 200
        self.spell_scroll_time = None

        # stats
        self.stamina_light_attack_mult = 3
        self.stamina_heavy_attack_mult = 5
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
        self.xp = interface_details['values']['souls']
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
        interface_details['values']['levelup_cost'] = round(self.upgrade_equation)

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
        self.estus_sound = pygame.mixer.Sound("assets/audio/sfx/estus_flask.wav")
        self.estus_sound.set_volume(0.3)
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

        # Estus use
        self.drinking_estus = False
        self.estus_cooldown = 500
        self.estus_use_time = None
        self.use_item_effect = use_item_effect
        
        self.menu_open = False
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
        self.selected_spell_index = 0
        self.trigger_boons_update = False
        self.any_interface_open = False
    
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
        
        if self.attacking:
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
        elif self.drinking_estus:
            self.status = "item"
            self.resting = True
            self.direction.x = 0
            self.direction.y = 0

            estus_image = pygame.image.load("assets/graphics/ui/interface_icons/inputs/estus.png").convert_alpha()
            x, y = centreImage(estus_image)
            self.display_surface.blit(estus_image, (x, y - 40))

        else:
            if "attack" in self.status:
                self.status = self.status.replace("_attack", "")
            elif "roll" in self.status:
                self.status = self.status.replace("_roll", "")

    def main_menu(self):
        if self.menu_open:
            self.popup.displayMenu(self)

    def input(self):
        if not self.any_interface_open:
            keys = pygame.key.get_pressed()

            if self.can_toggle_menu and not self.submenu_open:
                if keys[pygame.K_ESCAPE] and not self.menu_open:
                    self.menu_open = True
                    self.can_toggle_menu = False
                    self.menu_toggle_time = pygame.time.get_ticks()
                    #self.resting = True
                elif keys[pygame.K_ESCAPE] and self.menu_open:
                    self.menu_open = False
                    self.can_toggle_menu = False
                    self.menu_toggle_time = pygame.time.get_ticks()
                    self.resting = False

            # If the input is pressed during another attack, set action to false
            # Otherwise, the action will be "queued"
            if self.attacking:
                player_inputs["cast spell"] = False
                player_inputs["light attack"] = False
                player_inputs["heavy attack"] = False
            
            # If the SAME input is pressed during the COOLDOWN, set action to false
            # Otherwise, the action will be "queued"
            if self.casting_spell: player_inputs["cast spell"] = False
            elif self.light_attacking: player_inputs["light attack"] = False
            elif self.heavy_attacking: player_inputs["heavy attack"] = False


            if not self.attacking and not self.resting and not self.rolling and not self.stunned:
                if not self.dead:
                    # estus input
                    if keys[pygame.K_f] and not self.drinking_estus:       # Todo: change to not use index, but name, so that any item can be assigned to quick use 
                        
                        if interface_details["values"]["current estus"] > 0:
                            self.drinking_estus = True
                            self.estus_use_time = pygame.time.get_ticks()
                            self.use_item_effect()

                            interface_details["values"]["current estus"] -= 1
                            self.health_increase += 300 # todo: include estus level in amount of hp recovered AND update HP numbers
                            if self.health_increase >= player_data['dependent_variables']['health']:
                                self.health_increase = player_data['dependent_variables']['health']
                            self.estus_sound.play()

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

                    # skill input
                    # todo: skill effect
                    if keys[pygame.K_q] and not self.using_skill:
                        # todo: check stamina/mana cost and take away as needed
                        print("Skill used!")

                        self.attacking = True
                        self.attack_time = pygame.time.get_ticks()
                        self.using_skill = True
                        self.skill_use_time = pygame.time.get_ticks()

                    # spell cast
                    # todo: spell effect
                    if player_inputs["cast spell"] and not self.casting_spell:
                        # todo: check stamina/mana cost and take away as needed
                        if self.stamina_target - self.stamina_magic_mult >= 0:
                            self.stamina_target -= self.stamina_magic_mult
                            
                            spell_name = interface_details["spells"][self.spell_index+1]
                            spell_power = (magic_data[spell_name]["strength"] + interface_details["catalyst"]["base damage"]) * player_data["dependent_variables"]["magic mult"]
                            spell_fp_cost = magic_data[spell_name]["cost"]
                            self.create_magic(spell_name, spell_power, spell_fp_cost)

                            self.attacking = True
                            self.attack_time = pygame.time.get_ticks()
                            self.casting_spell = True
                            self.spell_use_time = pygame.time.get_ticks()

                            player_inputs["cast spell"] = False

                    # attack input - light
                    if player_inputs["light attack"] and not self.light_attacking:
                        if self.stamina_target - (self.stamina_light_attack_mult * self.weapon_weight) >= 0:
                            self.stamina_target -= (self.stamina_light_attack_mult * self.weapon_weight) # Effect on stamina

                            self.attacking = True
                            self.attack_time = pygame.time.get_ticks()
                            self.light_attacking = True
                            self.light_attack_time = pygame.time.get_ticks()

                            self.create_attack()
                            self.weapon_attack_sound.play()
                            player_inputs["light attack"] = False

                    # attack input - heavy
                    if player_inputs["heavy attack"] and not self.heavy_attacking:
                        if self.stamina_target - (self.stamina_heavy_attack_mult * self.weapon_weight) >= 0:
                            self.stamina_target -= (self.stamina_heavy_attack_mult * self.weapon_weight) # Effect on stamina

                            self.attacking = True
                            self.attack_time = pygame.time.get_ticks()
                            self.heavy_attacking = True
                            self.heavy_attack_time = pygame.time.get_ticks()

                            self.create_attack()
                            self.weapon_attack_sound.play()
                            player_inputs["heavy attack"] = False


                    # mousewheel - scroll through spells
                    if player_inputs["scroll spell"]:

                        self.scrolling_spells = True
                        self.spell_scroll_time = pygame.time.get_ticks()

                        self.spell_index -= player_inputs["scroll direction"]
                        if self.spell_index > 2: self.spell_index = 0
                        elif self.spell_index < 0: self.spell_index = 2

                        player_inputs["scroll spell"] = False
                        player_inputs["scroll direction"] = 0
                
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown + interface_details["light_attack"]["cooldown"]:
                self.attacking = False
                self.destroy_attack()
        
        if self.light_attacking:
            if current_time - self.light_attack_time >= self.light_attack_cooldown:
                self.light_attacking = False

        if self.heavy_attacking:
            if current_time - self.heavy_attack_time >= self.heavy_attack_cooldown:
                self.heavy_attacking = False
        
        if self.using_skill:
            if current_time - self.skill_use_time >= self.skill_cooldown:
                self.using_skill = False

        if self.casting_spell:
            if current_time - self.spell_use_time >= self.spell_cooldown:
                self.casting_spell = False

        if not self.can_toggle_menu:
            if current_time - self.menu_toggle_time >= self.menu_toggle_cooldown:
                self.can_toggle_menu = True

        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.weapon_switch_cooldown:
                self.can_switch_weapon = True

        if self.scrolling_spells:
            if current_time - self.spell_scroll_time >= self.spell_scroll_cooldown:
                self.scrolling_spells = False

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invincibility_duration:
                self.vulnerable = True

        if self.rolling:
            if current_time - self.roll_duration >= self.roll_cooldown:
                self.rolling = False
                #self.speed *= 2
        
        if self.drinking_estus:
            if current_time - self.estus_use_time >= self.estus_cooldown:
                self.drinking_estus = False
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
    
    # Update boons display - called from level's enable_player_control()
    def update_boons(self):
        self.popup.boons = []
        # Only load boons (not sub-boons) for the display
        for current_boon in interface_details["boons"]["list"]:
            if not boon_data[current_boon]["is_subboon"]:
                current_boon_surf = pygame.image.load(f"assets/graphics/ui/interface_icons/boons/{current_boon}.png")
                self.popup.boons.append(current_boon_surf)

    def get_full_weapon_damage(self):
        base_damage = player_data['dependent_variables']['attack']
        #weapon_damage = weapon_data[self.weapon]["damage"]
        #weapon_damage = right_hand_data[list(right_hand_data.keys())[self.weapon_index]]["damage"]
        weapon_damage = interface_details["light_attack"]["base damage"]
        
        # todo: add check for light/heavy attack, and alter damage/stamina usage/use time accordingly

        return base_damage + weapon_damage
    
    def get_full_magic_damage(self):
        base_damage = interface_details["catalyst"]["base damage"]
        spell_damage = magic_data[self.current_spell]["strength"]
        dmg_multiplier = player_data['dependent_variables']['magic mult']

        return (base_damage + spell_damage) * dmg_multiplier
    
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
            interface_details['values']['lost souls'] = interface_details['values']['souls']
            interface_details['values']['souls'] = 0

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
    
    def display_overlay(self):
        bg_overlay = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        bg_overlay.fill(TEXT_BG_COLOUR)
        self.display_surface.blit(bg_overlay, (0,0))

    def update(self):
        self.enemy_collision("horizontal", self.attackable_sprites)
        self.enemy_collision("vertical", self.attackable_sprites)

        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed, self.sprite_type)
        self.stamina_recovery()
        self.mana_recovery()
        self.check_death()
        #self.check_player_poise()

        if self.menu_open: self.main_menu()
        if self.trigger_boons_update: self.update_boons()
        if self.any_interface_open: self.display_overlay()