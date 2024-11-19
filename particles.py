import pygame
from support import import_folder
from random import choice

class AnimationPlayer():
    def __init__(self):
        # Particle Dictionary
        self.frames = {
            # Main Menu
            'mm_bonfire': import_folder('assets/graphics/menu_animations/mainmenu_bonfire'),

            # magic
            'fire_surge': import_folder('assets/graphics/particles/magic/fire_surge/frames'),
            'aura': import_folder('assets/graphics/particles/aura'),
            'heal': import_folder('assets/graphics/particles/magic/heal/frames'),
            'icecrag_burst': import_folder('assets/graphics/particles/magic/icecrag_burst/frames'),
            
            # attacks 
            'claw': import_folder('assets/graphics/particles/claw'),
            'slash': import_folder('assets/graphics/particles/slash'),
            'sparkle': import_folder('assets/graphics/particles/sparkle'),
            'leaf_attack': import_folder('assets/graphics/particles/leaf_attack'),
            'thunder': import_folder('assets/graphics/particles/thunder'),
            'sparkle': import_folder('assets/graphics/particles/sparkle'),
 
            # deaths
            'squid': import_folder('assets/graphics/particles/smoke'),
            'raccoon': import_folder('assets/graphics/particles/smoke'),
            'spirit': import_folder('assets/graphics/particles/smoke'),
            'bamboo': import_folder('assets/graphics/particles/smoke'),
            'asylum_demon': import_folder('assets/graphics/particles/smoke'),

            'player': import_folder('assets/graphics/particles/smoke2'),

            # spawning
            'enemy_spawn': import_folder('assets/graphics/particles/enemy_spawn'),
            'enemy_spawn2': import_folder('assets/graphics/particles/enemy_spawn2'),
            'item_spawn': import_folder('assets/graphics/particles/spawn'),
            'nova': import_folder('assets/graphics/particles/nova'),

            # leafs 
            'leaf': (
                import_folder('assets/graphics/particles/leaf1'),
                import_folder('assets/graphics/particles/leaf2'),
                import_folder('assets/graphics/particles/leaf3'),
                import_folder('assets/graphics/particles/leaf4'),
                import_folder('assets/graphics/particles/leaf5'),
                import_folder('assets/graphics/particles/leaf6'),
                self.reflect_images(import_folder('assets/graphics/particles/leaf1')),
                self.reflect_images(import_folder('assets/graphics/particles/leaf2')),
                self.reflect_images(import_folder('assets/graphics/particles/leaf3')),
                self.reflect_images(import_folder('assets/graphics/particles/leaf4')),
                self.reflect_images(import_folder('assets/graphics/particles/leaf5')),
                self.reflect_images(import_folder('assets/graphics/particles/leaf6'))
            ),

            # overlays
            'death': import_folder('assets/overlay/death'),
            'bonfire_lit': import_folder('assets/overlay/bonfire_lit'),
            'humanity_restored': import_folder('assets/overlay/humanity_restored'),
            'retrieval': import_folder('assets/overlay/retrieval'),
            'target_destroyed': import_folder('assets/overlay/target_destroyed'),
            'victory_achieved': import_folder('assets/overlay/victory_achieved'),

            # region titles
            'firelink_shrine': import_folder('assets/overlay/regions/firelink_shrine'),
            'undead_burg': import_folder('assets/overlay/regions/undead_burg'),
            'undead_parish': import_folder('assets/overlay/regions/undead_parish'),
            'the_depths': import_folder('assets/overlay/regions/the_depths'),

            # screen effects
            'fire1': import_folder('assets/graphics/ui/screen_effects/fire1'),
            'fire2': import_folder('assets/graphics/ui/screen_effects/fire2'),
            'fire3': import_folder('assets/graphics/ui/screen_effects/fire3'),

            # items
            'estus': import_folder('assets/graphics/particles/estus'),

            # reward icons
            'great_soul': import_folder('assets/graphics/ui/rewards/great_soul'),
            'humanity': import_folder('assets/graphics/ui/rewards/humanity'),
            'titanite_shard': import_folder('assets/graphics/ui/rewards/titanite_shard'),
            'titanite_chunk': import_folder('assets/graphics/ui/rewards/titanite_chunk'),
            'titanite_slab': import_folder('assets/graphics/ui/rewards/titanite_slab'),
            'demon_titanite': import_folder('assets/graphics/ui/rewards/demon_titanite'),
            'sunlight_medal': import_folder('assets/graphics/ui/rewards/sunlight_medal'),
            'souvenir_of_reprisal': import_folder('assets/graphics/ui/rewards/souvenir_of_reprisal'),
            'sunlight_summon': import_folder('assets/graphics/ui/rewards/sunlight_summon'),
            'chaos_summon': import_folder('assets/graphics/ui/rewards/chaos_summon'),
            'darkwraith_summon': import_folder('assets/graphics/ui/rewards/darkwraith_summon'),
            'darkmoon_summon': import_folder('assets/graphics/ui/rewards/darkmoon_summon'),
            'velkas_tome': import_folder('assets/graphics/ui/rewards/velkas_tome'),
            'vendor': import_folder('assets/graphics/ui/rewards/vendor'),

            # Asylum Demon
            # todo!!! ADD ACTUAL SPRITES AND FRAMES TO EACH ATTACK AND BLANK THE NONATTACKS! THANKL YOUY BABYE
            'down_idle': import_folder('assets/graphics/particles/slash'),
            'down_move': import_folder('assets/graphics/particles/slash'),
            'down_swing': import_folder('assets/graphics/particles/slash'),
            'down_slam': import_folder('assets/graphics/particles/slash'),
            'down_swing_down': import_folder('assets/graphics/particles/slash'),
            'down_fly': import_folder('assets/graphics/particles/slash'),

            'right_idle': import_folder('assets/graphics/particles/slash'),
            'right_move': import_folder('assets/graphics/particles/slash'),
            'right_swing': import_folder('assets/graphics/particles/slash'),
            'right_slam': import_folder('assets/graphics/particles/slash'),
            'right_swing_down': import_folder('assets/graphics/particles/slash'),
            'right_fly': import_folder('assets/graphics/particles/slash'),

            'up_idle': import_folder('assets/graphics/particles/slash'),
            'up_move': import_folder('assets/graphics/particles/slash'),
            'up_swing': import_folder('assets/graphics/particles/slash'),
            'up_slam': import_folder('assets/graphics/particles/slash'),
            'up_swing_down': import_folder('assets/graphics/particles/slash'),
            'up_fly': import_folder('assets/graphics/particles/slash'),

            'left_idle': import_folder('assets/graphics/particles/slash'),
            'left_move': import_folder('assets/graphics/particles/slash'),
            'left_swing': import_folder('assets/graphics/particles/slash'),
            'left_slam': import_folder('assets/graphics/particles/slash'),
            'left_swing_down': import_folder('assets/graphics/particles/slash'),
            'left_fly': import_folder('assets/graphics/particles/slash'),
        }

    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames
    
    def create_grass_particles(self, pos, groups, sprite_type):
        animation_frames = choice(self.frames["leaf"])
        ParticleEffect(pos, animation_frames, groups, sprite_type)
    
    def create_particles(self, animation_type, pos, groups, sprite_type, speed=0.15, effect=None):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups, sprite_type, speed, effect)
    
    def create_icon(self, animation_type, pos, groups, sprite_type, speed=0.15):
        animation_frames = self.frames[animation_type]
        TempIcon(pos, animation_frames, groups, sprite_type, speed)
    
    def create_macro(self, animation_type, pos, groups, effect, speed, remain_time, toggle_screen_effect):
        animation_frames = self.frames[animation_type]
        ScreenEffect(pos, animation_frames, groups, effect, speed, remain_time, toggle_screen_effect)

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups, sprite_type, speed=0.15, effect=None):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.frame_index = 0
        self.animation_speed = speed
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.effect = effect
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            if self.effect != None: self.effect()
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]
    
    def update(self):
        self.animate()
        # print(self.frame_index)

class TempIcon(pygame.sprite.Sprite): # todo: isnt actually animated
    def __init__(self, pos, animation_frames, groups, sprite_type, speed=0.15):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.frame_index = 0
        self.animation_speed = speed
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        else:
            self.image = self.frames[int(self.frame_index)]
    
    def update(self):
        self.animate()

class ScreenEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups, effect, speed, remain_time, toggle_screen_effect):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.effect = effect
        self.toggle_screen_effect = toggle_screen_effect
        
        self.frame_index = 0
        self.animation_speed = speed
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        self.showing_effect = False
        self.final_frame_time = remain_time
        self.final_frame_display_time = None
    
    def animate(self):
        current_time = pygame.time.get_ticks()

        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            # Keep last frame shown

            if not self.showing_effect:
                self.showing_effect = True
                self.final_frame_display_time = pygame.time.get_ticks()
        else:
            self.image = self.frames[int(self.frame_index)]
        self.display_surface.blit(self.image, self.rect)

        # Timer
        if self.showing_effect:
            if current_time - self.final_frame_display_time > self.final_frame_time:
                self.kill()
                self.showing_effect = False

                # Effects
                if self.effect != None: self.effect()
                self.toggle_screen_effect()
    
    def update(self):
        self.animate()