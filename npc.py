import pygame
from settings import *
from support import *
from gameinfo import *
from popups import Prompt, ItemPopup
from debug import debug
from random import choice

class NPC(pygame.sprite.Sprite):
    def __init__(self, npc_id, pos, groups, chamber_cleared, blit_reward_icon, map_id, effect = None, reward = "None", unique_id = None, rotate_val = 0):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.textfont = pygame.font.Font(UI_FONT, 16)
        self.frame_index = 0
        self.animation_speed = 0.10
        self.sprite_type = "npc"
        self.rotate_val = rotate_val

        self.map_id = map_id
        self.npc_id = npc_id
        self.unique_id = unique_id
        self.import_graphics()
        self.available_icon = pygame.transform.scale(pygame.image.load("assets/graphics/interactable_entities/npcs/available.png"), (8,39)).convert_alpha()
        self.image = pygame.transform.rotate(self.animations[self.npc_id][self.frame_index], self.rotate_val)

        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-30, -40)
        self.use_radius = 100
        self.chamber_cleared = chamber_cleared

        self.prompt = Prompt()
        self.item_popup = ItemPopup()

        self.interacting_npc = False
        self.interact_cooldown = 500
        self.interact_time = None

        self.click_time = None
        self.can_click = True
        self.current_prio = -1
        self.current_index = -1

        self.current_line_index = 0 # Current line spoken by the NPC, part of a list with all the lines of one conversation
        self.convo = None   
        self.talked_to = False  
        self.effect = effect  
        self.reward = reward
        self.blit_reward_icon = blit_reward_icon
        self.icon_blitted = False

        # self.chest_sound = pygame.mixer.Sound("assets/audio/sfx/OpenChest.wav")
        # self.chest_sound.set_volume(0.25)
    
    def import_graphics(self):
        self.animations = {
            "firekeeper": [],
            "crestfallen": [],
            "frampt": [],
            "andre": [],
            "patches": [],
            "petrus": [],
            "reah": [],
            "lautrec": [],
            "siegmeyer": [],
            "solaire": [],
            "ingward": [],
            "laurentius": [],
            "logan": [],
            "merchant": [],
            "kaathe": [],
            "domhnall": [],
            "knightess": [],
            "oscar": [],
            "quelana": [],
            "transition_prompt": [],
        }
        main_path = f"assets/graphics/interactable_entities/npcs/{self.npc_id}/"
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path, False)
    
    def animate(self):
        animation = self.animations[self.npc_id]
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        else:
            self.display_surface.blit(self.image, self.rect)

        self.image = pygame.transform.rotate(animation[int(self.frame_index)], self.rotate_val)
        #self.rect = self.image.get_rect(center = self.hitbox.center)

        # x = (self.display_surface.get_size()[0] // 2)
        # y = (self.display_surface.get_size()[1] // 2)
        # self.display_surface.blit(self.available_icon, (x, y))
    
    def get_player_dist(self, player):
        floor_item_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(player.rect.center)

        distance = (player_vector - floor_item_vector).magnitude()

        return distance

    def player_interact(self, player):
        player_distance = self.get_player_dist(player)
        if player_distance <= self.use_radius and not self.talked_to and self.chamber_cleared:
            # print(f"{round(player_distance)}m from {self.npc_id}!")
            if self.npc_id != "transition_prompt": self.prompt.createPrompt("NPC", "Q", "Talk")
            else:
                # for region in list(chambers_per_region.keys()):
                #     if self.map_id in chambers_per_region[region]:
                self.prompt.createPrompt("NPC", "Q", f"Continue ({self.reward})")

            if not self.interacting_npc:
                keys = pygame.key.get_pressed()

                if keys[pygame.K_q]:
                    if self.npc_id != "transition_prompt":
                        self.interacting_npc = True
                        self.initiate_npc(player)
                        # print(chest_list)
                        # self.chest_sound.play()
                        # self.status = "opening"
                        # print("opening")
                        # chest_list[self.chest_id] = 1
                        # Effects after opening (spawning item) done in self.animate
                        # due to only happening once chest opening animation played
                    else:
                        print(self.reward)
                        self.effect(self.reward, self.unique_id)

    def initiate_npc(self, player):
        if self.interacting_npc:
            self.interact_time = pygame.time.get_ticks()

            # todo: screen effect gfx

            player.resting = True
            player.npc_chatting = True
            self.current_prio = -1
            self.current_index = -1

            # Bring up UI and grab the npc name, icon and convo to use (done at self.interact_interface)
            # Each convo has a priority set - the one with the highest one is used, if available
            # Most have requirements to be available
            # If several available convos have the same priority, a random one is chosen between those

    def player_input(self, player):
        keys = pygame.key.get_pressed()

        if self.can_click:
            if keys[pygame.K_SPACE]:
                self.can_click = False
                self.click_time = pygame.time.get_ticks()

                # Continues to next line if able
                if self.current_line_index + 3 >= len(self.convo) - 1:
                    player.resting = False
                    player.npc_chatting = False

                    self.convo[2] = True # Marks last convo as done
                    self.talked_to = True
                    # self.current_prio = 0
                    # self.current_index = 0
                    self.current_line_index = 0
                else:
                    self.current_line_index += 1
    
    def interact_interface(self, player):
        if player.npc_chatting and self.get_player_dist(player) <= self.use_radius:
            if f'{self.npc_id}' in npc_conversations.keys():
                self.player_input(player)
                self.click_cooldown()

                bg_rect_size = (700, 150)
                name_rect_size = (370, 30)

                # x = (self.display_surface.get_size()[0] // 2) - (bg_rect_size[1])
                # y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2)

                name, self.convo = self.retrieve_conversation()
                debug(f"Prio: {self.current_prio} | Index: {self.current_index}")

                # BG
                menu_rect = pygame.Rect(290, 550, bg_rect_size[0], bg_rect_size[1])
                pygame.draw.rect(self.display_surface, UI_BG_COLOUR, menu_rect.inflate(10, 10))
                pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, menu_rect.inflate(10, 10), 5)

                # NPC Name
                name_rect = pygame.Rect(290, 515, name_rect_size[0], name_rect_size[1])
                pygame.draw.rect(self.display_surface, UI_BG_COLOUR, name_rect.inflate(10, 10))
                pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, name_rect.inflate(10, 10), 5)
                name_surf = self.font.render(name, False, "white")
                name_text_rect = name_surf.get_rect(midleft = name_rect.midleft + pygame.math.Vector2(10, 0))
                self.display_surface.blit(name_surf, name_text_rect)

                # Image
                npc_portrait = pygame.transform.scale(pygame.image.load(f"assets/graphics/ui/npc/{self.npc_id}.png"), (256, 256)).convert_alpha()
                portrait_rect = pygame.Rect(20, 444, 256, 256)
                pygame.draw.rect(self.display_surface, UI_BG_COLOUR, portrait_rect.inflate(10, 10))
                pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, portrait_rect.inflate(10, 10), 5)
                self.display_surface.blit(npc_portrait, portrait_rect)

                # Convo Body
                if self.current_line_index + 3 <= len(self.convo) - 1:
                    split_current_line = self.convo[self.current_line_index + 3].split("|")
                    while len(split_current_line) < 4:
                        split_current_line.append("")
                    
                    for subline in range(4):
                        text_surf = self.textfont.render(split_current_line[subline], False, "white")
                        text_rect = text_surf.get_rect(topleft = menu_rect.topleft + pygame.math.Vector2(20, 20 + (subline * 30)))
                        self.display_surface.blit(text_surf, text_rect)
            # else:
            #     player.resting = False
            #     player.npc_chatting = False
    
    def retrieve_conversation(self):
        # print(npc_conversations)
        current_npc = npc_conversations[f'{self.npc_id}']

        # Find the conversation with the highest priority (todo: add checks for the ones with requirements)
        for convo in current_npc:
            prio = int(convo[1])
            if prio > self.current_prio and not convo[2]:
                self.current_prio = prio
                self.current_index = current_npc.index(convo)

        # Get information to display
        chosen_convo = current_npc[self.current_index]
        display_name = chosen_convo[0]
        
        return display_name, chosen_convo
    
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.interacting_npc:
            if current_time - self.interact_time >= self.interact_cooldown:
                self.interacting_npc = False

    def click_cooldown(self):
        if not self.can_click:
            current_time = pygame.time.get_ticks()
            if current_time - self.click_time >= 200:
                self.can_click = True
    
    def draw_next_reward(self, reward, pos):
        if self.chamber_cleared:
            if self.npc_id == "transition_prompt":
                pos += pygame.math.Vector2(32, 32)
                self.blit_reward_icon(reward, pos)
    
    def update(self):
        self.animate()
        self.cooldowns()
        
        # Only trigger the effect ONCE
        # Once triggered, the TempIcon class will loop it
        if not self.icon_blitted:
            self.draw_next_reward(self.reward, self.pos)
            self.icon_blitted = True
    
    def npc_update(self, player, bool):
        self.player_interact(player)
        self.interact_interface(player)
        self.chamber_cleared = bool