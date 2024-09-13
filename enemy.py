import pygame
from settings import *
from entity import Entity
from support import *
from bonfire import Bonfire

class Enemy(Entity):
    def __init__(self, enemy_name, pos, groups, obstacle_sprites, attackable_sprites, damage_player, trigger_death_particles, add_xp):
        super().__init__(groups)
        self.sprite_type = "enemy"
        self.animation_speed = 0.15

        self.import_graphics(enemy_name)
        self.status = "idle"
        # self.respawn_status = False
        self.image = self.animations[self.status][self.frame_index]

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites
        self.attackable_sprites = attackable_sprites

        # Enemy Stats
        self.enemy_name = enemy_name
        enemy_info = enemy_data[self.enemy_name]
        self.health = enemy_info['health']
        self.xp = enemy_info['xp']
        self.speed = enemy_info['speed']
        self.attack_damage = enemy_info['damage']
        self.resistance = enemy_info['resistance']
        self.attack_radius = enemy_info['attack_radius']
        self.notice_radius = enemy_info['notice_radius']
        self.attack_type = enemy_info['attack_type']

        # Player Interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 800
        self.damage_player = damage_player
        self.trigger_death_particles = trigger_death_particles
        self.add_xp = add_xp

        # I-Frame Timer
        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = 500
        self.dead = False

        # Sounds
        self.death_sound = pygame.mixer.Sound("assets/audio/sfx/death.wav")
        self.death_sound.set_volume(0.2)
        self.hit_sound = pygame.mixer.Sound("assets/audio/sfx/hit.wav")
        self.hit_sound.set_volume(0.15)
        self.attack_sound = pygame.mixer.Sound(enemy_info["attack_sound"])
        self.attack_sound.set_volume(0.2)

    
    def import_graphics(self, name):
        self.animations = {
            "idle": [],
            "move": [],
            "attack": [],
            "dead": [],
        }
        main_path = f"assets/graphics/enemy/{name}/"
        for animation in self.animations.keys():
            full_path = main_path + animation
            self.animations[animation] = import_folder(full_path)
    
    def get_player_dist_and_dir(self, player):
        enemy_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(player.rect.center)

        distance = (player_vector - enemy_vector).magnitude()
        if distance > 0:
            direction = (player_vector - enemy_vector).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)
    
    def get_status(self, player):
        distance = self.get_player_dist_and_dir(player)[0]

        if not self.dead:
            if player.dead:
                self.status = "idle"
            elif distance <= self.attack_radius and self.can_attack:
                if self.status != "attack":
                    self.frame_index = 0
                self.status = "attack"
            elif distance <= self.notice_radius:
                self.status = "move"
            else:
                self.status = "idle"

    def actions(self, player):
        if self.status == "attack":
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.attack_damage, self.attack_type)
            self.attack_sound.play()
        elif self.status == "move":
            self.direction = self.get_player_dist_and_dir(player)[1]
        else:
            self.direction = pygame.math.Vector2()
    
    def animate(self):
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index  >= len(animation):
            if self.status == "attack":
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if not self.vulnerable:
            # Flicker
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def cooldowns(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True
        
        if not self.vulnerable and not self.dead: # todo: dead
            current_time = pygame.time.get_ticks()
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True

    def get_damage(self, player, attack_type):
        if self.vulnerable:
            self.hit_sound.play()
            self.direction = self.get_player_dist_and_dir(player)[1]
            if attack_type == "weapon":
                self.health -= player.get_full_weapon_damage()
            elif attack_type == "tool":
                self.health -= player.get_full_tool_damage()
            else:
                self.health -= player.get_full_magic_damage()
            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False
    
    def check_death(self):
        if self.health <= 0 and not self.dead:
            self.kill()
            self.dead = True
            self.vulnerable = False
            self.status = "dead"

            self.trigger_death_particles(self.rect.center, self.enemy_name)
            self.add_xp(self.xp)
            self.death_sound.play()

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistance

    def update(self):
        self.hit_reaction()
        self.move(self.speed, self.sprite_type)
        self.animate()
        self.cooldowns()
        self.check_death()
    
    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)