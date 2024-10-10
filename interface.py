# main
import pygame
import os

# intro ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def intro():
    # background colour - dim purple
    screen.fill((75, 76, 117))

    # import background image
    # path = os.path.join(os.getcwd(), 'Assets', 'IntroBG.png')
    # introBG = pygame.transform.scale(pygame.image.load(path), (screen_width, screen_height))
    # screen.blit(introBG, (0, 0)) 
    # pygame.draw.rect(screen, 'blue', pygame.Rect(200, 200, 100, 100))

    # title text
    pygame.font.init()
    path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
    title_font = pygame.font.Font(path, 100)
    title = title_font.render("Name", False, (237, 238, 255))
    screen.blit(title, (100, 90))

    # play button
    start_button = Button(270, 250, 250, 40, 10, (171, 174, 222), 'play')
    start_button.create_button()

    # story button
    story_button = Button(270, 300, 250, 40, 10, (171, 174, 222), 'story')
    story_button.create_button()

    # customization button
    customization_button = Button(270, 350, 250, 40, 10, (171, 174, 222), 'characters')
    customization_button.create_button()

    # exit button
    exit_button = Button(270, 400, 250, 40, 10, (171, 174, 222), 'exit')
    exit_button.create_button()

    # settings button
    settings_button = Button(740, 40, 75, 40, 10, (171, 174, 222), 'set')
    settings_button.create_button()


def intro_clicks() -> int:
    # start button
    if mouse_tact(270, 250, 250, 40):
        return mouse_click(270, 250, 250, 40, GAME)
    # story button
    if mouse_tact(270, 300, 250, 40):
        return mouse_click(270, 300, 250, 40, INSTRUCTIONS)
    # customization button
    if mouse_tact(270, 350, 250, 40):
        return mouse_click(270, 350, 250, 40, CUSTOMIZATIONS)
    # exit button
    if mouse_tact(270, 400, 250, 40):
        return mouse_click(270, 400, 250, 40, 707)
    # settings button
    if mouse_tact(740, 40, 75, 40):
        return mouse_click(740, 40, 75, 40, SETTINGS)
    return mode

# settings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def settings():
    # background colour - dim purple
    screen.fill((75, 76, 117))

    # title text
    pygame.font.init()
    path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
    title_font = pygame.font.Font(path, 70)
    title = title_font.render("Settings", False, (237, 238, 255))
    screen.blit(title, (80, 70))

    volume_display = pygame.Rect(90, 185, 600, 120)
    pygame.draw.rect(screen, (165, 167, 199), volume_display, 0, 20)

    sfx_display = pygame.Rect(90, 335, 600, 120)
    pygame.draw.rect(screen, (165, 167, 199), sfx_display, 0, 20)

    # back button
    back_button = Button(80, 40, 90, 40, 10, (165, 167, 199), 'home')
    back_button.create_button()

def settings_clicks() -> int:
    # back button
    if mouse_tact(80, 40, 90, 40):
        return mouse_click(80, 40, 90, 40, INTRO)
    return mode

# instructions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def instructions():
    # background colour - dim purple
    screen.fill((75, 76, 117))

    # title text
    pygame.font.init()
    path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
    title_font = pygame.font.Font(path, 70)
    title = title_font.render("Story", False, (237, 238, 255))
    screen.blit(title, (80, 70))

    # main display
    main_display = pygame.Rect(90, 150, 600, 330)
    pygame.draw.rect(screen, (165, 167, 199), main_display, 0, 20)

    # back button
    back_button = Button(80, 40, 90, 40, 10, (165, 167, 199), 'home')
    back_button.create_button()

    # settings button
    settings_button = Button(740, 40, 75, 40, 10, (171, 174, 222), 'set')
    settings_button.create_button()

def instructions_clicks():
    # back button
    if mouse_tact(80, 40, 90, 40):
        return mouse_click(80, 40, 90, 40, INTRO)
    # settings button
    if mouse_tact(740, 40, 75, 40):
        return mouse_click(740, 40, 75, 40, SETTINGS)
    return mode

