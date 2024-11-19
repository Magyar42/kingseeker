import pygame
from math import sin
from debug import debug

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()
    
    def move(self, speed, sprite_type):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal", sprite_type)
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical", sprite_type)

        self.rect.center = self.hitbox.center

    def collision(self, direction, sprite_type):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        elif direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
    
    def enemy_collision(self, direction, sprite_group):
        pass 
        # problem is that player to enemy collision is only detected when player has a direction
        # which means they must be moving. even if we detect collision when the player is static
        # we cannot plausibly work out what to do, as in which direction to move the player.
        # as such, it would be best to also implement enemy to player collision, so as to 
        # prevent both the enemies from colliding with the player and stop the player from being
        # pushed around, causing a bunch of jumps in the player rect.

        # if direction == "horizontal":
        #     for sprite in sprite_group:
        #         if sprite.hitbox.colliderect(self.hitbox):
        #             print("x collision")
        #             if self.direction.x > 0:
        #                 self.hitbox.right = sprite.hitbox.left
        #             if self.direction.x < 0:
        #                 self.hitbox.left = sprite.hitbox.right
        # elif direction == "vertical":
        #     for sprite in sprite_group:
        #         if sprite.hitbox.colliderect(self.hitbox):
        #             print("y collision")
        #             if self.direction.y > 0:
        #                 self.hitbox.bottom = sprite.hitbox.top
        #             if self.direction.y < 0:
        #                 self.hitbox.top = sprite.hitbox.bottom
    
    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0