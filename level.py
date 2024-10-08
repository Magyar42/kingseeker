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
from npc import NPC
from interactable_items import SummonSign

class Level:
    def __init__(self, map_id):
        self.display_surface = pygame.display.get_surface()
        self.map_id = map_id
        self.levelup_menu_active = False
        self.show_screen_effect = False
        self.displaying_message = False
        self.current_message_id = 0
        self.font = pygame.font.Font(UI_FONT, MEDIUM_FONT_SIZE)

        self.visible_sprites = YSortCameraGroup(self.map_id)
        self.screen_sprites = ScreenCameraGroup(self.map_id)
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
        self.current_tool = None
        self.hurtbox = None

        self.create_map(True, self.map_id)

        self.ui = UI()
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
        self.message_icon = pygame.image.load("assets/graphics/ui/message_icon.png")

    def create_map(self, player_reset, map_id = "0"):
        layouts = {
            "boundary": import_csv_layout(f"assets/map/{map_id}/map_FloorBlocks.csv"),
            #"grass": import_csv_layout("assets/map/map_Grass.csv"),
            "object": import_csv_layout(f"assets/map/{map_id}/map_LargeObjects.csv"),
            "entities": import_csv_layout(f"assets/map/{map_id}/map_Entities.csv"),
        }
        graphics = {
            "grass": import_folder("assets/graphics/grass"),
            "objects": import_folder("assets/graphics/objects"),
        }

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
                                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites, self.attackable_sprites, self.create_attack, self.destroy_attack, self.create_tool, self.destroy_tool, self.create_magic, self.trigger_death_particles, self.check_player_death, self.use_item_effect, self.toggle_screen_effect)
                            elif column == "388":
                                self.bonfire = Bonfire(0, (x, y), [self.visible_sprites, self.obstacle_sprites, self.interactable_sprites], self.restart_world, self.check_humanity_restored, self.check_bonfire_lit, self.check_bonfire_rest, self.toggle_menu, self.toggle_screen_effect, self.kindle_bonfire_visuals)
                            # elif column == "396":
                            #     item_id = 1
                            #     if ground_item_list[item_id][0] == 0:
                            #         FloorItem(item_id, (x, y), [self.visible_sprites, self.interactable_sprites])
                            #     #self.flooritem.item_setup(item_id, (x, y), [self.visible_sprites, self.interactable_sprites])
                            # elif column == "397":
                            #     item_id = 3
                            #     chest_id = 0
                            #     if chest_list[chest_id] == 0: chest_opened = False
                            #     else: chest_opened = True
                            #     Chest(chest_id, item_id, (x, y), [self.visible_sprites, self.interactable_sprites, self.obstacle_sprites], self.spawn_chest_item, chest_opened)
                            # elif column == "398":
                            #     lever_id = 1
                            #     if lever_list[lever_id] == 0: lever_pulled = False
                            #     else: lever_pulled = True
                            #     Lever(lever_id, (x, y), [self.visible_sprites, self.interactable_sprites, self.obstacle_sprites], self.activated_lever_effect, lever_pulled)
                            # elif column == "399":
                            #     message_id = 1
                            #     Message(message_id, (x, y), [self.visible_sprites, self.interactable_sprites, self.obstacle_sprites], self.activated_message_effect)
                            # else:
                            #     if column == "389":
                            #         enemy_name = "asylum_demon"
                            #         self.boss = Boss(enemy_name, (x, y), [self.visible_sprites, self.attackable_sprites], self.obstacle_sprites, self.attackable_sprites, self.damage_player, self.trigger_death_particles, self.add_xp, self.update_hurtboxes, self.destroy_hurtboxes, self.check_victory_achieved)
                            elif column in npc_list:
                                effect = None
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
                                elif column == "366":
                                    npc_id = "transition_prompt"
                                    effect = self.load_new_region
                                NPC(npc_id, (x, y), [self.visible_sprites, self.interactable_sprites, self.obstacle_sprites], effect)
                            elif column == "387":
                                # covenant_sign = choice(covenants) # todo: set to random
                                covenant_sign = "warriors_of_sunlight"
                                SummonSign(covenant_sign, (x, y), [self.visible_sprites, self.interactable_sprites, self.obstacle_sprites], self.summon_sign_effect)
                            else:
                                if column == "390": enemy_name = "bamboo"
                                elif column == "391": enemy_name = "spirit"
                                elif column == "392": enemy_name = "raccoon"
                                elif column == "393": enemy_name = "squid"
                                else: enemy_name = "bamboo" # todo: change
                                Enemy(enemy_name, (x, y), [self.visible_sprites, self.attackable_sprites], self.obstacle_sprites, self.attackable_sprites, self.damage_player, self.trigger_death_particles, self.add_xp)

    def update_map(self, pos):       # triggered on player death, enemy death, item pickup
        self.bloodstain = Bloodstain(pos, [self.visible_sprites, self.interactable_sprites], self.check_souls_retrieval)
    
    def update_hurtboxes(self, pos, size, frame_index, enemy_name, current_action):
        self.hurtbox = HurtBoxes(pos, size, [self.visible_sprites, self.boss_attack_sprites], self.destroy_hurtboxes, self.damage_player, enemy_name, current_action)
        #print(self.hurtbox) 

    def destroy_hurtboxes(self):
        if self.hurtbox: self.hurtbox.kill()
        self.hurtbox = None

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])
    
    def create_tool(self):
        self.current_tool = Tool(self.player, [self.visible_sprites, self.attack_sprites])

    def create_magic(self, style, strength, cost):
        if style == "heal":
            self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])
        elif style == "fire_surge":
            self.magic_player.fire_surge(self.player, cost, [self.visible_sprites, self.attack_sprites])
        elif style == "icecrag_burst":
            self.magic_player.icecrag_burst(self.player, cost, [self.visible_sprites, self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None
    
    def destroy_tool(self):
        if self.current_tool:
            self.current_tool.kill()
        self.current_tool = None

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
        player_data['values']['souls'] += amount

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

    def use_item_effect(self, index):   #todo: change index system
        self.animation_player.create_particles("sparkle", self.player.rect.center + pygame.math.Vector2(0, -40), [self.visible_sprites], "item")

        if index == 0:  # Estus
            self.animation_player.create_particles("estus", self.player.rect.center + pygame.math.Vector2(-3, -30), [self.visible_sprites], "item")

    def kindle_bonfire_visuals(self, pos):
        self.animation_player.create_particles("estus", pos, [self.visible_sprites], "bonfire_effect")
        self.kindling_sound.play()

    def spawn_chest_item(self, id, pos):
        FloorItem(id, pos, [self.visible_sprites, self.interactable_sprites], True)
    
    def activated_lever_effect(self, id, pos):
        # todo: do an effect depending on the lever id
        print("Lever pulled!")
    
    def summon_sign_effect(self, covenant):
        # todo: effect
        print(f"{covenant} summon sign activated!")
    
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

    def restart_world(self, map = 0):
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
        if self.player.status == "dead":
            self.visible_sprites = YSortCameraGroup(map)
            self.screen_sprites = ScreenCameraGroup(map)
            self.create_map(True, map)
            # self.update_map(bloodstain_pos)
            restore_estus(self.player, 1)   # todo: use kindle level of last bonfire
        else:
            self.create_map(False, map) # todo: dont reset for sitting at bonfire
            # if self.bloodstain_present: self.update_map(self.current_bloodstain_pos)
    
    def load_new_region(self, region_id = "0"):
        # Removes all sprites
        for sprite_group in self.sprite_groups_list:
            for sprite in sprite_group:
                sprite.kill()
        # Loads new sprites and inits new background
        self.visible_sprites = YSortCameraGroup(region_id)
        self.screen_sprites = ScreenCameraGroup(region_id)
        self.create_map(True, region_id)
        self.map_id = region_id
    
    def update_dynamic_sprites(self):
        self.visible_sprites.enemy_update(self.player)
        self.visible_sprites.item_update(self.player)
        self.visible_sprites.chest_update(self.player)
        self.visible_sprites.lever_update(self.player)
        self.visible_sprites.message_update(self.player)
        self.visible_sprites.npc_update(self.player)
        self.visible_sprites.bonfire_update(self.player)
        self.visible_sprites.sign_update(self.player)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        if self.map_id != "0": self.ui.display(self.player)
        # self.boss.display(self.player)
        self.visible_sprites.update()
        self.screen_sprites.update()

        self.update_dynamic_sprites()
        
        # Testing
        # debug(f"Position: {self.player.rect.center} | Status: {self.player.status}")
        # debug(f"Displayed HP: {self.player.health_target} | Actual HP: {self.player.health} | Increased HP: {self.player.health_increase}")
        # debug(f"Index: {int(self.player.frame_index)}")
        # debug(f"{self.player.poise} / {self.player.max_poise}")
        # debug(self.displaying_message)
        #get_attribute_num("vitality")
        getSlotData(right_hand_data, weapon_data)
        getSlotData(left_hand_data, tool_data)

        self.bonfire.bonfire_popup_update(self.player)
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
            if self.hurtbox: self.hurtbox.collision_update(self.player, self.hurtbox)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, map_id):
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surface = pygame.image.load(f"assets/graphics/tilemap/ground_{map_id}.png").convert()
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

    def npc_update(self, player):
        npc_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "npc"]
        for npc in npc_sprites:
            npc.npc_update(player)
    
    def bonfire_update(self, player):
        bonfire_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "bonfire"]
        for bonfire in bonfire_sprites:
            bonfire.bonfire_update(player)

    def sign_update(self, player):
        sign_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "summon_sign"]
        for sign in sign_sprites:
            sign.sign_update(player)

class ScreenCameraGroup(pygame.sprite.Group):
    def __init__(self, map_id):
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surface = pygame.image.load(f"assets/graphics/tilemap/ground_{map_id}.png").convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))
    
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # floor_offset_pos = self.floor_rect.topleft - self.offset
        # self.display_surf