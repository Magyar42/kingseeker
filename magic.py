import pygame
from settings import *
from random import randint

class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player

        # sound
        self.sounds = {
            "heal": pygame.mixer.Sound("assets/audio/sfx/heal.wav"),
            "fire_surge": pygame.mixer.Sound("assets/audio/sfx/fire.wav"),
            "icecrag_burst": pygame.mixer.Sound("assets/audio/sfx/burst.wav"),
        }

    def heal(self, player, strength, cost, groups):
        if player.mana_target >= cost:

            spell_sfx = self.sounds["heal"]
            spell_sfx.set_volume(0.5)
            spell_sfx.play()

            player.health_increase += strength

            player.mana_target -= cost
            if player.health_increase >= player_data['dependent_variables']["health"]:
                player.health_increase = player_data['dependent_variables']["health"]

            self.animation_player.create_particles("aura", player.rect.center, groups, "self_spell")
            self.animation_player.create_particles("heal", player.rect.center + pygame.math.Vector2(0, -30), groups, "holy_spell")

    def fire_surge(self, player, cost, groups):
        if player.mana_target >= cost:

            spell_sfx = self.sounds["fire_surge"]
            spell_sfx.set_volume(0.3)
            spell_sfx.play()

            player.mana_target -= cost
            direction = player.status.split("_")[0]
            if direction == "right": direction_vector = pygame.math.Vector2(1, 0)
            elif direction == "left": direction_vector = pygame.math.Vector2(-1, 0)
            elif direction == "up": direction_vector = pygame.math.Vector2(0, -1)
            else: direction_vector = pygame.math.Vector2(0, 1)

            for i in range(1, 3):
                if direction_vector.x: # horizontal
                    offset_x = (direction_vector.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE // 4, TILESIZE // 4)
                    y = player.rect.centery + randint(-TILESIZE // 4, TILESIZE // 4)
                    self.animation_player.create_particles("fire_surge", (x, y), groups, "flame_spell", 0.35)
                else: # vertical
                    offset_y = (direction_vector.y * i) * TILESIZE
                    y = player.rect.centery + offset_y + randint(-TILESIZE // 4, TILESIZE // 4)
                    x = player.rect.centerx + randint(-TILESIZE // 4, TILESIZE // 4)
                    self.animation_player.create_particles("fire_surge", (x, y), groups, "flame_spell", 0.35)
    
    def icecrag_burst(self, player, cost, groups):
        if player.mana_target >= cost:

            spell_sfx = self.sounds["icecrag_burst"]
            spell_sfx.set_volume(0.2)
            spell_sfx.play()

            player.mana_target -= cost
            direction = player.status.split("_")[0]
            if direction == "right": direction_vector = pygame.math.Vector2(1, 0)
            elif direction == "left": direction_vector = pygame.math.Vector2(-1, 0)
            elif direction == "up": direction_vector = pygame.math.Vector2(0, -1)
            else: direction_vector = pygame.math.Vector2(0, 1)

            for i in range(1, 6):
                if direction_vector.x: # horizontal
                    offset_x = (direction_vector.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x
                    y = player.rect.centery
                    self.animation_player.create_particles("icecrag_burst", (x, y), groups, "ice_spell")
                else: # vertical
                    offset_y = (direction_vector.y * i) * TILESIZE
                    y = player.rect.centery + offset_y
                    x = player.rect.centerx
                    self.animation_player.create_particles("icecrag_burst", (x, y), groups, "ice_spell")