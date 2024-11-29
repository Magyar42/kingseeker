import pygame
from settings import *

class Hurtboxes(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, width, height):
        super().__init__(groups)
        self.sprite_type = "attack"
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.transform.scale(pygame.image.load("assets/graphics/hitbox.png"), (width, height)).convert_alpha()
        #self.rect = self.image.get_rect(topleft = (100, 100))

        self.rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, self.rect)
    
    # def create_hurtboxes(self, x, y, width, height):
    #     self.rect = pygame.Rect(x, y, width, height)
    #     pygame.draw.rect(self.display_surface, UI_BG_COLOUR, self.rect)

# todo: could call class at level init and then call the above method to create hurtboxes

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = "weapon"
        direction = player.status.split("_")[0]

        full_path = f"assets/graphics/weapons/none/{direction}.png" #player.weapon
        self.image = pygame.image.load(full_path).convert_alpha()

        if direction == "right":
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0, 16))
        elif direction == "left":
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0, 16))
        elif direction == "up":
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-10, 0))
        elif direction == "down":
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10, 0))

class Catalyst(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = "catalyst"
        direction = player.status.split("_")[0]

        full_path = f"assets/graphics/weapons/{player.catalyst}/{direction}.png" 
        self.image = pygame.image.load(full_path).convert_alpha()

        if direction == "right":
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0, 16))
        elif direction == "left":
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0, 16))
        elif direction == "up":
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-10, 0))
        elif direction == "down":
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10, 0))