import pygame, random, math, time, hashlib
from StoringData import CheckingName, ScoreChecker
from MenuButton import MenuButton

#importing pygame display and font modules
pygame.display.init()
pygame.font.init()

#setting the pygame screen size, name and icon
width = 1000
height = 1050

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption(" Mastermind")
icon_for_screen = pygame.image.load("Assets\Images\Icon\Icon.png")
pygame.display.set_icon(icon_for_screen)

#font
font = pygame.font.Font("freesansbold.ttf", 20)
error_font = pygame.font.Font("freesansbold.ttf", 20)
bigger_font = pygame.font.Font("freesansbold.ttf", 30)
Login_font = pygame.font.Font("freesansbold.ttf", 60)
DPBfont = pygame.font.Font("Assets\Fonts\DAYPBL__.TTF", 40)
bigger_DPBfont = pygame.font.Font("Assets\Fonts\DAYPBL__.TTF", 80)

#colours used for pygame
red = (255, 77, 77)
orange = (255, 128, 0)
yellow = (230, 230, 0)
green = (0, 153, 0)
blue = (0, 77, 153)
purple = (77, 0, 153)
pink = (255, 128, 170)
brown = (102, 68, 0)

checkbutton = (25, 77, 0)

moved_red = (254, 77, 77)
moved_orange = (254, 128, 0)
moved_yellow = (229, 230, 0)
moved_green = (0, 152, 0)
moved_blue = (0, 76, 153)
moved_purple = (76, 0, 153)
moved_pink = (254, 128, 170)
moved_brown = (101, 68, 0)

pin_red = ((255, 76, 77))
pin_white = (255, 254, 255)

grey = (169, 169, 169)
black = (0, 0, 0)


#list of all rgb for colours
rgb_colours = [red, orange, yellow, green, blue, purple, pink, brown]
moved_rgb_colours = [moved_red, moved_orange, moved_yellow, moved_green, moved_blue, moved_purple, moved_pink, moved_brown]
pin_rgb_colours = [pin_red, pin_white]

#text colours
length_of_code_message = black
repeating_colours_message = grey
win_message = grey
textbox_colour_active = (68, 119, 178)
textbox_colour_passive = (72, 68, 178)

#variable for code properties, create code, draw board
use_repeating_colours, got_length_of_code, is_draw_on, make_code, scoring, score_result = False, False, False, False, False, False
username_active, password_active = False, False
length_of_code = 0

#user text and rects for text boxes
username_text = "Username"
username_rect = pygame.Rect(100, 200, 400, 100)
password_text = "Password"
password_rect = pygame.Rect(100, 350, 400, 100)
login_image = pygame.image.load("Assets\Images\Menu_Buttons\login.png").convert()
back_image = pygame.image.load("Assets\Images\Menu_Buttons/back.png").convert()




#main class for creating code, handling code and displaying objects
class CodeHandler:
    #class constructor to define class variables
    def __init__(self, length_of_code, button_list):
        self.code = []
        self.length_of_code = int(length_of_code)
        
        self.button_list = button_list
        self.board = []
        self.pin_list = []

        self.row = 10
        self.previous_buttons = []
        self.previous_pins = []


    #function to create code depending on user preference
    def CodeCreator(self, use_repeating_colours):
        self.use_repeating_colours = use_repeating_colours
        name_of_colours = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]

        if use_repeating_colours == False: #if no repeating colours: for users specified length of code, choose one random colour, add it to the code and remove that colour from the list
            for _ in range(self.length_of_code):
                random_colour = name_of_colours[random.randint(0, len(name_of_colours) - 1)]
                self.code.append(random_colour)
                name_of_colours.remove(random_colour)

        elif use_repeating_colours == True: #if repeating colours: for users specified length of code, choose one random colour and add it to the code
            for _ in range(self.length_of_code):
                random_colour = name_of_colours[random.randint(0, len(name_of_colours) - 1)]
                self.code.append(random_colour)
        

    #function that displays the objects on the screen
    def DisplayObjects(self):
        for item in self.button_list:
            item.DrawSideButton()
        check_button.DrawCheckButton()
        for item in self.board:
            item.DrawMovedButton()
        for item in self.pin_list:
            item.DrawPin()
        for item in self.previous_buttons:
          item.DrawMovedButton()
        for item in self.previous_pins:
          item.DrawPin()
        
              
    


