import pygame
import sys
from sprites.Page import Page

pygame.init()

# load icon
icon = pygame.image.load("assets/graphics/Characters/ship1.png")

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

pygame.display.set_caption("Galactic Firestorm")
pygame.display.set_icon(icon)

# variables
running = True

clock = pygame.time.Clock()

# sprite group
sprites = pygame.sprite.Group()

# init sprites
page = Page(screen)
sprites.add(page)

while running:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False

            case pygame.ACTIVEEVENT:
                if event.gain == 1:
                    page.drawMainPage()

            case pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos

                    page.checkClick(mouse_x, mouse_y)

    pygame.display.flip() # odświeżenie ekranu

pygame.quit()
sys.exit()