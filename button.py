
import pygame

select_sfx = pygame.mixer.Sound("assets/audio/sfx/CURSOL_SELECT.wav")
select_sfx.set_volume(0.3)
confirm_sfx = pygame.mixer.Sound("assets/audio/sfx/CURSOL_OK.wav")
confirm_sfx.set_volume(0.3)

class Button(pygame.sprite.Sprite):
    def __init__(self, font, color, text_colour, color_hover, rect, callback, text='', outline=None):
        super().__init__()
        self.text = text
        # a temporary Rect to store the size of the button
        tmp_rect = pygame.Rect(0, 0, *rect.size)
    
        # create two Surfaces here, one the normal state, and one for the hovering state
        # we create the Surfaces here once, so we can simple built them and dont have
        # to render the text and outline again every frame
        self.org = self._create_image(font, color, outline, text, text_colour, tmp_rect)
        self.hov = self._create_image(font, color_hover, outline, text, text_colour, tmp_rect)
    
        # in Sprites, the image attribute holds the Surface to be displayed...
        self.image = self.org
        # ...and the rect holds the Rect that defines it position
        self.rect = rect
        self.callback = callback

        self.sfx_hover_played = False

    def _create_image(self, font, color, outline, text, text_colour, rect):
        # function to create the actual surface
        # see how we can make use of Rect's virtual attributes like 'size'
        img = pygame.Surface(rect.size)
        if outline:
            # here we can make good use of Rect's functions again
            # first, fill the Surface in the outline color
            # then fill a rectangular area in the actual color
            # 'inflate' is used to 'shrink' the rect
            img.fill(outline)
            img.fill(color, rect.inflate(-4, -3))
        else:
            img.fill(color)
 
        # render the text once here instead of every frame
        if text != '':
            text_surf = font.render(text, 1, pygame.Color(text_colour))
            # again, see how easy it is to center stuff using Rect's attributes like 'center'
            text_rect = text_surf.get_rect(midleft=(rect.midleft[0] + 10, rect.midleft[1]))
            img.blit(text_surf, text_rect)
        return img
 
    def update(self, events):
        # here we handle all the logic of the Button
        pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(pos)
        # if the mouse is inside the Rect, use the 'hov' image instead of 'org'
        if hit:
            self.image = self.hov
            if not self.sfx_hover_played:
                select_sfx.play()
                self.sfx_hover_played = True
        else:
            self.image = self.org
            self.sfx_hover_played = False
        for event in events:
            # the Button checks for events itself.
            # if this Button is clicked, it runs the callback function
            if self.callback != None and event.type == pygame.MOUSEBUTTONDOWN and hit:
                confirm_sfx.play()
                self.callback()