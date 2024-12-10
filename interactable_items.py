import pygame
from settings import *
from support import *
from gameinfo import *
from popups import Prompt, ItemPopup
from debug import debug

# class FloorItem(pygame.sprite.Sprite):
#     def __init__(self, id, pos, groups, crop = False):    #check_item_retrieval
#         super().__init__(groups)
#         self.display_surface = pygame.display.get_surface()
#         self.frame_index = 0
#         self.animation_speed = 0.15
#         self.sprite_type = "floor_item"
#         self.crop = crop

#         if crop: self.import_graphics("chest_item")
#         else: self.import_graphics("floor_item")

#         self.status = "active"
#         self.image = self.animations[self.status][self.frame_index]

#         self.rect = self.image.get_rect(topleft = pos)
#         self.hitbox = self.rect.inflate(0, -10)
#         self.id = id
#         self.use_radius = 60

#         self.prompt = Prompt()
#         self.item_popup = ItemPopup()

#         self.retrieving_item = False
#         self.retrieval_cooldown = 500
#         self.retrieval_time = None

#         self.display_item_get = False
#         self.itemlist = []
#         self.numlist = []

#         self.pickup_sound = pygame.mixer.Sound("assets/audio/sfx/PickUpItem.wav")
#         self.pickup_sound.set_volume(0.25)

#     # def item_setup(self, id, pos, groups):
#     #     super().__init__(groups)
#     #     self.rect = self.image.get_rect(topleft = pos)
#     #     self.hitbox = self.rect.inflate(0, -10)
#     #     self.id = id

#     def import_graphics(self, name):
#         self.animations = {
#             "active": [],
#             "inactive": [],
#         }
#         main_path = f"assets/graphics/interactable_entities/{name}/"
#         for animation in self.animations.keys():
#             full_path = main_path + animation
#             self.animations[animation] = import_folder(full_path)

#     def animate(self):
#         animation = self.animations[self.status]
        
#         self.frame_index += self.animation_speed
#         if self.frame_index  >= len(animation):
#             self.frame_index = 0
#         else:
#             self.display_surface.blit(self.image, self.rect)

#         self.image = animation[int(self.frame_index)]
#         #self.rect = self.image.get_rect(center = self.hitbox.center)

#     def get_player_dist(self, player):
#         floor_item_vector = pygame.math.Vector2(self.rect.center)
#         player_vector = pygame.math.Vector2(player.rect.center)

#         distance = (player_vector - floor_item_vector).magnitude()

#         return distance
    
#     def player_interact(self, player):
#         player_distance = self.get_player_dist(player)
#         if player_distance <= self.use_radius and self.status == "active":
#             self.prompt.createPrompt("Item Pickup", "F", "Pick up item")

#             if not self.retrieving_item:
#                 keys = pygame.key.get_pressed()

#                 if keys[pygame.K_q]:
#                     self.pickup_sound.play()
#                     self.status = "inactive"
#                     self.retrieval_effects(player)
#                     #self.kill()
                    
#                     # Give items
#                     self.itemlist = []
#                     self.numlist = []
#                     for items in ground_item_list[self.id]:
#                         if ground_item_list[self.id].index(items) != 0:
#                             if ground_item_list[self.id].index(items) % 2 == 0:
#                                 self.numlist.append(items)
#                             else:
#                                 self.itemlist.append(items)
                    
#                     print(f"{self.itemlist} {self.numlist}")
#                     for i in range(len(self.itemlist)):
#                         item_category = game_items[self.itemlist[i]]["category"]

#                         if self.itemlist[i] in player_inventory[item_category]:
#                             item_index = player_inventory[item_category].index(self.itemlist[i])
#                             player_inventory[f"{item_category}_num"][item_index] += self.numlist[i]
#                         else:
#                             player_inventory[item_category].append(self.itemlist[i])
#                             player_inventory[f"{item_category}_num"].append(self.numlist[i])

#                     self.display_item_get = True

#                     player.reset_display = True
#                     ground_item_list[self.id][0] = 1
#                     player.reset_qitems_display()

