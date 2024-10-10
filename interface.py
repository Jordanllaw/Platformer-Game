# main
import pygame
import os

# import background image
# path = os.path.join(os.getcwd(), 'Assets', 'IntroBG.png')
# introBG = pygame.transform.scale(pygame.image.load(path), (screen_width, screen_height))
# screen.blit(introBG, (0, 0)) 
# pygame.draw.rect(screen, 'blue', pygame.Rect(200, 200, 100, 100))

# intro ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def intro(screen, mouse):
    # background colour - dim purple
    screen.fill((75, 76, 117))

    # title text
    pygame.font.init()
    path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
    title_font = pygame.font.Font(path, 100)
    title = title_font.render("Name", False, (237, 238, 255))
    screen.blit(title, (100, 90))

    # play button
    start_button = Button(270, 250, 250, 40, 10, (171, 174, 222), 'play')
    start_button.create_button(screen, mouse)

    # story button
    story_button = Button(270, 300, 250, 40, 10, (171, 174, 222), 'story')
    story_button.create_button(screen, mouse)

    # customization button
    customization_button = Button(270, 350, 250, 40, 10, (171, 174, 222), 'characters')
    customization_button.create_button(screen, mouse)

    # exit button
    exit_button = Button(270, 400, 250, 40, 10, (171, 174, 222), 'exit')
    exit_button.create_button(screen, mouse)

    # settings button
    settings_button = Button(740, 40, 75, 40, 10, (171, 174, 222), 'set')
    settings_button.create_button(screen, mouse)


def intro_clicks(mode, mouse) -> int:
    # start button
    if mouse_tact(270, 250, 250, 40, mouse):
        return mouse_click(270, 250, 250, 40, 5, mouse, mode)
    # story button
    if mouse_tact(270, 300, 250, 40, mouse):
        return mouse_click(270, 300, 250, 40, 3, mouse, mode)
    # customization button
    if mouse_tact(270, 350, 250, 40, mouse):
        return mouse_click(270, 350, 250, 40, 4, mouse, mode)
    # exit button
    if mouse_tact(270, 400, 250, 40, mouse):
        return mouse_click(270, 400, 250, 40, 707, mouse, mode)
    # settings button
    if mouse_tact(740, 40, 75, 40, mouse):
        return mouse_click(740, 40, 75, 40, 2, mouse, mode)
    return mode

# settings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def settings(screen, mouse):
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
    back_button.create_button(screen, mouse)

def settings_clicks(mode, mouse) -> int:
    # back button
    if mouse_tact(80, 40, 90, 40, mouse):
        return mouse_click(80, 40, 90, 40, 1, mouse, mode)
    return mode

# instructions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def instructions(screen, mouse):
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
    back_button.create_button(screen, mouse)

    # settings button
    settings_button = Button(740, 40, 75, 40, 10, (171, 174, 222), 'set')
    settings_button.create_button(screen, mouse)

def instructions_clicks(mode, mouse):
    # back button
    if mouse_tact(80, 40, 90, 40, mouse):
        return mouse_click(80, 40, 90, 40, 1, mouse, mode)
    # settings button
    if mouse_tact(740, 40, 75, 40, mouse):
        return mouse_click(740, 40, 75, 40, 2, mouse, mode)
    return mode

# customizations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def customizations(screen, mouse):
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
    next_button.create_button(screen, mouse)

    # back button
    back_button = Button(130, 180, 50, 40, 10, (147, 149, 186), '<')
    back_button.create_button(screen, mouse)

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
    next_button.create_button(screen, mouse)

    # back button
    back_button = Button(460, 180, 50, 40, 10, (147, 149, 186), '<')
    back_button.create_button(screen, mouse)

    # back button
    back_button = Button(80, 40, 90, 40, 10, (165, 167, 199), 'home')
    back_button.create_button(screen, mouse)

    # settings button
    settings_button = Button(740, 40, 75, 40, 10, (171, 174, 222), 'set')
    settings_button.create_button(screen, mouse)

def customizations_clicks(mode, mouse):
    # back button
    if mouse_tact(80, 40, 90, 40, mouse):
        return mouse_click(80, 40, 90, 40, 1, mouse, mode)
    # settings button
    if mouse_tact(740, 40, 75, 40, mouse):
        return mouse_click(740, 40, 75, 40, 2, mouse, mode)
    return mode

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

    def create_button(self, screen, mouse):
        button = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w, self.h)
        pygame.draw.rect(screen, self.base_colour, button, 0, self.corner)

        # text creation
        pygame.font.init()
        path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
        title_font = pygame.font.Font(path, 20)
        text = title_font.render(self.text, False, (0, 0, 0))
        screen.blit(text, (self.x - self.w/2 + 20, self.y - self.h/5))

        # makes button tactile
        if mouse_tact(self.x, self.y, self.w, self.h, mouse):
            pygame.draw.rect(screen, (255, 255, 255), button, 3, self.corner)
            text = title_font.render(self.text, False, (255, 255, 255))
            screen.blit(text, (self.x - self.w/2 + 20, self.y - self.h/5))

# mouse helper functions
def mouse_tact(x, y, w, h, mouse) -> bool:
    if (x - w/2 <= mouse[0] <= x + w/2) and (y - h/2 <= mouse[1] <= y + h/2):
        return True
    return False

def mouse_click(x, y, w, h, newMode, mouse, mode) -> int:
    if (x - w/2 <= mouse[0] <= x + w/2) and (y - h/2 <= mouse[1] <= y + h/2):
        return newMode
    return mode