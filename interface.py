# main
import pygame
import os
import main

# intro ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def intro():
    # background colour - dim purple
    main.screen.fill((75, 76, 117))

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
    main.screen.blit(title, (100, 90))

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
    if main.mouse_tact(270, 250, 250, 40):
        return main.mouse_click(270, 250, 250, 40, main.GAME)
    # story button
    if main.mouse_tact(270, 300, 250, 40):
        return main.mouse_click(270, 300, 250, 40, main.INSTRUCTIONS)
    # customization button
    if main.mouse_tact(270, 350, 250, 40):
        return main.mouse_click(270, 350, 250, 40, main.CUSTOMIZATIONS)
    # exit button
    if main.mouse_tact(270, 400, 250, 40):
        return main.mouse_click(270, 400, 250, 40, 707)
    # settings button
    if main.mouse_tact(740, 40, 75, 40):
        return main.mouse_click(740, 40, 75, 40, main.SETTINGS)
    return main.mode

# settings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def settings():
    # background colour - dim purple
    main.screen.fill((75, 76, 117))

    # title text
    pygame.font.init()
    path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
    title_font = pygame.font.Font(path, 70)
    title = title_font.render("Settings", False, (237, 238, 255))
    main.screen.blit(title, (80, 70))

    volume_display = pygame.Rect(90, 185, 600, 120)
    pygame.draw.rect(main.screen, (165, 167, 199), volume_display, 0, 20)

    sfx_display = pygame.Rect(90, 335, 600, 120)
    pygame.draw.rect(main.screen, (165, 167, 199), sfx_display, 0, 20)

    # back button
    back_button = Button(80, 40, 90, 40, 10, (165, 167, 199), 'home')
    back_button.create_button()

def settings_clicks() -> int:
    # back button
    if main.mouse_tact(80, 40, 90, 40):
        return main.mouse_click(80, 40, 90, 40, main.INTRO)
    return main.mode

# instructions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def instructions():
    # background colour - dim purple
    main.screen.fill((75, 76, 117))

    # title text
    pygame.font.init()
    path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
    title_font = pygame.font.Font(path, 70)
    title = title_font.render("Story", False, (237, 238, 255))
    main.screen.blit(title, (80, 70))

    # main display
    main_display = pygame.Rect(90, 150, 600, 330)
    pygame.draw.rect(main.screen, (165, 167, 199), main_display, 0, 20)

    # back button
    back_button = Button(80, 40, 90, 40, 10, (165, 167, 199), 'home')
    back_button.create_button()

    # settings button
    settings_button = Button(740, 40, 75, 40, 10, (171, 174, 222), 'set')
    settings_button.create_button()

def instructions_clicks():
    # back button
    if main.mouse_tact(80, 40, 90, 40):
        return main.mouse_click(80, 40, 90, 40, main.INTRO)
    # settings button
    if main.mouse_tact(740, 40, 75, 40):
        return main.mouse_click(740, 40, 75, 40, main.SETTINGS)
    return main.mode

# customizations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def customizations():
    # background colour - dim purple
    main.screen.fill((75, 76, 117))
    
    # title text
    pygame.font.init()
    path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
    title_font = pygame.font.Font(path, 70)
    title = title_font.render("Customization", False, (237, 238, 255))
    main.screen.blit(title, (80, 70))

    # P1 display
    p1_display = pygame.Rect(90, 150, 280, 350)
    pygame.draw.rect(main.screen, (165, 167, 199), p1_display, 0, 20)
    
    # P1 text
    title_font = pygame.font.Font(path, 40)
    title = title_font.render("Player 1", False, (0, 0, 0))
    main.screen.blit(title, (140, 440))

    # next button
    next_button = Button(330, 180, 50, 40, 10, (147, 149, 186), '>')
    next_button.create_button()

    # back button
    back_button = Button(130, 180, 50, 40, 10, (147, 149, 186), '<')
    back_button.create_button()

    # ~~~~~~~~~~~~~~~~~~~

    # P2 display
    p2_display = pygame.Rect(420, 150, 280, 350)
    pygame.draw.rect(nain.screen, (165, 167, 199), p2_display, 0, 20)

    # P1 text
    title_font = pygame.font.Font(path, 40)
    title = title_font.render("Player 2", False, (0, 0, 0))
    main.screen.blit(title, (470, 440))

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
    if main.mouse_tact(80, 40, 90, 40):
        return main.mouse_click(80, 40, 90, 40, main.INTRO)
    # settings button
    if main.mouse_tact(740, 40, 75, 40):
        return main.mouse_click(740, 40, 75, 40, main.SETTINGS)
    return main.mode

# game ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def game():
    # background colour - dim purple
    main.screen.fill((75, 76, 117))

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
        pygame.draw.rect(main.screen, self.base_colour, button, 0, self.corner)

        # text creation
        pygame.font.init()
        path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
        title_font = pygame.font.Font(path, 20)
        text = title_font.render(self.text, False, (0, 0, 0))
        main.screen.blit(text, (self.x - self.w/2 + 20, self.y - self.h/5))

        # makes button tactile
        if main.mouse_tact(self.x, self.y, self.w, self.h):
            pygame.draw.rect(main.screen, (255, 255, 255), button, 3, self.corner)
            text = title_font.render(self.text, False, (255, 255, 255))
            main.screen.blit(text, (self.x - self.w/2 + 20, self.y - self.h/5))