#this class is for all the Buttons and where their x, y, image and their colour
class SideButton():

    def __init__(self, colour_rgb, colour):
        self.x = 610
        
        self.colour_rgb = colour_rgb
        self.colour = colour

        index = rgb_colours.index(self.colour_rgb)
        self.y = 50 + (70 * index)


    #function to draw the Button onto the screen
    def DrawSideButton(self): 
        pygame.draw.circle(screen, self.colour_rgb, (self.x + (1 / 2 * self.x), self.y + (1 / 2 * self.y)), 40)
        pygame.draw.circle(screen, (0, 0, 0), (self.x + (1 / 2 * self.x), self.y + (1 / 2 * self.y)), 41, 2)


  #function to add the buttons onto the board
    def AddButtonsOnBoard(self):
        Mastermind.board.append(MovedButton(self.colour_rgb, self.colour))#adds the button to the board

        
        




#this class creates buttons which are copies of the original ones but are in another list
class MovedButton():

    def __init__(self, colour_rgb, colour):
        index = rgb_colours.index(colour_rgb)
        self.colour_rgb = moved_rgb_colours[index]

        self.colour = colour

        self.x = self.__XCoordinateOnBoard()
        self.y = self.__YCoordinateOnBoard()
    
    #function to find the x coordinate for the button
    def __XCoordinateOnBoard(self):
        index = len(Mastermind.board)
        return math.floor(50 + (index * 85))
    
    #function to find the y coordinate for the button
    def __YCoordinateOnBoard(self):
        return math.floor(60 + ((Mastermind.row - 1) * 100)) 

    #function to add the board to a list of all the buttons on the board
    def DrawMovedButton(self):
        pygame.draw.circle(screen, self.colour_rgb, (self.x, self.y), 35)
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 36, 2)
    
    #function to revome the button off the board 
    def RemoveButtonOffBoard(self):
        mouse_position = pygame.mouse.get_pos()
        if self.x - 40 <= mouse_position[0] and self.x + 40 >= mouse_position[0]:
            if self.y - 40 <= mouse_position[1] and self.y + 40 >= mouse_position[1]:
                index =  Mastermind.board.index(self)

                for _ in range(len(Mastermind.board) - index):
                    Mastermind.board.pop()


        



#this class is for the button which checks the rows
class CheckButton():

    def __init__(self):
        self.x = 610
        self.y = 610
        self.checked = False

    #function to draw the check button
    def DrawCheckButton(self):
        pygame.draw.circle(screen, checkbutton, (self.x + (1 / 2 * self.x), self.y + (1 / 2 * self.y)), 40)
        pygame.draw.circle(screen, (0, 0, 0), (self.x + (1 / 2 * self.x), self.y + (1 / 2 * self.y)), 41, 2)
        self.__DisplayCheckMark()
        

    #function to draw the check mark onto the button
    def __DisplayCheckMark(self):
        tick_font = pygame.font.Font("Assets\Fonts\seguisym.ttf", 50)
        text_surface = tick_font.render(u'\u2713', True, (255, 253, 255))
        screen.blit(text_surface, (895, 880))

    #function which checks how many of each colour pin the guess deserves
    def RowChecker(self):
        copy_of_board = []
        for item in Mastermind.board:
            copy_of_board.append(item.colour) #makes copy of board and the code to remove colours after its colour is assigned 
        copy_of_code = Mastermind.code.copy()

        same_index_same_colour = [x for x, y in zip(copy_of_board, copy_of_code) if x == y] #checks the colours are the same and if the indexes are the same 

        for item in same_index_same_colour:
            try:
              Mastermind.pin_list.append(Pin(pin_red))#for every item in the same_index_same_colour it adds it to the pin_list to be display it
              copy_of_board.remove(item)
              copy_of_code.remove(item)
            except:
              pass
        

        different_index_same_colour = [x for x in copy_of_board if x in copy_of_code] #checks if board has colours are same in both copies of lists 
        
        for item in different_index_same_colour:
            if item in copy_of_code:
              Mastermind.pin_list.append(Pin(pin_white)) #for every item in the different_index_same_colour it adds it to the pin_list to display it
              copy_of_board.remove(item)
              copy_of_code.remove(item) 

        for item in Mastermind.pin_list:
            item.CoordinateFinder()
            item.DrawPin()

        code_correctness = 0
        for item in Mastermind.pin_list:
          if item.colour_rgb == pin_red:
            code_correctness += 1
          if code_correctness == Mastermind.length_of_code:
            FinalMessage(True)

        Mastermind.row -= 1
        if Mastermind.row == 0:
            FinalMessage(False)

        for item in Mastermind.board:
          Mastermind.previous_buttons.append(item)
        Mastermind.board.clear()

        for item in Mastermind.pin_list:
          Mastermind.previous_pins.append(item)
        Mastermind.pin_list.clear()






  
