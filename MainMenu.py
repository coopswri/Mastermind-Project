import pygame, sys
from subprocess import call
from MenuButton import MenuButton


pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption(" MainMenu")
icon_for_screen = pygame.image.load("Assets\Images\Icon\Icon.png")
pygame.display.set_icon(icon_for_screen)

#font
DPBfont = pygame.font.Font("Assets\Fonts\DAYPBL__.TTF", 70)

#load menu button images
play_image = pygame.image.load("Assets\Images\Menu_Buttons\play.png").convert()
quit_image = pygame.image.load("Assets\Images\Menu_Buttons\quit.png").convert()


play_button = MenuButton(180, 150, play_image, "play", 1)
quit_button = MenuButton(184, 250, quit_image, "quit", 1)

MenuButtons = [play_button, quit_button]


game_loop_running = True
while game_loop_running:

    screen.fill((169, 169, 169))

    text = DPBfont.render("Mastermind", True, (0, 0, 0))
    screen.blit(text, (15, 10))

    for item in MenuButtons:
        item.DrawMenuButton(None, None, None)

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop_running = False

    pygame.display.update()