import pygame
from settings import *
from support import *
from gameinfo import *
from popups import Prompt

class Bloodstain(pygame.sprite.Sprite):
    def __init__(self, pos, groups, check_souls_retrieval):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.sprite_type = "bloodstain"

        self.import_graphics("bloodstain")
        self.status = "idle"
        self.image = self.animations[self.status][self.frame_index]

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)

        self.use_radius = 100

        self.retrieving_souls = False
        self.retrieval_cooldown = 400
        self.retrieval_time = None

        self.check_souls_retrieval = check_souls_retrieval
        self.prompt = Prompt()

    def import_graphics(self, name):
        self.animations = {
            "idle": [],
            "retrieved": [],
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
        else:
            self.display_surface.blit(self.image, self.rect)

        self.image = animation[int(self.frame_index)]
        #self.rect = self.image.get_rect(center = self.hitbox.center)

    def get_player_dist(self, player):
        bloodstain_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(player.rect.center)

        distance = (player_vector - bloodstain_vector).magnitude()

        return distance
    
    def player_interact(self, player):
        player_distance = self.get_player_dist(player)
        if player_distance <= self.use_radius:
            self.prompt.createPrompt("Retrieval", "F", "Retrieve Souls")

            if not self.retrieving_souls:
                keys = pygame.key.get_pressed()

                if keys[pygame.K_f]:
                    self.status = "retrieved"
                    self.retrieval_effects(player)
                    self.kill()
    
    def retrieval_effects(self, player):
        self.retrieving_souls = True
        self.retrieval_time = pygame.time.get_ticks()

        player_data['values']['souls'] += player_data['values']['lost_souls']
        player_data['values']['humanity'] += player_data['values']['lost_humanity']
        self.check_souls_retrieval()

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.retrieving_souls:
            if current_time - self.retrieval_time >= self.retrieval_cooldown:
                self.retrieving_souls = False
    
    def update(self):
        self.animate()
        self.cooldowns()
    
    def bloodstain_update(self, player):
        self.player_interact(player)