#     def display_item_popup(self, player):
#         for i in range(len(self.itemlist)):
#             self.item_popup.createPrompt("Item Popup", "F", self.itemlist[i], self.numlist[i], i+1)
        
#         # check for player input of Q, if so then set bool to false
#         self.prompt.createPrompt("Remove Popup", "F", "OK")

#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_q] and not self.retrieving_item:
#             self.display_item_get = False
    
#     def retrieval_effects(self, player):
#         self.retrieving_item = True
#         self.retrieval_time = pygame.time.get_ticks()
#         print("item pickup")

#     def cooldowns(self):
#         current_time = pygame.time.get_ticks()

#         if self.retrieving_item:
#             if current_time - self.retrieval_time >= self.retrieval_cooldown:
#                 self.retrieving_item = False
    
#     def update(self):
#         self.animate()
#         self.cooldowns()
    
#     def ground_items_update(self, player):
#         self.player_interact(player)

#         if self.display_item_get:
#             self.display_item_popup(player)

# class Chest(pygame.sprite.Sprite):
#     def __init__(self, chest_id, item_id, pos, groups, spawn_chest_item, opened = True):
#         super().__init__(groups)
#         self.spawn_chest_item = spawn_chest_item
#         self.display_surface = pygame.display.get_surface()
#         self.frame_index = 0
#         self.animation_speed = 0.15
#         self.sprite_type = "chest"

#         self.import_graphics("chest1")
#         if opened: self.status = "open"
#         else: self.status = "closed"
#         self.image = self.animations[self.status][self.frame_index]

#         self.pos = pos
#         self.rect = self.image.get_rect(topleft = pos)
#         self.hitbox = self.rect.inflate(-30, -40)
#         self.item_id = item_id
#         self.chest_id = chest_id
#         self.use_radius = 100

#         self.prompt = Prompt()
#         self.item_popup = ItemPopup()

#         self.opening_chest = False
#         self.open_cooldown = 500
#         self.open_time = None

#         self.chest_sound = pygame.mixer.Sound("assets/audio/sfx/OpenChest.wav")
#         self.chest_sound.set_volume(0.25)
    
#     def import_graphics(self, name):
#         self.animations = {
#             "open": [],
#             "closed": [],
#             "opening": [],
#         }
#         main_path = f"assets/graphics/interactable_entities/{name}/"
#         for animation in self.animations.keys():
#             full_path = main_path + animation
#             self.animations[animation] = import_folder(full_path, True, (64, 64))

#     def animate(self):
#         animation = self.animations[self.status]
        
#         self.frame_index += self.animation_speed
#         if self.frame_index  >= len(animation):
#             # Keep open after opening animation plays
#             if self.status == "opening":
#                 self.status = "open"
#                 self.spawn_item()
#                 self.frame_index = 6
#             else:
#                 self.frame_index = 0
#         else:
#             self.display_surface.blit(self.image, self.rect)

#         self.image = animation[int(self.frame_index)]
#         #self.rect = self.image.get_rect(center = self.hitbox.center)

#     def get_player_dist(self, player):
#         floor_item_vector = pygame.math.Vector2(self.rect.center)
#         player_vector = pygame.math.Vector2(player.rect.center)

#         distance = (player_vector - floor_item_vector).magnitude()

#         return distance
    
#     def spawn_item(self):
#         # todo: call upon this function for each chest item upon resetting map (as long as item isn't picked up)
#         # or maybe close the relevant chest? would be easier and more obvious that an item was missed
#         self.spawn_chest_item(self.item_id, self.pos + pygame.math.Vector2(self.rect.w // 2 - 7, 5))

#     def player_interact(self, player):
#         player_distance = self.get_player_dist(player)
#         if player_distance <= self.use_radius and self.status == "closed":
#             self.prompt.createPrompt("Chest", "F", "Open chest")

#             if not self.opening_chest:
#                 keys = pygame.key.get_pressed()

#                 if keys[pygame.K_q]:
#                     print(chest_list)
#                     self.chest_sound.play()
#                     self.status = "opening"
#                     print("opening")
#                     chest_list[self.chest_id] = 1
#                     # Effects after opening (spawning item) done in self.animate
#                     # due to only happening once chest opening animation played

