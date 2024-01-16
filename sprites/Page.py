import pygame
import pygame.sprite

class Page(pygame.sprite.Sprite):
    game_active = False

    def __init__(self, screen):
        super().__init__()

        self.main_font = pygame.font.Font("assets/fonts/title.ttf", 48)
        self.sub_font = pygame.font.Font("assets/fonts/subtitle.ttf", 19)
        self.pixel_type = pygame.font.Font("assets/fonts/PixelType.ttf", 23)

        self.screen = screen

        self.original_background = pygame.image.load("assets/graphics/Background/space.png")
        self.original_background = pygame.transform.scale(self.original_background, (1280, 720))

        self.earth = pygame.image.load("assets/graphics/Background/earth.png")
        self.earth = pygame.transform.scale(self.earth, (1280,320))

        self.title_text = self.main_font.render("Galatic Firestorm", False, (0,255,0))

        self.start_game_btn = pygame.image.load("assets/graphics/GUI/green-btn.png")
        self.start_game_btn = pygame.transform.scale(self.start_game_btn, (220, 220 / 3.95))
        self.start_game_rect = self.start_game_btn.get_rect()

        self.quit_game_btn = pygame.image.load("assets/graphics/GUI/red-btn.png")
        self.quit_game_btn = pygame.transform.scale(self.quit_game_btn, (220, 220 / 3.95))
        self.quit_game_rect = self.quit_game_btn.get_rect()

        self.start_text = self.sub_font.render("Start game", False, (219, 247, 205))
        self.quit_text = self.sub_font.render("Quit game", False, (255, 201, 201))

        self.drawMainPage()

    def updateFPS(self, fps):
        self.fps_text = self.pixel_type.render(f"FPS: {fps}", False, (0,255,0))

        self.screen.blit(self.fps_text, (5,5))

    def checkClick(self, mouse_x, mouse_y):
        if self.start_game_rect.collidepoint(mouse_x, mouse_y):
            print("Click!")

    def drawMainPage(self):
        screen_width, screen_height = self.screen.get_size()
        background_width, background_height = self.original_background.get_size()

        background_x = (screen_width - background_width) // 2
        background_y = (screen_width - background_width) // 2

        self.screen.blit(self.original_background, (background_x, background_y))

        earth_width, earth_height = self.earth.get_size()

        earth_x = (screen_width - earth_width) // 2
        earth_y = (screen_height - earth_height - ((background_height - screen_height) // 2)) + 140

        self.screen.blit(self.earth, (earth_x, earth_y))

        title_width, title_height = self.title_text.get_size()

        title_x = (self.screen.get_width() - title_width) // 2
        title_y = 120

        self.screen.blit(self.title_text, (title_x, title_y))

        start_width, start_height = self.start_game_btn.get_size()

        start_x = (screen_width - start_width) // 2
        start_y = 220
        quit_y = start_y + start_height + 10

        self.start_game_rect.x = start_x
        self.start_game_rect.y = start_y

        self.quit_game_rect.x = start_x
        self.quit_game_rect.y = quit_y

        self.screen.blit(self.start_game_btn, (start_x, start_y))
        self.screen.blit(self.quit_game_btn, (start_x, quit_y))

        sub_text_width, sub_text_height = self.start_text.get_size()
        quit_text_width, quit_text_height = self.quit_text.get_size()

        sub_text_x = (self.screen.get_width() - sub_text_width) // 2

        start_text_y = start_y + sub_text_height - 5

        self.screen.blit(self.start_text, (sub_text_x, start_text_y))

        quit_text_x = (self.screen.get_width() - quit_text_width) // 2
        quit_text_y = quit_y + sub_text_height - 5

        self.screen.blit(self.quit_text, (quit_text_x, quit_text_y))
