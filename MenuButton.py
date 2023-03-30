import pygame, sys, time
from subprocess import call
from StoringData import LoginOrSignup

screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

class MenuButton():
    def __init__(self, x, y, image, function, scale):
        self.x = x
        self.y = y

        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.clicked = False
        self.function = function

    def DrawMenuButton(self, username_text, password_text, score):
        mouse_position = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if self.function == "login":
                    LoginOrSignup(username_text, password_text, score)
                    time.sleep(0.5)
                    return True
                    
                elif self.function == "None":
                    pass
                elif self.function == "quit":
                    sys.exit()
                elif self.function == "play":
                    import PlayGame
                self.clicked = True
            
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False

        screen.blit(self.image, (self.x, self.y))