#     def cooldowns(self):
#         current_time = pygame.time.get_ticks()

#         if self.opening_chest:
#             if current_time - self.open_time >= self.open_cooldown:
#                 self.opening_chest = False
    
#     def update(self):
#         self.animate()
#         self.cooldowns()
    
#     def chest_update(self, player):
#         self.player_interact(player)

# class Lever(pygame.sprite.Sprite):
#     def __init__(self, lever_id, pos, groups, activated_lever_effect, activated = True):
#         super().__init__(groups)
#         self.activated_lever_effect = activated_lever_effect
#         self.display_surface = pygame.display.get_surface()
#         self.frame_index = 0
#         self.animation_speed = 0.10
#         self.sprite_type = "lever"

#         self.import_graphics("lever")
#         if activated: self.status = "active"
#         else: self.status = "inactive"
#         self.image = self.animations[self.status][self.frame_index]

#         self.pos = pos
#         self.rect = self.image.get_rect(topleft = pos)
#         self.hitbox = self.rect.inflate(-30, -40)
#         self.lever_id = lever_id
#         self.use_radius = 100

#         self.prompt = Prompt()
#         self.item_popup = ItemPopup()

#         self.activating_lever = False
#         self.lever_cooldown = 500
#         self.lever_pull_time = None

#         self.lever_sound = pygame.mixer.Sound("assets/audio/sfx/pull_lever.wav")
#         self.lever_sound.set_volume(0.25)
    
#     def import_graphics(self, name):
#         self.animations = {
#             "active": [],
#             "inactive": [],
#             "activating": [],
#         }
#         main_path = f"assets/graphics/interactable_entities/{name}/"
#         for animation in self.animations.keys():
#             full_path = main_path + animation
#             self.animations[animation] = import_folder(full_path, True, (69, 44))

#     def animate(self):
#         animation = self.animations[self.status]
        
#         self.frame_index += self.animation_speed
#         if self.frame_index  >= len(animation):
#             # Keep open after opening animation plays
#             if self.status == "activating":
#                 self.status = "active"
#                 self.lever_activation()
#                 self.frame_index = 6
#             else:
#                 self.frame_index = 0
#         else:
#             self.display_surface.blit(self.image, self.rect)

#         self.image = animation[int(self.frame_index)]
#         #self.rect = self.image.get_rect(center = self.hitbox.center)

#     def lever_activation(self):
#         self.activated_lever_effect(self.lever_id, self.pos)

#     def get_player_dist(self, player):
#         floor_item_vector = pygame.math.Vector2(self.rect.center)
#         player_vector = pygame.math.Vector2(player.rect.center)

#         distance = (player_vector - floor_item_vector).magnitude()

#         return distance

#     def player_interact(self, player):
#         player_distance = self.get_player_dist(player)
#         if player_distance <= self.use_radius and self.status == "inactive":
#             self.prompt.createPrompt("Lever", "F", "Pull lever")

#             if not self.activating_lever:
#                 keys = pygame.key.get_pressed()

#                 if keys[pygame.K_q]:
#                     self.lever_sound.play()
#                     self.status = "activating"
#                     lever_list[self.lever_id] = 1

#     def cooldowns(self):
#         current_time = pygame.time.get_ticks()

#         if self.activating_lever:
#             if current_time - self.lever_pull_time >= self.lever_cooldown:
#                 self.activating_lever = False
    
#     def update(self):
#         self.animate()
#         self.cooldowns()
    
#     def lever_update(self, player):
#         self.player_interact(player)