class Pin():

    def __init__(self, colour_rgb):
        self.colour_rgb = colour_rgb


    def CoordinateFinder(self):
        self.index = Mastermind.pin_list.index(self)
        self.y = self.__PositionOnPinSide(self.index)
        
        if (self.index + 1) > math.ceil(Mastermind.length_of_code / 2):
          self.index = self.index - math.ceil(Mastermind.length_of_code / 2)
          
        self.x = ((85 * Mastermind.length_of_code) + (45 * self.index) + 40)


    #this function draws the pins and has no other functionality
    def DrawPin(self):
        pygame.draw.circle(screen, self.colour_rgb, (self.x, self.y), 10)
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 11, 2)


    def __PositionOnPinSide(self, index):
        if (index + 1) <= math.ceil(Mastermind.length_of_code / 2): 
            return int(40 + (100 * (Mastermind.row - 1)))
        else:
            return int(80 + (100 * (Mastermind.row - 1)))  




#these variables and lists below contain all of the buttons / icons to be displayed on the board
button_list = [
    SideButton((255, 77, 77), "red"),
    SideButton((255, 128, 0), "orange"),
    SideButton((230, 230, 0), "yellow"),
    SideButton((0, 153, 0), "green"),
    SideButton((0, 77, 153), "blue"),
    SideButton((77, 0, 153), "purple"),
    SideButton((255, 128, 170), "pink"),
    SideButton((102, 68, 0), "brown")
    ]
check_button = CheckButton()


def ShowText(length_of_code_message, repeating_colours_message):
    try:
        text = DPBfont.render("What Length should the board be? (2-7)", True, length_of_code_message)
        screen.blit(text, (40, 100))

        text = DPBfont.render("Should the code have repeating colours?", True, repeating_colours_message)
        screen.blit(text, (35, 200))
        text = DPBfont.render("(Y/N)", True, repeating_colours_message)
        screen.blit(text, (425, 240))
    except:
        pass


def DrawRectangleBase(length_of_code):
    pygame.draw.rect(screen, (128, 69, 45), pygame.Rect(10, 10, (85*length_of_code), 1000)) #each circle is gonna be 70 but 10 of them
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, 10, (85*length_of_code), 1000), 2)

    pygame.draw.rect(screen, (128, 69, 45), pygame.Rect(10 + (85*length_of_code), 10, (32*length_of_code), 1000))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(11 + (85*length_of_code), 10, (32*length_of_code), 1000), 2)


