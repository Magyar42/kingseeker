import pygame, sys
from settings import *
from debug import debug
from level import Level
from support import *
from button import Button
import json
import gameinfo
import uuid
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

icon_image = pygame.image.load("assets/graphics/ico.png")

# Functions
def mm_newgame():
    print("Starting Game.")

    game.run_game()

def mm_exit():
    print("Exiting.")

    sys.exit()

def mm_credits():
    print("Showing Credits.")

    game.show_credits()

def mm_system():
    print("System Settings.")

    game.settings()

def mm_load_save():
    print("Loading Save.")

    game.load_save()

def display_cursor(img, screen):
    cursor_pos = pygame.mouse.get_pos()
    cursor_rect = img.get_rect(topleft = (cursor_pos[0] - 5, cursor_pos[1] - 2))
    screen.blit(img, cursor_rect)

def change_music():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets/audio/MainTheme.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops = -1)

# Button Sprites
mainmenuFont = pygame.font.Font(UI_FONT, MAIN_MENU_FONT_SIZE)
bodyFont = pygame.font.Font(UI_FONT, 16)
titleFont = pygame.font.Font(UI_FONT, 24)
subTitleFont = pygame.font.Font(UI_FONT, SMALL_FONT_SIZE)
mainMenuSprites = pygame.sprite.Group()
mainMenuSprites.add(
    Button(mainmenuFont, pygame.Color(MM_COLOUR), TEXT_COLOUR, HOVER_COLOUR, pygame.Rect(centreImageNum(200, 20)[0] + 110, centreImageNum(200, 20)[1], 200, 25), mm_newgame, 'NEW GAME'),
    Button(mainmenuFont, pygame.Color(MM_COLOUR), TEXT_COLOUR, HOVER_COLOUR, pygame.Rect(centreImageNum(200, 20)[0] + 110, centreImageNum(200, 20)[1] + 40, 200, 25), mm_load_save, 'LOAD GAME'),
    Button(mainmenuFont, pygame.Color(MM_COLOUR), TEXT_COLOUR, HOVER_COLOUR, pygame.Rect(centreImageNum(200, 20)[0] + 110, centreImageNum(200, 20)[1] + 80, 200, 25), mm_system, 'SETTINGS'),
    Button(mainmenuFont, pygame.Color(MM_COLOUR), TEXT_COLOUR, HOVER_COLOUR, pygame.Rect(centreImageNum(200, 20)[0] + 110, centreImageNum(200, 20)[1] + 120, 200, 25), mm_credits, 'CREDITS'),
    Button(mainmenuFont, pygame.Color(MM_COLOUR), TEXT_COLOUR, HOVER_COLOUR, pygame.Rect(centreImageNum(200, 20)[0] + 110, centreImageNum(200, 20)[1] + 160, 200, 25), mm_exit, 'QUIT'),
)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Kingseeker")
        pygame.display.set_icon(icon_image)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.level = Level("000")
        self.cursor_img = pygame.image.load('assets/graphics/cursor.png').convert_alpha()

        self.frames_list = import_folder('assets/graphics/menu_animations/mainmenu_bonfire')
        self.frame_speed = 0.12
        self.frame_index = 0
        self.image = self.frames_list[self.frame_index]

        self.save_data = None
        # self.save_game()

    def save_game(self):
        # Find the directory in the user's Documents folder
        documents_dir = os.path.expanduser("~/Documents")
        saved_games_dir = os.path.join(documents_dir, "Saved Games", "Kingseeker")

        # Ensure the directory exists
        os.makedirs(saved_games_dir, exist_ok=True)

        # Generate a unique file name using UUID
        unique_id = uuid.uuid4().hex[:8]
        file_name = f"savedata_{unique_id}.json"
        file_path = os.path.join(saved_games_dir, file_name)

        # Collect all dictionaries from gameinfo.py
        self.save_data = {
            name: obj
            for name, obj in vars(gameinfo).items()
            if isinstance(obj, dict) and not name.startswith("__")  # Exclude dunder (double underscore) attributes
        }

        # Save the dictionaries to a JSON file
        with open(file_path, 'w') as file:
            json.dump(self.save_data, file, indent=4)

    def run_game(self):
        change_music()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    
                    # Save the game
                    self.save_game()

                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousekey_pressed = pygame.mouse.get_pressed()
                    if mousekey_pressed[0]:
                        player_inputs["light attack"] = True
                    elif mousekey_pressed[2]:
                        player_inputs["heavy attack"] = True
                    elif mousekey_pressed[1]:
                        player_inputs["cast spell"] = True
                elif event.type == pygame.MOUSEWHEEL:
                    player_inputs["scroll spell"] = True
                    player_inputs["scroll direction"] = event.y

            self.screen.fill(MM_COLOUR)
            self.level.run()

            display_cursor(self.cursor_img, self.screen)
            pygame.display.update()
            self.clock.tick(FPS)

    def load_save(self):
        # Open file dialog
        Tk().withdraw()  # Prevent Tkinter window from appearing
        file_path = askopenfilename(
            title="Select a save file",
            filetypes=[("JSON files", "*.json")]
        )

        if not file_path:
            print("No file selected.")
            return
    
        try:
            # Load the JSON data from the save file
            with open(file_path, 'r') as file:
                saved_data = json.load(file)
            
            # Update dictionaries in gameinfo with the loaded data
            for name, save_data in saved_data.items():
                if hasattr(gameinfo, name):  # Check if the attribute exists in gameinfo
                    gameinfo_dict = getattr(gameinfo, name)
                    if isinstance(gameinfo_dict, dict):  # Ensure it's a dictionary before updating
                        # print(gameinfo_dict)
                        # print(save_data)
                        gameinfo_dict.update(save_data)  # Update the dictionary in place
                        print(f"Updated {name} in gameinfo.")
        
        # If file cannot be loaded (due to corruption, fake file etc)
        except:
            print("Cannot load save file. Creating new save instead.")
        
        # Run game
        self.run_game()

    
    # def play_intro(self):
    #     while True:
    #         key = None
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 opening.close()
    #                 pygame.quit()
    #                 exit()

    #             if event.type == pygame.KEYDOWN:
    #                 key = pygame.key.name(event.key)
            
    #         if opening.get_pos() >= 219 or opening.get_pos() >= 0.1 and key == "escape": # Skip
    #             opening.close()
    #             pygame.mixer.music.load("assets/audio/MainTheme.mp3")
    #             pygame.mixer.music.set_volume(0.1)
    #             pygame.mixer.music.play(loops = -1)
    #             game.run_game()
            
    #         if opening.draw(pygame.display.get_surface(), (0, 0), force_draw=False):
    #             pygame.display.update()
    #         self.clock.tick(FPS)

    def main_menu(self):
        mainmenu_title = pygame.transform.scale(pygame.image.load("assets/graphics/title3.png"), (949, 125))

        while True:
            self.screen.fill(MM_COLOUR)
            # Bonfire Animation
            self.frame_index += self.frame_speed
            if self.frame_index >= len(self.frames_list):
                self.frame_index = 0
            self.image = pygame.transform.scale(self.frames_list[int(self.frame_index)], (258, 354))

            # Blit Images & Surfaces
            mainMenuSprites.draw(self.screen)
            mainMenuSprites.update(pygame.event.get())

            header_surf = subTitleFont.render("Kristof Konig Presents", 1, "white")
            x, y = centreImage(header_surf)
            self.screen.blit(header_surf, (x, y - 270))

            x, y = centreImage(self.image)
            self.screen.blit(self.image, (x - 180, y + 100))
            self.screen.blit(mainmenu_title, (centreImage(mainmenu_title)[0], centreImage(mainmenu_title)[1] - 190))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            display_cursor(self.cursor_img, self.screen)
            pygame.display.update()
            self.clock.tick(FPS)
    
    def settings(self):
        while True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.main_menu()

            self.screen.fill((MM_COLOUR))

            system_title = titleFont.render("SETTINGS", True, TEXT_COLOUR)
            system_title_rect = system_title.get_rect(topleft = (centreImage(system_title)[0], centreImage(system_title)[1] - 250))
            self.screen.blit(system_title, system_title_rect)

            cat_index = 0
            for cat in global_settings.keys():
                item_index = 0
                for item in global_settings[cat]:
                    #print(f"{item}: {global_settings[cat][item]}")
                    rendered_item = bodyFont.render(f'{item}: {global_settings[cat][item]}', True, TEXT_COLOUR)
                    item_rect = rendered_item.get_rect(topleft = (centreImage(rendered_item)[0], centreImage(rendered_item)[1] - 200 + (item_index * 25) + (cat_index * 100)))
                    self.screen.blit(rendered_item, item_rect)
                    item_index += 1
                cat_index += 1

            header_surf = subTitleFont.render("ESC to return", 1, "white")
            self.screen.blit(header_surf, (10, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            display_cursor(self.cursor_img, self.screen)
            pygame.display.update()
            self.clock.tick(FPS)

    def show_credits(self):
        while True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.main_menu()
            
            self.screen.fill((MM_COLOUR))

            credits_title = titleFont.render("CREDITS", True, TEXT_COLOUR)
            credits_title_rect = credits_title.get_rect(topleft = (centreImage(credits_title)[0], centreImage(credits_title)[1] - 250))
            self.screen.blit(credits_title, credits_title_rect)

            for item in credits_info:
                rendered_item = bodyFont.render(item, True, TEXT_COLOUR)
                item_rect = rendered_item.get_rect(topleft = (centreImage(rendered_item)[0], centreImage(rendered_item)[1] - 200 + (credits_info.index(item) * 25)))
                self.screen.blit(rendered_item, item_rect)
            # self.screen.blit(credits_text, credits_rect)

            header_surf = subTitleFont.render("ESC to return", 1, "white")
            self.screen.blit(header_surf, (10, 10))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            display_cursor(self.cursor_img, self.screen)
            pygame.display.update()
            self.clock.tick(FPS)


pygame.mixer.music.load("assets/audio/Soles of Fire.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops = -1)

select_sfx = pygame.mixer.Sound("assets/audio/sfx/CURSOL_SELECT.wav")
select_sfx.set_volume(0.2)
confirm_sfx = pygame.mixer.Sound("assets/audio/sfx/CURSOL_OK.wav")

pygame.mouse.set_visible(False)

# Game
if __name__ == "__main__":
    game = Game()
    game.main_menu()