# customizations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def customizations():
    # background colour - dim purple
    screen.fill((75, 76, 117))
    
    # title text
    pygame.font.init()
    path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
    title_font = pygame.font.Font(path, 70)
    title = title_font.render("Customization", False, (237, 238, 255))
    screen.blit(title, (80, 70))

    # P1 display
    p1_display = pygame.Rect(90, 150, 280, 350)
    pygame.draw.rect(screen, (165, 167, 199), p1_display, 0, 20)
    
    # P1 text
    title_font = pygame.font.Font(path, 40)
    title = title_font.render("Player 1", False, (0, 0, 0))
    screen.blit(title, (140, 440))

    # next button
    next_button = Button(330, 180, 50, 40, 10, (147, 149, 186), '>')
    next_button.create_button()

    # back button
    back_button = Button(130, 180, 50, 40, 10, (147, 149, 186), '<')
    back_button.create_button()

    # ~~~~~~~~~~~~~~~~~~~

    # P2 display
    p2_display = pygame.Rect(420, 150, 280, 350)
    pygame.draw.rect(screen, (165, 167, 199), p2_display, 0, 20)

    # P1 text
    title_font = pygame.font.Font(path, 40)
    title = title_font.render("Player 2", False, (0, 0, 0))
    screen.blit(title, (470, 440))

    # next button
    next_button = Button(660, 180, 50, 40, 10, (147, 149, 186), '>')
    next_button.create_button()

    # back button
    back_button = Button(460, 180, 50, 40, 10, (147, 149, 186), '<')
    back_button.create_button()

    # back button
    back_button = Button(80, 40, 90, 40, 10, (165, 167, 199), 'home')
    back_button.create_button()

    # settings button
    settings_button = Button(740, 40, 75, 40, 10, (171, 174, 222), 'set')
    settings_button.create_button()

def customizations_clicks():
    # back button
    if mouse_tact(80, 40, 90, 40):
        return mouse_click(80, 40, 90, 40, INTRO)
    # settings button
    if mouse_tact(740, 40, 75, 40):
        return mouse_click(740, 40, 75, 40, SETTINGS)
    return mode

# game ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def game():
    # background colour - dim purple
    screen.fill((75, 76, 117))

# gameover ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gameover():
    pass

class Button:
    x: float
    y: float
    w: float
    h: float
    corner: float
    base_colour: tuple[float, float, float]
    text: str

    def __init__(self, x, y, w, h, corner, base_colour, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.corner = corner
        self.base_colour = base_colour
        self.text = text

    def create_button(self):
        button = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w, self.h)
        pygame.draw.rect(screen, self.base_colour, button, 0, self.corner)

        # text creation
        pygame.font.init()
        path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
        title_font = pygame.font.Font(path, 20)
        text = title_font.render(self.text, False, (0, 0, 0))
        screen.blit(text, (self.x - self.w/2 + 20, self.y - self.h/5))

        # makes button tactile
        if mouse_tact(self.x, self.y, self.w, self.h):
            pygame.draw.rect(screen, (255, 255, 255), button, 3, self.corner)
            text = title_font.render(self.text, False, (255, 255, 255))
            screen.blit(text, (self.x - self.w/2 + 20, self.y - self.h/5))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mouse_tact(x, y, w, h) -> bool:
    if (x - w/2 <= mouse[0] <= x + w/2) and (y - h/2 <= mouse[1] <= y + h/2):
        return True
    return False

def mouse_click(x, y, w, h, newMode) -> int:
    if (x - w/2 <= mouse[0] <= x + w/2) and (y - h/2 <= mouse[1] <= y + h/2):
        return newMode
    return mode

mode = 0
INTRO = 1
SETTINGS = 2
INSTRUCTIONS = 3
CUSTOMIZATIONS = 4
GAME = 5
GAMEOVER = 6

mode = CUSTOMIZATIONS

# initializing game start
pygame.init()
clock = pygame.time.Clock()

# initializing screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

screen.fill((0, 0, 0))

running = True

while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

        mouse = pygame.mouse.get_pos()

        if mode == INTRO:
            intro()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode = intro_clicks()
                if mode == 707:
                    running = False
        elif mode == SETTINGS:
            settings()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode = settings_clicks()
        elif mode == INSTRUCTIONS:
            instructions()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode = instructions_clicks()
        elif mode == CUSTOMIZATIONS:
            customizations()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode = customizations_clicks()
        elif mode == GAME:
            game()
        elif mode == GAMEOVER:
            gameover()
        else:
            print("Error: Mode = " + str(mode))

        # pygame.display.flip()
