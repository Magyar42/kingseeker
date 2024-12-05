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
        self.current_prio = 0
        self.current_index = 0

        self.current_line_index = 0 # Current line spoken by the NPC, part of a list with all the lines of one conversation
        self.convo = None   
        self.convo_text_list = []
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

            if self.npc_id != "transition_prompt": self.prompt.createPrompt("NPC", "Q", "Talk")
            else: self.prompt.createPrompt("NPC", "Q", "Continue")

            if not self.interacting_npc:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    if self.npc_id != "transition_prompt":
                        self.interacting_npc = True
                        self.initiate_npc(player)
                    else:
                        self.effect(self.reward, self.unique_id)

    def initiate_npc(self, player):
        if self.interacting_npc:
            self.interact_time = pygame.time.get_ticks()

            player.resting = True
            player.npc_chatting = True
            self.current_prio = 0
            self.current_index = 0

            # Bring up UI and grab the npc name, icon and convo to use (done at self.interact_interface)
            # Each convo has a priority set - the one with the highest one is used, if available
            # Most have requirements to be available

    def player_input(self, player):
        keys = pygame.key.get_pressed()

        if self.can_click:
            if keys[pygame.K_SPACE]:
                self.can_click = False
                self.click_time = pygame.time.get_ticks()

                self.current_line_index += 1
    
    def interact_interface(self, player):
        if self.get_player_dist(player) <= self.use_radius:
            if f'{self.npc_id}' in npc_conversations.keys():
                name, self.convo = self.retrieve_conversation()
                self.convo_text_list = self.convo["text"]
                # debug(f"Prio: {self.current_prio} | Index: {self.current_index}")

                # End dialogue if needed
                if self.current_line_index >= len(self.convo_text_list) - 1:
                    player.resting = False
                    player.npc_chatting = False

                    self.talked_to = True
                    self.current_line_index = 0

                    self.convo["completed"] = True # Marks last convo as done
                else:
                    self.player_input(player)
                    self.click_cooldown()

                    bg_rect_size = (800, 140)
                    x = 50
                    y = (self.display_surface.get_size()[1] // 2) - (bg_rect_size[1] // 2) + 250
                    main_rect = pygame.Rect(x, y, bg_rect_size[0], bg_rect_size[1])
                    text_rect_pos = main_rect.topleft + pygame.math.Vector2(135, 60)
                    text_rect_size = (bg_rect_size[0] - 20 - 20 - 100 - 15, bg_rect_size[1] - 50 - 10 - 20)

                    createUI(self.display_surface, bg_rect_size[0], bg_rect_size[1], (x, y), "dark")
                    createUI(self.display_surface, text_rect_size[0], text_rect_size[1], text_rect_pos, "basic")

                    # NPC Name
                    title_surface = pygame.font.Font(UI_FONT, 16).render(f"| {name.upper()}", True, TEXT_TITLE_COLOUR)
                    title_rect = title_surface.get_rect(midleft = main_rect.topleft + pygame.math.Vector2(120, 20))
                    self.display_surface.blit(title_surface, title_rect)

                    # Image    
                    icon_surface = pygame.image.load(f"assets/graphics/ui/npc/{self.npc_id}.png").convert_alpha()
                    icon_rect = icon_surface.get_rect(midleft = main_rect.midleft + pygame.math.Vector2(15, 0))

                    createUI(self.display_surface, 56, 56, (icon_rect.topleft[0] + 10, icon_rect.topleft[1] + 10), "basic")
                    self.display_surface.blit(icon_surface, icon_rect)

                    # Convo Body
                    # if self.current_line_index + 3 <= len(self.convo) - 1:
                    #     split_current_line = self.convo[self.current_line_index + 3].split("|")
                    #     while len(split_current_line) < 4:
                    #         split_current_line.append("")
                        
                    #     for subline in range(4):
                    #         text_surf = pygame.font.Font(UI_FONT, 12).render(split_current_line[subline], False, UI_BG_COLOUR)
                    #         text_rect = text_surf.get_rect(topleft = text_rect_pos + pygame.math.Vector2(0, (subline * 15)))
                    #         self.display_surface.blit(text_surf, text_rect)
                    
                    split_current_line = self.convo_text_list[self.current_line_index].split("|")
                    
                    while len(split_current_line) < 4: split_current_line.append("")
                        
                    for subline in range(4):
                        text_surf = pygame.font.Font(UI_FONT, 12).render(split_current_line[subline], False, UI_BG_COLOUR)
                        text_rect = text_surf.get_rect(topleft = text_rect_pos + pygame.math.Vector2(0, (subline * 15)))
                        self.display_surface.blit(text_surf, text_rect)
    
    def retrieve_conversation(self):
        current_npc = npc_conversations[f'{self.npc_id}']

        # Find available convos
        available_convos = []
        for convo in current_npc:
            if not current_npc[convo]["completed"]: available_convos.append(convo)
            
        # Choose convo with highest priority (todo: add checks for the ones with requirements)
        self.current_prio = 0
        self.current_index = "000"
        for convo in available_convos:
            if current_npc[convo]["priority"] > self.current_prio:
                self.current_prio = current_npc[convo]["priority"]
                self.current_index = convo

            # # Find the conversation with the highest priority (todo: add checks for the ones with requirements)
            # for convo in current_npc:
            #     prio = int(convo[1])
            #     if prio > self.current_prio and not convo[2]:
            #         self.current_prio = prio
            #         self.current_index = current_npc.index(convo)

         # Get information to display
        chosen_convo = current_npc[self.current_index]
        display_name = chosen_convo["name"]
            
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
        if self.npc_id == "transition_prompt":
            pos += pygame.math.Vector2(32, 32)
            self.blit_reward_icon(reward, pos)
        else:
            if not self.talked_to:
                pos += pygame.math.Vector2(32, -20)
                self.blit_reward_icon("available_icon", pos, True)
    
    def update(self):
        self.animate()
        self.cooldowns()
        
        # Only trigger the effect ONCE
        # Once triggered, the TempIcon class will loop it
        if self.chamber_cleared:
            if not self.icon_blitted:
                self.draw_next_reward(self.reward, self.pos)
                self.icon_blitted = True
        if self.npc_id != "transition_prompt": self.draw_next_reward("available_icon", self.pos)
    
    def npc_update(self, player, bool):
        self.player_interact(player)
        if player.npc_chatting: self.interact_interface(player)
        self.chamber_cleared = bool