def DrawPositionsItems(length_of_code):
    for height in range(10):
        for width in range(length_of_code):            
            pygame.draw.circle(screen, (0, 0, 0), (51 + (85 * width), 60 + (100 * height)), 30)

        for position in range(math.ceil(length_of_code/2)):
            pygame.draw.circle(screen, (0, 0, 0), (40 + (85 * length_of_code) + (45 * position), 40 + (100 * height)), 10)

        for position in range(math.ceil(length_of_code//2)):
            pygame.draw.circle(screen, (0, 0, 0), (40 + (85 * length_of_code) + (45 * position), 80 + (100 * height)), 10)

def FinalMessage(win):
    if win == True:
        
        pygame.draw.rect(screen, black, pygame.Rect(0, 300, 1000, 400))

        win_message = "YOU WON!!!"
        win_message_list = [letter for letter in win_message]
        for index in range(len(win_message_list)):
            font_colour = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
            text = bigger_font.render(win_message_list[index], True, font_colour)
            screen.blit(text, (400 + (24 * index), 500))

        text = bigger_font.render("Thank you for playing", True, (255, 255, 255))
        screen.blit(text, (350, 450))
    
    if win == False:

        pygame.draw.rect(screen, black, pygame.Rect(0, 300, 1000, 400))

        win_message = "GAME OVER!!!"
        win_message_list = [letter for letter in win_message]
        for index in range(len(win_message_list)):
            font_colour = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
            text = bigger_font.render(win_message_list[index], True, font_colour)
            screen.blit(text, (375 + (24 * index), 500))
        
        text = bigger_font.render("Thank you for playing", True, (255, 255, 255))
        screen.blit(text, (350, 450))

        code_as_message ="The final code was: " + ", ".join([str(colour) for colour in Mastermind.code]) 
        text = bigger_font.render(code_as_message, True, (255, 255, 255))
        screen.blit(text, (10, 550))
        
    pygame.display.update()
    time.sleep(5)

    global scoring
    scoring = True
    

def PasswordHandler(password):
    lower, upper, symbols, digit = 0, 0, 0, 0
    if len(password) == 0 or password == "Password":
        return None
    elif (len(password) >= 8):
        for letter in password:
            if (letter.islower()):
                lower += 1           
            if (letter.isupper()):
                upper += 1           
            if (letter.isdigit()):
                digit += 1           
            if(letter == "@" or letter == "$" or letter == "_" or letter == "*" or letter == "!" or letter == "%" or letter == "&"):
                symbols += 1          
    if (lower>=1 and upper>=1 and symbols>=1 and digit>=1 and lower+upper+symbols+digit==len(password)):
        return True
    else:
        return False

def HashPassword(password):
  password_bytes = password.encode("utf-8")
  hashed_bytes = hashlib.sha256(password_bytes).digest()
  hashed_password = "".join("{:02x}".format(b) for b in hashed_bytes)
  return hashed_password


def Score():
    extra = 0
    if Mastermind.use_repeating_colours == True:
        extra = 100
    score = (10 - Mastermind.row) * Mastermind.length_of_code * 10 + extra
    return score


def LoginMenu(username_colour, username_rect, username_text, password_colour, password_rect, password_text):
    function = "login"
    password_secure = False
    
    text = DPBfont.render("Enter your username and password:", True, black)
    screen.blit(text, (50, username_rect.y - 100))

    pygame.draw.rect(screen, black, (username_rect.x - 3, username_rect.y - 2, username_rect.w + 6, 106))
    pygame.draw.rect(screen, black, (password_rect.x - 3, password_rect.y - 2, password_rect.w + 6, 106))
    pygame.draw.rect(screen, username_colour, username_rect)
    pygame.draw.rect(screen, password_colour, password_rect)


    username_text_surface = Login_font.render(username_text, True, pin_white)
    password_text_surface = Login_font.render(password_text, True, pin_white)
    screen.blit(username_text_surface, (username_rect.x + 10, username_rect.y + 20))
    screen.blit(password_text_surface, (password_rect.x + 10, password_rect.y + 20)) 

    username_rect.w = max(350, username_text_surface.get_width() + 30)
    password_rect.w = max(350, password_text_surface.get_width() + 30)

    if CheckingName(username_text, HashPassword(password_text)) == False:
        function = "None"
        text = font.render("That username is already taken!", True, red)
        screen.blit(text, (380, 500))
        pygame.time.wait(1)
    
    else:
        function = "login"
    
    if PasswordHandler(password_text) == False:
        function = "None"
        text = font.render("Password must be greater than 8 characters and include uppercases, symbols and numbers!", True, red)
        screen.blit(text, (80, 550))
        pygame.time.wait(1)

    else:
        function = "login"
        password_text = HashPassword(password_text)

    login_button = MenuButton(400, 600, login_image, function, 2)
    if login_button.DrawMenuButton(username_text, password_text, Score()) == True:

        score_list = ScoreChecker(username_text)
        high_score = list(score_list)[0][0]
        average_score = list(score_list)[0][1]

        text = DPBfont.render("High score:", True, black)
        high_score_text = bigger_DPBfont.render(str(int(high_score)), True, black)
        screen.blit(text, (100, 500))
        screen.blit(high_score_text, (150, 550))

        text = DPBfont.render("Average score:", True, black)
        average_score_text = bigger_DPBfont.render(str(int(average_score)), True, black)
        screen.blit(text, (500, 500))
        screen.blit(average_score_text, (600, 550))
        pygame.display.update()
        pygame.time.wait(5000)
        import MainMenu
            

    
        
        

        
screen.fill(grey)

#game loop
game_loop_running = True
while game_loop_running:
    
    if scoring == False:
        #if someone exits then the game fully stops
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop_running = False     

            if event.type == pygame.MOUSEBUTTONDOWN and is_draw_on == True:
                if len(Mastermind.board) == int(length_of_code):
                    click = screen.get_at(pygame.mouse.get_pos()) == (25, 77, 0)
                    click_2 = screen.get_at(pygame.mouse.get_pos()) == (255, 253, 255)

                    if click == True or click_2 == True:
                        check_button.RowChecker()
                
                elif len(Mastermind.board) < int(length_of_code):
                    for item in rgb_colours:
                        click = screen.get_at(pygame.mouse.get_pos()) == item

                        if click == True:
                            for button in button_list:
                                if button.colour_rgb == item:
                                    button.AddButtonsOnBoard()
                
                if len(Mastermind.board) > 0:
                    for item in moved_rgb_colours:
                        click = screen.get_at(pygame.mouse.get_pos()) == item

                        if click == True:
                            for button in Mastermind.board:
                                if button.colour_rgb == item:
                                    button.RemoveButtonOffBoard()

                        

            if event.type == pygame.KEYDOWN and is_draw_on == False:
                if pygame.key.name(event.key) in ["2", "3", "4", "5", "6", "7"]:
                    length_of_code = pygame.key.name(event.key)
                    got_length_of_code = True
                    length_of_code_message = grey
                    repeating_colours_message = black

                if got_length_of_code == True:
                    if pygame.key.name(event.key) in ["y", "Y"]:
                        got_repeating_colour_answer = True
                        make_code = True

                    elif pygame.key.name(event.key) in ["n", "N"]:
                        got_repeating_colour_answer = False
                        make_code = True

                    if make_code == True:
                        repeating_colours_message = grey
                        is_draw_on = True

                        Mastermind = CodeHandler(length_of_code, button_list)
                        Mastermind.CodeCreator(got_repeating_colour_answer)


        
        try:
            screen.fill(grey)
        except:
            pass    
        ShowText(length_of_code_message, repeating_colours_message)

        if is_draw_on == True:
            DrawRectangleBase(int(length_of_code))
            DrawPositionsItems(int(length_of_code))
        
        try:
            Mastermind.DisplayObjects()
        except:
            pass
    

    elif scoring == True:
        screen.fill(grey)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop_running = False 

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if username_rect.collidepoint(event.pos):
                    username_active = True
                    if username_text == "Username":
                        username_text = ""
                else:
                    username_active = False
                    if username_text == "":
                        username_text = "Username"


                if password_rect.collidepoint(event.pos):
                    password_active = True
                    if password_text == "Password":
                        password_text = ""
                else:
                    password_active = False
                    if password_text == "":
                        password_text = "Password"
            
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_RETURN, pygame.K_TAB, pygame.K_ESCAPE, pygame.K_SPACE, pygame.K_LCTRL, pygame.K_RCTRL]:
                    pass
                elif username_active == True:
                    if event.key == pygame.K_BACKSPACE: 
                        username_text = username_text[:-1]
                    elif len(username_text) >= 20:
                        pass 
                    else:
                        if pygame.key.get_pressed()[pygame.K_RCTRL] or pygame.key.get_pressed()[pygame.K_LCTRL]:
                            pass
                        else:
                            username_text += event.unicode

                elif password_active == True:
                    if event.key == pygame.K_BACKSPACE: 
                        password_text = password_text[:-1]
                    elif len(password_text) >= 20:
                        pass     
                    else:
                        if pygame.key.get_pressed()[pygame.K_RCTRL] or pygame.key.get_pressed()[pygame.K_LCTRL]:
                            pass
                        else:
                            password_text += event.unicode
                        

        if username_active == True:
            username_colour = textbox_colour_active
            password_colour = textbox_colour_passive
        elif password_active == True:
            password_colour = textbox_colour_active
            username_colour = textbox_colour_passive
        else:
            username_colour = textbox_colour_passive
            password_colour = textbox_colour_passive
        

        LoginMenu(username_colour, username_rect, username_text, password_colour, password_rect, password_text)
    


    pygame.display.update()
