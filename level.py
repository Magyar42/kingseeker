import pygame
from settings import *
from tile import Tile
from player import Player
from support import *
from gameinfo import *
from random import choice, randint
from weapon import *
from debug import debug
from ui import UI
from enemy import Enemy
#from boss import Boss
from particles import AnimationPlayer
from magic import MagicPlayer
from bonfire import Bonfire
#from upgrade import Upgrades
from bloodstain import Bloodstain
#from objects import FloorItem
#from objects import Chest
#from objects import Lever
#from objects import Message
# from boss import HurtBoxes
from weapon import Hurtboxes
from npc import NPC
from interactable_items import SummonSign, ResourceItem, PerkPillar
from popups import BoonsMenu, HumanityPowers, LevelUp, WeaponsSelection

class Level:
    def __init__(self, map_id, exit):
        self.display_surface = pygame.display.get_surface()
        self.map_id = map_id
        self.levelup_menu_active = False
        self.show_screen_effect = False
        self.displaying_message = False
        self.current_message_id = 0
        self.font = pygame.font.Font(UI_FONT, MEDIUM_FONT_SIZE)
        self.exit_effect = exit

        if flags["completed_tutorial"]: self.region = "firelink_shrine"
        else: self.region = "the_asylum"
        
        self.reward = None
        self.region_chambers_done = 0 # Amount of chambers for THIS region completed
        self.available_chambers = chambers_per_region[self.region]
        self.visible_sprites = YSortCameraGroup(self.map_id, self.region)
        self.screen_sprites = ScreenCameraGroup(self.map_id, self.region)
        self.obstacle_sprites = pygame.sprite.Group()
        self.attack_sprites = pygame.sprite.Group()
        self.boss_attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        self.interactable_sprites = pygame.sprite.Group()

        self.sprite_groups_list = [
            self.visible_sprites, 
            self.obstacle_sprites, 
            self.attack_sprites, 
            self.attackable_sprites,
            self.interactable_sprites,
            self.screen_sprites,
        ]

        self.current_attack = None
        self.hurtbox = None
        # self.current_hurtboxes = []
        # self.hurtboxes = Hurtboxes([self.attack_sprites])

        # Enemy Spawning
        self.enemy_spawn_coords = []
        self.chamber_wave_active = False
        self.chamber_active_enemies = 0
        self.enemies_list_empty = False
        self.chamber_cleared = False
        self.reward_pos = (0, 0)

        self.create_map(True, self.map_id)

        self.ui = UI()
        self.boons_menu = BoonsMenu(self.boons_postmenu)
        self.humanity_menu = HumanityPowers(self.enable_player_control)
        self.levelup_menu = LevelUp(self.enable_player_control)
        self.weapons_menu = WeaponsSelection(self.enable_player_control)
        self.boons_menu_open = False
        self.humanity_menu_open = False
        self.levelup_menu_open = False
        self.weapons_menu_open = False
        self.boon_options = None

        # self.upgrade = Upgrades(self.player, self.toggle_menu)
        self.bloodstain_present = False

        # Particle Effects
        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

        # Sound
        self.death_macro_sound = pygame.mixer.Sound("assets/audio/sfx/player_death.wav")
        self.death_macro_sound.set_volume(1)
        self.retrieval_macro_sound = pygame.mixer.Sound("assets/audio/sfx/new_area.wav")
        self.retrieval_macro_sound.set_volume(1)
        self.victory_macro_sound = pygame.mixer.Sound("assets/audio/sfx/victory_achieved.wav")
        self.victory_macro_sound.set_volume(1)
        self.bonfire_sound = pygame.mixer.Sound("assets/audio/sfx/bonfire_rest.wav")
        self.bonfire_sound.set_volume(0.5)
        self.kindling_sound = pygame.mixer.Sound("assets/audio/sfx/kindling.wav")
        self.kindling_sound.set_volume(0.3)

        self.current_bloodstain_pos = ()

    def create_enemy_spawns(self, player, region, spawn_locations):
        # Get values
        spawn_id = choice(list(enemy_spawn_template[region].keys()))
        min = enemy_spawn_template[region][spawn_id]["min_enemies"]
        max = enemy_spawn_template[region][spawn_id]["max_enemies"]
        type_list = enemy_spawn_template[region][spawn_id]["whitelisted_enemies"]
        total_enemies = randint(min, max)
        print(total_enemies)

        # Set details - depends on the type of the spawn_id
        if enemy_spawn_template[region][spawn_id]["type"] == "waves":
            # Select number of waves
            min_waves = enemy_spawn_template[region][spawn_id]["min_waves"]
            max_waves = enemy_spawn_template[region][spawn_id]["max_waves"]
            num_waves = randint(min_waves, max_waves)

            # Set number of enemies in each wave
            enemies_per_wave = total_enemies // num_waves
            remainder_enemies = total_enemies % num_waves

            # Update chamber_enemy_info dictionary
            chamber_enemy_info["num_waves"] = num_waves
            chamber_enemy_info["enemies_per_wave"] = enemies_per_wave
            chamber_enemy_info["remainder_enemies"] = remainder_enemies

        elif enemy_spawn_template[region][spawn_id]["type"] == "constant":
            # Select initial number of enemies
            max_initial_num = total_enemies // 2
            initial_num_divider = randint(2,3) # todo: add check to ensure initial value is !> number of spawn points (and is !< 2)
            enemy_initial_num = max_initial_num // initial_num_divider

            # Update chamber_enemy_info dictionary
            chamber_enemy_info["initial_num"] = enemy_initial_num

        for enemy in range(total_enemies):
            spawn_pos = choice(spawn_locations)
            print(spawn_pos)
            spawn_locations.remove(spawn_pos)
            type = choice(type_list)

            enemy_info = [spawn_pos, type]
            chamber_enemy_info["enemy_list"].append(enemy_info)
        
        # Update chamber_enemy_info dictionary
        chamber_enemy_info["type"] = enemy_spawn_template[region][spawn_id]["type"]
        chamber_enemy_info["total_enemies"] = total_enemies

        print(f"{chamber_enemy_info}\n")
    
    def check_enemy_spawns(self):
        # If all enemies defeated, set active to False
        if self.chamber_active_enemies == 0 and self.chamber_wave_active:
            self.chamber_wave_active = False

        if len(chamber_enemy_info["enemy_list"]) > 0: # Only triggers if list of enemies has any enemies in it

            if chamber_enemy_info["type"] == "waves":
                if not self.chamber_wave_active: # Ensures only one wave's enemies are spawned

                    # Get number of enemies to spawn; often the set value, but checks for remainders
                    if len(chamber_enemy_info["enemy_list"]) < chamber_enemy_info["enemies_per_wave"]:
                        enemies_per_wave = chamber_enemy_info["remainder_enemies"]
                    else:
                        enemies_per_wave = chamber_enemy_info["enemies_per_wave"]

                    for num in range(enemies_per_wave):
                        spawn_anim_pos = (chamber_enemy_info["enemy_list"][num][0][0] + 32, chamber_enemy_info["enemy_list"][num][0][1] + 32) # Centres anim with enemy
                        
                        self.animation_player.create_particles("enemy_spawn2", spawn_anim_pos, [self.visible_sprites], "ambient", 0.25, self.spawn_enemies)
                        
                        # Enemy(chamber_enemy_info["enemy_list"][0][1], chamber_enemy_info["enemy_list"][0][0], [self.visible_sprites, self.attackable_sprites], self.obstacle_sprites, self.attackable_sprites, self.damage_player, self.trigger_death_particles, self.add_xp, self.death_effect)
                        
                        # print(chamber_enemy_info["enemy_list"][0])
                        # chamber_enemy_info["enemy_list"].pop(0)
                    
                    # print("End of this wave's spawning.")
                    self.chamber_active_enemies = enemies_per_wave
                    self.chamber_wave_active = True
            
            if chamber_enemy_info["type"] == "constant":
                if not self.chamber_wave_active: # Ensures only one wave's enemies are spawned

                    spawn_anim_pos = (chamber_enemy_info["enemy_list"][0][0][0] + 32, chamber_enemy_info["enemy_list"][0][0][1] + 32) # Centres anim with enemy
                        
                    self.animation_player.create_particles("enemy_spawn2", spawn_anim_pos, [self.visible_sprites], "ambient", 0.25, self.spawn_enemies)
                    
                    self.chamber_active_enemies = 1 # Spawn one after one dies
                    self.chamber_wave_active = True
        
        else:
            self.enemies_list_empty = True

    def death_effect(self):     # On enemy death
        self.chamber_active_enemies -= 1
        if self.enemies_list_empty and self.chamber_active_enemies == 0:
            self.chamber_cleared = True
            self.animation_player.create_particles("nova", (self.reward_pos[0] + 32, self.reward_pos[1] + 32), [self.visible_sprites], "ambient", 0.15, self.spawn_reward)
    
    def spawn_reward(self):
        # If self.reward is a BOON
        if self.reward in boon_summons:
            covenant_index = boon_summons.index(self.reward)
            covenant_sign = covenants[covenant_index]

            # todo: update to ANY of the potential rewards
            SummonSign(covenant_sign, (self.reward_pos), [self.visible_sprites, self.interactable_sprites, self.obstacle_sprites], self.summon_sign_effect)
        
        # Else if vendor
        elif self.reward == "vendor":
            print("money!") # todo

        # Else if self.reward is a RESOURCE
        else:
            ResourceItem(self.reward, (self.reward_pos), [self.visible_sprites, self.interactable_sprites, self.obstacle_sprites])

    
    def spawn_enemies(self):
        Enemy(chamber_enemy_info["enemy_list"][0][1], chamber_enemy_info["enemy_list"][0][0], [self.visible_sprites, self.attackable_sprites], self.obstacle_sprites, self.attackable_sprites, self.damage_player, self.trigger_death_particles, self.add_xp, self.death_effect)

        print(chamber_enemy_info["enemy_list"][0])
        chamber_enemy_info["enemy_list"].pop(0)
    
    # def find_current_region(self, id):
    #     region_num = id[0]
    #     self.region = region_values[region_num]

    def create_map(self, player_reset, map_id = "000", trigger_region_title = False):
        # self.find_current_region(map_id)
        self.enemies_list_empty = False
        if map_id not in safe_rooms: self.chamber_cleared = False
        else: self.chamber_cleared = True

        if self.region == "firelink_shrine" or map_id == "900": prevent_player_input = True
        else: prevent_player_input = False

        layouts = {
            "boundary": import_csv_layout(f"assets/map/{self.region}/{map_id}/map_FloorBlocks.csv"),
            #"grass": import_csv_layout("assets/map/map_Grass.csv"),
            "object": import_csv_layout(f"assets/map/{self.region}/{map_id}/map_LargeObjects.csv"),
            "entities": import_csv_layout(f"assets/map/{self.region}/{map_id}/map_Entities.csv"),
        }
        graphics = {
            "grass": import_folder("assets/graphics/grass"),
            "objects": import_folder("assets/graphics/objects"),
        }

        transition_ids = [0, 1]
        unique_id = None # by default
        self.enemy_spawn_coords = []
        chamber_enemy_info["enemy_list"] = []
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for column_index, column in enumerate(row):
                    if column != "-1":
                        x = column_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == "boundary":
                            Tile((x, y), [self.obstacle_sprites], "invisible")
                        # if style == "grass":
                        #     random_grass_image = choice(graphics["grass"])
                        #     Tile((x, y), [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites], "grass", random_grass_image)
                        if style == "object":
                            surface = graphics["objects"][int(column)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], "object", surface)
                        if style == "entities":
                            if column == "394":
                                if player_reset:
                                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites, self.attackable_sprites, self.create_attack, self.destroy_attack, self.create_magic, self.trigger_death_particles, self.check_player_death, self.use_item_effect, self.toggle_screen_effect, prevent_player_input, self.lock_player, self.enable_player_control, self.exit_effect)
                            elif column == "388":
                                self.bonfire = Bonfire(0, (x, y), [self.visible_sprites, self.obstacle_sprites, self.interactable_sprites], self.restart_world, self.check_humanity_restored, self.check_bonfire_lit, self.check_bonfire_rest, self.toggle_menu, self.toggle_screen_effect, self.kindle_bonfire_visuals)
                            elif column == "277": # Potential enemy spawns
                                self.enemy_spawn_coords.append([x, y])
                            elif column in npc_list:
                                effect = None
                                reward = "None"
                                rotate_val = 0
                                if column == "389": npc_id = "firekeeper"
                                elif column == "367": npc_id = "crestfallen"
                                elif column == "345": npc_id = "frampt"
                                elif column == "323": npc_id = "andre"
                                elif column == "301": npc_id = "patches"
                                elif column == "279": npc_id = "petrus"
                                elif column == "257": npc_id = "reah"
                                elif column == "368": npc_id = "lautrec"
                                elif column == "346": npc_id = "siegmeyer"
                                elif column == "324": npc_id = "solaire"
                                elif column == "302": npc_id = "ingward"
                                elif column == "280": npc_id = "laurentius"
                                elif column == "258": npc_id = "logan"
                                elif column == "369": npc_id = "merchant"
                                elif column == "347": npc_id = "kaathe"
                                elif column == "325": npc_id = "domhnall"
                                elif column == "303": npc_id = "knightess"
                                elif column == "281": npc_id = "oscar"
                                elif column == "259": npc_id = "quelana"
                                elif column == "370": npc_id = "oscar_tutorial"
                                elif column == "366" or column == "344":
                                    if column == "344": rotate_val = 90
                                    npc_id = "transition_prompt"
                                    effect = self.load_new_chamber

                                    if map_id == "000": # todo: change back
                                        # reward = choice(boon_summons)
                                        reward = "darkwraith_summon"
                                    else: reward = choice(list(chamber_rewards.keys()))

                                    unique_id = transition_ids[0]
                                    transition_ids.pop(0)
                                NPC(npc_id, (x, y), [self.visible_sprites, self.interactable_sprites, self.obstacle_sprites], self.chamber_cleared, self.blit_reward_icon, self.lock_player, self.enable_player_control, self.map_id, effect, reward, unique_id, rotate_val)
                            elif column in pillar_list:
                                if column == "386": pillar_type = "perks"
                                elif column == "364": pillar_type = "levels"
                                elif column == "342": pillar_type = "bonfire"
                                elif column == "320": pillar_type = "weapons"
                                elif column == "298": pillar_type = "anvil"
                                PerkPillar(pillar_type, (x, y), [self.visible_sprites, self.interactable_sprites, self.obstacle_sprites], self.trigger_pillar_effect, self.check_status)
                            elif column == "387":
                                # covenant_sign = choice(covenants) # todo: set to random
                                self.reward_pos = (x, y)
                                # covenant_sign = "warriors_of_sunlight"
                                # SummonSign(covenant_sign, (x, y), [self.visible_sprites, self.interactable_sprites, self.obstacle_sprites], self.summon_sign_effect)
                            else:
                                if column == "390": enemy_name = "bamboo"
                                elif column == "391": enemy_name = "spirit"
                                elif column == "392": enemy_name = "raccoon"
                                elif column == "393": enemy_name = "squid"
                                else: enemy_name = "bamboo" # todo: change
                                Enemy(enemy_name, (x, y), [self.visible_sprites, self.attackable_sprites], self.obstacle_sprites, self.attackable_sprites, self.damage_player, self.trigger_death_particles, self.add_xp, self.death_effect)

        # Spawn enemies if NOT in safe room
        if map_id not in safe_rooms:
            self.create_enemy_spawns(self.player, self.region, self.enemy_spawn_coords)
        # If in reward-first room, spawn the reward
        if map_id in reward_first_rooms:
            self.spawn_reward()

        if trigger_region_title:
            self.toggle_screen_effect()
            x = self.display_surface.get_size()[0] // 2
            y = self.display_surface.get_size()[1] // 4
            self.animation_player.create_macro(f"{self.region}", (x, y), [self.screen_sprites], None, 0.20, 0, self.toggle_screen_effect)

    def blit_reward_icon(self, reward, pos, is_npc=False):
        self.animation_player.create_icon(f"{reward}", pos, [self.visible_sprites], "ambient", 0.10, is_npc)

    def update_map(self, pos):       # triggered on player death, enemy death, item pickup
        self.bloodstain = Bloodstain(pos, [self.visible_sprites, self.interactable_sprites], self.check_souls_retrieval)
    
    # def update_hurtboxes(self, pos, size, frame_index, enemy_name, current_action):
    #     self.hurtbox = HurtBoxes(pos, size, [self.visible_sprites, self.boss_attack_sprites], self.destroy_hurtboxes, self.damage_player, enemy_name, current_action)
    #     #print(self.hurtbox) 

    # def destroy_hurtboxes(self):
    #     if self.hurtbox: self.hurtbox.kill()
    #     self.hurtbox = None

    def create_attack(self, attack_type):
        #self.current_attack = Weapon(self.player, [self.visible_sprites]) # self.attack_sprites
        
        direction = self.player.status.split("_")[0]
        pos = self.player.rect.center
        self.animation_player.create_attack(attack_type, pos, [self.visible_sprites, self.attack_sprites], "weapon", direction, self.create_attack_hurtboxes, self.destroy_attack_hurtboxes, 0.20)

    def create_magic(self, name, strength, cost):
        self.current_attack = Catalyst(self.player, [self.visible_sprites])
        if name == "heal":
            self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])
        elif name == "fire_surge":
            self.magic_player.fire_surge(self.player, cost, [self.visible_sprites, self.attack_sprites])
        elif name == "icecrag_burst":
            self.magic_player.icecrag_burst(self.player, cost, [self.visible_sprites, self.attack_sprites])

    def create_attack_hurtboxes(self, frame, attack_type, direction):
        current_hurtboxes_details = list(attack_hurtbox_data[direction][attack_type][frame])

        x_base = self.player.rect.x
        y_base = self.player.rect.y
        
        for box in current_hurtboxes_details:
            self.hurtbox = Hurtboxes([self.attack_sprites, self.visible_sprites], x_base+box[0], y_base+box[1], box[2], box[3])
            # self.destroy_attack_hurtboxes(frame) # Makes hurtboxes invisible

        # todo!!! make hitboxes disappear after
        
        # print(f"{frame}: {current_hurtboxes_objects}")
        # self.current_hurtboxes.append(current_hurtboxes_objects) # Save list X to list containing all hurtboxes currently

        # self.destroy_attack_hurtboxes(frame)

    def destroy_attack_hurtboxes(self, frame=0):
        if self.hurtbox: self.hurtbox.kill()
        self.hurtbox = None

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == "grass":
                            pos = target_sprite.rect.center
                            offset = pygame.math.Vector2(0, 50)

                            for leaf in range(randint(3, 6)):
                                self.animation_player.create_grass_particles(pos - offset, [self.visible_sprites], "ambient")
                            target_sprite.kill()
                        elif target_sprite.sprite_type == "enemy":
                            target_sprite.get_damage(self.player, attack_sprite.sprite_type)

    def damage_player(self, amount, attack_type):
        if self.player.vulnerable and not self.player.rolling:
            self.player.health_target -= amount
            self.player.health_increase -= amount

            # DO NOT USE for player, will use for enemy poise instead
            # self.player.poise -= (amount // 4)
            # if self.player.poise < 0:
            #     self.player.poise = 0
            # self.player.poise = round(self.player.poise, 1)

            self.player.check_player_poise(amount)

            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            self.animation_player.create_particles(attack_type, self.player.rect.center, [self.visible_sprites], "ambient")

    def trigger_death_particles(self, pos, particle_type):
        self.animation_player.create_particles(particle_type, pos, [self.visible_sprites], "ambient")

    def add_xp(self, amount):
        player_core_info['values']['souls'] += amount

    def toggle_menu(self):
        self.levelup_menu_active = not self.levelup_menu_active

    def toggle_screen_effect(self):
        self.show_screen_effect = not self.show_screen_effect

    def check_player_death(self):
        if self.player.dead:
            self.toggle_screen_effect()
            x = self.display_surface.get_size()[0] // 2
            y = self.display_surface.get_size()[1] // 2
            self.animation_player.create_macro("death", (x, y), [self.screen_sprites], self.restart_world, 0.08, 4000, self.toggle_screen_effect)

            current_channel = pygame.mixer.find_channel(True)
            current_channel.play(self.death_macro_sound)
        
    def check_player_stats(self, stat):
        if stat == "Health":
            # Actual health catching up with health increase
            if self.player.health_target < self.player.health_increase:
                self.player.health_target += 5
                self.player.transition_width_h = int(self.player.health_target - self.player.health_increase)
            if self.player.health_target > self.player.health_increase:
                self.player.health_target = self.player.health_increase

            # Display health catching up with actual health
            if self.player.health < self.player.health_target:
                self.player.health += 4
                self.player.transition_width_h = int((self.player.health - self.player.health_target) * 0.5)
            if self.player.health > self.player.health_target:
                self.player.health -= 4
                self.player.transition_width_h = int((self.player.health - self.player.health_target) * 0.5)
        
        elif stat == "Stamina":
            # Display stamina catching up with actual stamina
            if self.player.stamina < self.player.stamina_target:
                self.player.stamina += 0.5
                self.player.transition_width_s = int((self.player.stamina - self.player.stamina_target) * 2)
            if self.player.stamina > self.player.stamina_target:
                self.player.stamina -= 0.5
                self.player.transition_width_s = int((self.player.stamina - self.player.stamina_target) * 2)
        
        elif stat == "Mana":
            # Display mana catching up with actual mana
            if self.player.mana < self.player.mana_target:
                self.player.mana += 1
                self.player.transition_width_m = int((self.player.mana - self.player.mana_target) * 0.5)
            if self.player.mana > self.player.mana_target:
                self.player.mana -= 1
                self.player.transition_width_m = int((self.player.mana - self.player.mana_target) * 0.5)
    
    def check_souls_retrieval(self):
        self.toggle_screen_effect()
        self.bloodstain_present = False
        
        x = self.display_surface.get_size()[0] // 2
        y = self.display_surface.get_size()[1] // 2
        self.animation_player.create_macro("retrieval", (x, y), [self.screen_sprites], None, 0.25, 1500, self.toggle_screen_effect)

        current_channel = pygame.mixer.find_channel(True)
        current_channel.play(self.retrieval_macro_sound)

    def check_humanity_restored(self):
        self.toggle_screen_effect()
        x = self.display_surface.get_size()[0] // 2
        y = self.display_surface.get_size()[1] // 2
        self.animation_player.create_macro("humanity_restored", (x, y), [self.screen_sprites], None, 0.25, 1700, self.toggle_screen_effect)

        current_channel = pygame.mixer.find_channel(True)
        current_channel.play(self.retrieval_macro_sound)
    
    def check_victory_achieved(self):
        self.toggle_screen_effect()
        x = self.display_surface.get_size()[0] // 2
        y = self.display_surface.get_size()[1] // 2
        self.animation_player.create_macro("victory_achieved", (x, y), [self.screen_sprites], None, 0.25, 1700, self.toggle_screen_effect)

        current_channel = pygame.mixer.find_channel(True)
        current_channel.play(self.victory_macro_sound)

    def check_bonfire_lit(self):
        self.toggle_screen_effect()
        x = self.display_surface.get_size()[0] // 2
        y = self.display_surface.get_size()[1] // 2
        self.animation_player.create_macro("bonfire_lit", (x, y), [self.screen_sprites], None, 0.25, 1700, self.toggle_screen_effect)

        current_channel = pygame.mixer.find_channel(True)
        current_channel.play(self.retrieval_macro_sound)
    
    def check_bonfire_rest(self): # here for bonfire reset
        # self.toggle_screen_effect()
        # x = self.display_surface.get_size()[0] // 2
        # y = self.display_surface.get_size()[1] // 2
        # self.animation_player.create_macro("fire1", (x, y), [self.screen_sprites], self.restart_world, 0.2, 0, self.toggle_screen_effect)

        current_channel = pygame.mixer.find_channel(True)
        current_channel.play(self.bonfire_sound)

    def use_item_effect(self):
        self.animation_player.create_particles("sparkle", self.player.rect.center + pygame.math.Vector2(0, -40), [self.visible_sprites], "item")
        self.animation_player.create_particles("estus", self.player.rect.center + pygame.math.Vector2(-3, -30), [self.visible_sprites], "item")

    def kindle_bonfire_visuals(self, pos):
        self.animation_player.create_particles("estus", pos, [self.visible_sprites], "bonfire_effect")
        self.kindling_sound.play()

    # def spawn_chest_item(self, id, pos):
    #     FloorItem(id, pos, [self.visible_sprites, self.interactable_sprites], True)
    
    # def activated_lever_effect(self, id, pos):
    #     # todo: do an effect depending on the lever id
    #     print("Lever pulled!")

    def trigger_pillar_effect(self, type): # todo
        self.player.resting = True
        self.player.any_interface_open = True

        if type == "perks":
            self.humanity_menu_open = True
        elif type == "levels":
            self.levelup_menu_open = True
        elif type == "weapons":
            self.weapons_menu_open = True
        print("Perk pillar activated!")
    
    def summon_sign_effect(self, covenant):
        self.lock_player()
        self.boons_menu_open = True
        self.boon_options = self.boons_menu.generate_boons(covenant)
        print(f"{covenant} summon sign activated!")
    
    # Prevents player movement and prevents TAB menu toggle
    def lock_player(self):
        self.player.any_interface_open = True
        self.player.resting = True
        self.player.direction.y = 0
        self.player.direction.x = 0

    # Enables player movement, removing any screen-effects
    def enable_player_control(self):
        self.player.resting = False
        self.boons_menu_open = False
        self.humanity_menu_open = False
        self.levelup_menu_open = False
        self.weapons_menu_open = False
        self.player.any_interface_open = False
    
    def boons_postmenu(self):
        self.animation_player.create_particles("aura", self.player.rect.center, [self.visible_sprites], "ambient")

        self.player.trigger_boons_update = True
        self.enable_player_control()
    
    def activated_message_effect(self, id, pos):
        if not self.displaying_message:
            self.displaying_message = True
            self.player.resting = True
            self.current_message_id = id
        
        elif self.displaying_message:
            self.displaying_message = False
            self.player.resting = False
    
    def display_message(self, id):
        if self.displaying_message:
            bg_rect_size = (500, 100)
            x = (self.display_surface.get_size()[0] // 2) - (bg_rect_size[0] // 2)
            y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2) - 200

            main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
            pygame.draw.rect(self.display_surface, UI_BG_COLOUR, main_rect.inflate(10, 10))
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, main_rect.inflate(10, 10), 4)
            message_icon_rect = pygame.Rect(x + 20, y + 12, self.message_icon.get_width(), self.message_icon.get_height())
            
            current_line = 0
            for line in message_list[id]:
                current_line += 1
                text_surf = self.font.render(f"{line}", False, TEXT_COLOUR).convert_alpha()
                text_rect = text_surf.get_rect(topleft = (x, y) + pygame.math.Vector2(130, (20 * current_line)))
                self.display_surface.blit(text_surf, text_rect)

            self.display_surface.blit(self.message_icon, message_icon_rect)

    def update_player_stats(self):
        self.check_player_stats("Health")
        self.check_player_stats("Stamina")
        self.check_player_stats("Mana")

    def check_status(self, type):
        if type == "perks":
            if not self.humanity_menu_open: new_status = "idle"
            else: new_status = "active"
        elif type == "levels":
            if not self.levelup_menu_open: new_status = "idle"
            else: new_status = "active"
        elif type == "weapons":
            if not self.weapons_menu_open: new_status = "idle"
            else: new_status = "active"
        else: new_status = "idle"

        return new_status

    def restart_world(self, map = "000"):
        if not flags["completed_tutorial"]: map = "900"

        # Removes stuff
        for sprite_group in self.sprite_groups_list:
            for sprite in sprite_group:
                if sprite != self.player:
                    sprite.kill()
                elif self.player.status == "dead":
                    print(f"Died at {sprite.rect.center}.")
                    # bloodstain_pos = sprite.rect.center
                    # self.current_bloodstain_pos = bloodstain_pos
                    sprite.kill()
                    # self.bloodstain_present = True

        # Loads stuff
        self.map_id = map
        if flags["completed_tutorial"]: self.region = "firelink_shrine"
        else: self.region = "the_asylum"
        self.chamber_wave_active = False
        self.chamber_active_enemies = 0
        self.region_chambers_done = 0
        if self.player.status == "dead":
            self.visible_sprites = YSortCameraGroup(map, self.region)
            self.screen_sprites = ScreenCameraGroup(map, self.region)
            self.create_map(True, map)
            # self.update_map(bloodstain_pos)
            restore_estus(self.player, 1)   # todo: use kindle level of last bonfire
        else:
            self.create_map(False, map) # todo: dont reset for sitting at bonfire
            # if self.bloodstain_present: self.update_map(self.current_bloodstain_pos)
    
    def load_new_chamber(self, reward=None, id=None):
        trigger_region_title = False
        self.region_chambers_done += 1

        if self.region_chambers_done >= NUM_CHAMBERS_PER_REGION or self.region == "firelink_shrine": # If this region is FULLY completed
            print("Loading new region!")
            self.region_chambers_done = 0

            # todo: set dynamically
            if self.region == "the_asylum":
                chamber_id = "000"
                self.region = "firelink_shrine"
                flags["completed_tutorial"] = True
            elif self.region == "firelink_shrine":
                if id == 0:
                    chamber_id = "001"
                    self.region = "undead_burg"
                elif id == 1:
                    chamber_id = "401"
                    self.region = "catacombs"
                else:
                    chamber_id = "601"
                    self.region = "new_londo_ruins"
            elif self.region == "undead_burg":
                if id == 0:
                    chamber_id = "101"
                    self.region = "undead_parish"
                else:
                    chamber_id = "201"
                    self.region = "the_depths"
            
            self.available_chambers = chambers_per_region[self.region]
            trigger_region_title = True
            self.reward = reward

            self.ui.update_input_icons()

        # todo add check for region minus end room AND the room before
        # this is because ideally that room will have 1 exit, and will also not have any reward set

        elif self.region_chambers_done == NUM_CHAMBERS_PER_REGION - 1: # If this region is completed (minus end room)
            print("Loading end chamber!")
            if self.region == "the_asylum":
                update_dialogue_completion("oscar_tutorial", "002")
                control_flags["can_cast_spells"] = True
            region_num = region_values[self.region]
            chamber_id = f"{region_num}99" # Load end room
            self.reward = reward

        else: 
            print("Loading next chamber!")
            # todo: add method of loading safe/npc rooms when needed
            if self.region == "the_asylum" and self.region_chambers_done == 3:
                chamber_id = "903"
                update_dialogue_completion("oscar_tutorial", "001")
                control_flags["can_use_skill"] = True
                control_flags["can_drink_estus"] = True
            else:
                chamber_id = choice(self.available_chambers)
                self.available_chambers.remove(chamber_id) # Prevents same chamber from being loaded in a run
            self.reward = reward

        print(self.reward)
        self.map_id = chamber_id
        # Removes all sprites
        for sprite_group in self.sprite_groups_list:
            for sprite in sprite_group:
                sprite.kill()
        # Loads new sprites and inits new background
        self.visible_sprites = YSortCameraGroup(chamber_id, self.region)
        self.screen_sprites = ScreenCameraGroup(chamber_id, self.region)
        self.create_map(True, chamber_id, trigger_region_title)
    
    def update_dynamic_sprites(self):
        self.visible_sprites.enemy_update(self.player)
        self.visible_sprites.item_update(self.player)
        self.visible_sprites.chest_update(self.player)
        self.visible_sprites.lever_update(self.player)
        self.visible_sprites.message_update(self.player)
        self.visible_sprites.npc_update(self.player, self.chamber_cleared)
        self.visible_sprites.bonfire_update(self.player)
        self.visible_sprites.sign_update(self.player)
        self.visible_sprites.pillar_update(self.player)
        self.visible_sprites.resource_items_update(self.player)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.ui.permanent_display(self.player)
        if self.map_id not in safe_rooms: self.ui.combat_display(self.player)
        # self.boss.display(self.player)
        self.visible_sprites.update()
        self.screen_sprites.update()

        self.update_dynamic_sprites()
        self.check_enemy_spawns()

        if self.boons_menu_open: self.boons_menu.display(self.boon_options)
        if self.humanity_menu_open: self.humanity_menu.display()
        if self.levelup_menu_open: self.levelup_menu.display()
        if self.weapons_menu_open: self.weapons_menu.display()
        
        # Testing
        # debug(f"Position: {self.player.rect.center} | Status: {self.player.status}")
        # debug(f"Displayed HP: {self.player.health_target} | Actual HP: {self.player.health} | Increased HP: {self.player.health_increase}")
        # debug(f"Index: {int(self.player.frame_index)}")
        # debug(f"{self.player.poise} / {self.player.max_poise}")
        # debug(self.displaying_message)
        #get_attribute_num("vitality")
        # debug(resources["humanity sprites"])

        #self.bonfire.bonfire_popup_update(self.player)
        self.update_player_stats()

        if self.show_screen_effect:
            self.player_attack_logic()
        else:
            # if self.levelup_menu_active:
            #     self.upgrade.display()
            # else:
            self.display_message(self.current_message_id)
            # self.bonfire.bonfire_update(self.player) removed (todo for devlog)
            # this was causing the check for the player's distance from the bonfire
            # and thus the interaction to be firing always, even if there is no
            # bonfire present visually - moved to update_dynamic_sprites
            # as self.visible_sprites.bonfire_update(self.player), because then
            # ONLY visible sprites will get this update fired
            self.player_attack_logic()
            # if self.bloodstain_present: self.bloodstain.bloodstain_update(self.player)
            # if self.hurtbox: self.hurtbox.collision_update(self.player, self.hurtbox)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, map_id, region="undead_burg"):
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surface = pygame.image.load(f"assets/graphics/tilemap/{region}/ground_{map_id}.png").convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))
    
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): # Works but I don't know why
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
    
    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "enemy"]
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
    
    def item_update(self, player):
        item_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "floor_item"]
        for item in item_sprites:
            item.ground_items_update(player)
    
    def chest_update(self, player):
        chest_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "chest"]
        for chest in chest_sprites:
            chest.chest_update(player)
    
    def lever_update(self, player):
        lever_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "lever"]
        for lever in lever_sprites:
            lever.lever_update(player)
    
    def message_update(self, player):
        message_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "message"]
        for message in message_sprites:
            message.message_update(player)

    def npc_update(self, player, bool):
        npc_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "npc"]
        for npc in npc_sprites:
            npc.npc_update(player, bool)
    
    def bonfire_update(self, player):
        bonfire_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "bonfire"]
        for bonfire in bonfire_sprites:
            bonfire.bonfire_update(player)

    def sign_update(self, player):
        sign_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "summon_sign"]
        for sign in sign_sprites:
            sign.sign_update(player)
    
    def pillar_update(self, player):
        pillar_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "pillar"]
        for pillar in pillar_sprites:
            pillar.pillar_update(player)

    def resource_items_update(self, player):
        resource_items_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "resource"]
        for item in resource_items_sprites:
            item.resource_items_update(player)

class ScreenCameraGroup(pygame.sprite.Group):
    def __init__(self, map_id, region):
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surface = pygame.image.load(f"assets/graphics/tilemap/{region}/ground_{map_id}.png").convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))
    
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # floor_offset_pos = self.floor_rect.topleft - self.offset
        # self.display_surf