# class Message(pygame.sprite.Sprite):
    # def __init__(self, message_id, pos, groups, activated_message_effect):
    #     super().__init__(groups)
    #     self.activated_message_effect = activated_message_effect
    #     self.display_surface = pygame.display.get_surface()
    #     self.frame_index = 0
    #     self.animation_speed = 0.10
    #     self.sprite_type = "message"

    #     self.import_graphics("message")
    #     self.status = "idle"
    #     self.image = self.animations[self.status][self.frame_index]

    #     self.pos = pos
    #     self.rect = self.image.get_rect(topleft = pos)
    #     self.hitbox = self.rect.inflate(-20, -20)
    #     self.hitbox.y -= 15
    #     self.message_id = message_id
    #     self.use_radius = 100

    #     self.prompt = Prompt()
    #     self.item_popup = ItemPopup()

    #     self.activating_message = False
    #     self.message_cooldown = 500
    #     self.message_pull_time = None

    #     self.message_sound = pygame.mixer.Sound("assets/audio/sfx/CURSOL_OK.wav")
    #     self.message_sound.set_volume(0.25)
    
    # def import_graphics(self, name):
    #     self.animations = {
    #         "active": [],
    #         "idle": [],
    #     }
    #     main_path = f"assets/graphics/interactable_entities/{name}/"
    #     for animation in self.animations.keys():
    #         full_path = main_path + animation
    #         self.animations[animation] = import_folder(full_path, True, (90, 45))

    # def animate(self):
    #     animation = self.animations[self.status]
        
    #     self.frame_index += self.animation_speed
    #     if self.frame_index  >= len(animation):
    #         self.frame_index = 0
    #     else:
    #         self.display_surface.blit(self.image, self.rect)

    #     self.image = animation[int(self.frame_index)]
    #     #self.rect = self.image.get_rect(center = self.hitbox.center)

    # def message_activation(self):
    #     self.activated_message_effect(self.message_id, self.pos)

    # def get_player_dist(self, player):
    #     floor_item_vector = pygame.math.Vector2(self.rect.center)
    #     player_vector = pygame.math.Vector2(player.rect.center)

    #     distance = (player_vector - floor_item_vector).magnitude()

    #     return distance

    # def player_interact(self, player):
    #     player_distance = self.get_player_dist(player)
    #     if player_distance <= self.use_radius and self.status == "idle":
    #         self.prompt.createPrompt("Message", "F", "Read message")

    #         if not self.activating_message:
    #             keys = pygame.key.get_pressed()

    #             if keys[pygame.K_q]:
    #                 self.message_activation()
    #                 self.message_sound.play()
    #                 self.status = "active"
    #     if player_distance <= self.use_radius and self.status == "active":
    #         keys = pygame.key.get_pressed()

    #         if keys[pygame.K_SPACE]:
    #             self.message_activation()
    #             self.status = "idle"

    # def cooldowns(self):
    #     current_time = pygame.time.get_ticks()

    #     if self.activating_message:
    #         if current_time - self.message_pull_time >= self.message_cooldown:
    #             self.activating_message = False
    
    # def update(self):
    #     self.animate()
    #     self.cooldowns()
    
    # def message_update(self, player):
    #     self.player_interact(player)

class SummonSign(pygame.sprite.Sprite):
    def __init__(self, covenant, pos, groups, interact_effect):
        super().__init__(groups)
        self.interact_effect = interact_effect
        self.display_surface = pygame.display.get_surface()
        self.frame_index = 0
        self.animation_speed = 0.09
        self.sprite_type = "summon_sign"
        self.covenant = covenant

        self.import_graphics(f"summon_signs/{self.covenant}")
        self.status = "idle"
        self.image = self.animations[self.status][self.frame_index]

        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-30, -40)
        self.use_radius = 100

        self.prompt = Prompt()
        self.item_popup = ItemPopup()

        self.opening_sign = False
        self.open_cooldown = 500
        self.open_time = None

        self.sign_sound = pygame.mixer.Sound("assets/audio/sfx/ghost.wav")
        self.sign_sound.set_volume(0.25)
    
    def import_graphics(self, name):
        self.animations = {
            "idle": [],
            "active": [],
            "activating": [],
        }
        main_path = f"assets/graphics/interactable_entities/{name}/"
        for animation in self.animations.keys():
            full_path = main_path + animation
            self.animations[animation] = import_folder(full_path, True, (64, 64))

    def animate(self):
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index  >= len(animation):
            # Keep open after opening animation plays
            if self.status == "activating":
                self.status = "active"
                self.summon_sign_ui_effect()
                self.frame_index = len(animation) - 1
            else:
                self.frame_index = 0
        else:
            self.display_surface.blit(self.image, self.rect)

        self.image = animation[int(self.frame_index)]
        #self.rect = self.image.get_rect(center = self.hitbox.center)

    def get_player_dist(self, player):
        floor_item_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(player.rect.center)

        distance = (player_vector - floor_item_vector).magnitude()

        return distance
    
    def summon_sign_ui_effect(self):
        self.interact_effect(self.covenant)

    def player_interact(self, player):
        player_distance = self.get_player_dist(player)
        if player_distance <= self.use_radius and self.status == "idle":
            self.prompt.createPrompt("Summon Sign", "F", "Activate Summon Sign")

            if not self.opening_sign:
                keys = pygame.key.get_pressed()

                if keys[pygame.K_f]:
                    self.sign_sound.play()
                    self.status = "activating"

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.opening_sign:
            if current_time - self.open_time >= self.open_cooldown:
                self.opening_sign = False
    
    def update(self):
        self.animate()
        self.cooldowns()
    
    def sign_update(self, player):
        self.player_interact(player)

class PerkPillar(pygame.sprite.Sprite):
    def __init__(self, pillar_type, pos, groups, interact_effect, check_status):
        super().__init__(groups)
        self.interact_effect = interact_effect
        self.check_status = check_status
        self.display_surface = pygame.display.get_surface()
        self.frame_index = 0
        self.animation_speed = 0.20
        self.sprite_type = "pillar"
        self.type = pillar_type

        self.import_graphics("perk_pillar")
        self.status = "idle"
        self.new_status = "idle"
        self.image = self.animations[self.status][self.frame_index]

        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-30, -40)
        self.use_radius = 150

        self.prompt = Prompt()
        self.item_popup = ItemPopup()

        self.opening_sign = False
        self.open_cooldown = 500
        self.open_time = None

        self.sign_sound = pygame.mixer.Sound("assets/audio/sfx/ghost.wav")
        self.sign_sound.set_volume(0.25)
    
    def import_graphics(self, name):
        self.animations = {
            "idle": [],
            "active": [],
            "activating": [],
        }
        main_path = f"assets/graphics/interactable_entities/{name}/"
        for animation in self.animations.keys():
            full_path = main_path + animation
            self.animations[animation] = import_folder(full_path, True, (65, 165))

    def animate(self):
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index  >= len(animation):
            # Keep open after opening animation plays
            if self.status == "activating":
                self.status = "active"
                self.pillar_ui_effect()
                self.frame_index = len(animation) - 1
            else:
                self.frame_index = 0
        else:
            self.display_surface.blit(self.image, self.rect)

        self.image = animation[int(self.frame_index)]

    def get_player_dist(self, player):
        floor_item_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(player.rect.center)

        distance = (player_vector - floor_item_vector).magnitude()

        return distance
    
    def pillar_ui_effect(self):
        self.interact_effect(self.type)

    def player_interact(self, player):
        player_distance = self.get_player_dist(player)
        if player_distance <= self.use_radius and self.status == "idle":
            match self.type:
                case "perks": display_string = "View Gifts of Humanity"
                case "levels": display_string = "Strengthen Attributes"
                case "bonfire": display_string = "Rest at Bonfire"
                case "weapons": display_string = "Switch Weapons"
                case "anvil": display_string = "Improve Weapons"
            self.prompt.createPrompt("Summon Sign", "F", f"{display_string}")

            if not self.opening_sign:
                keys = pygame.key.get_pressed()

                if keys[pygame.K_f]:
                    self.sign_sound.play()
                    self.status = "activating"

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.opening_sign:
            if current_time - self.open_time >= self.open_cooldown:
                self.opening_sign = False
    
    def update(self):
        self.animate()
        self.cooldowns()
        self.new_status = self.check_status(self.type)

        # Only set status when already active; otherwise, the status will be
        # constantly set to idle, as the interface is not active
        if self.status == "active": self.status = self.new_status
    
    def pillar_update(self, player):
        self.player_interact(player)