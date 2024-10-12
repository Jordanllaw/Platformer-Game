# main
import pygame
import os

# import background image
# path = os.path.join(os.getcwd(), 'Assets', 'IntroBG.png')
# introBG = pygame.transform.scale(pygame.image.load(path), (screen_width, screen_height))
# screen.blit(introBG, (0, 0)) 
# pygame.draw.rect(screen, 'blue', pygame.Rect(200, 200, 100, 100))

# intro ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def intro(screen, mouse, counter, gif):
    # background colour - dim purple
    screen.fill((75, 76, 117))

    # title text
    pygame.font.init()
    path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
    title_font = pygame.font.Font(path, 100)
    title = title_font.render("Rock Monster", False, (237, 238, 255))
    screen.blit(title, (50, 90))

    # play button
    start_button = Button(270, 250, 250, 40, 10, (171, 174, 222), 'play')
    start_button.create_button(screen, mouse)

    # story button
    story_button = Button(270, 300, 250, 40, 10, (171, 174, 222), 'story')
    story_button.create_button(screen, mouse)

    # customization button
    customization_button = Button(270, 350, 250, 40, 10, (171, 174, 222), 'customization')
    customization_button.create_button(screen, mouse)

    # exit button
    exit_button = Button(270, 400, 250, 40, 10, (171, 174, 222), 'exit')
    exit_button.create_button(screen, mouse)

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
    main_display = pygame.Rect(90, 150, 600, 400)
    pygame.draw.rect(screen, (165, 167, 199), main_display, 0, 20)

    # back button
    back_button = Button(720, 40, 90, 40, 10, (165, 167, 199), 'home')
    back_button.create_button(screen, mouse)

def instructions_clicks(mode, mouse):
    # back button
    if mouse_tact(720, 40, 90, 40, mouse):
        return mouse_click(720, 40, 90, 40, 1, mouse, mode)
    return mode

# customizations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

curr_char1 = 0
curr_char2 = 0

def customizations(screen, mouse, curr1, curr2):
    # getting images of characters
    character_p1 = []

    image_path1 = os.path.join(os.getcwd(), 'Assets', 'P1.png')
    image_path2 = os.path.join(os.getcwd(), 'Assets', 'P2.png')
    image_path3 = os.path.join(os.getcwd(), 'Assets', 'P3.png')
    character_p1.append(pygame.transform.scale(pygame.image.load(image_path1), (200, 200)))
    character_p1.append(pygame.transform.scale(pygame.image.load(image_path2), (200, 200)))
    character_p1.append(pygame.transform.scale(pygame.image.load(image_path3), (200, 200)))

    character_p2 = character_p1[:]

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
    back_button = Button(720, 40, 90, 40, 10, (165, 167, 199), 'home')
    back_button.create_button(screen, mouse)

    pygame.font.init()
    path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
    text = pygame.font.Font(path, 20)

    # selection buttons
    pygame.draw.ellipse(screen, (147, 149, 186), (195, 175, 15, 15), 0)
    pygame.draw.ellipse(screen, (147, 149, 186), (225, 175, 15, 15), 0)
    pygame.draw.ellipse(screen, (147, 149, 186), (255, 175, 15, 15), 0)

    if (curr1 == 0):
        pygame.draw.ellipse(screen, (255, 255, 255), (195, 175, 15, 15), 2)
        screen.blit(text.render("Pink Monster", False, (237, 238, 255)), (155, 515))
    if (curr1 == 1):
        pygame.draw.ellipse(screen, (255, 255, 255), (225, 175, 15, 15), 2)
        screen.blit(text.render("Owlet Monster", False, (237, 238, 255)), (150, 515))
    if (curr1 == 2):
        pygame.draw.ellipse(screen, (255, 255, 255), (255, 175, 15, 15), 2)
        screen.blit(text.render("Dude Monster", False, (237, 238, 255)), (155, 515))

    pygame.draw.ellipse(screen, (147, 149, 186), (525, 175, 15, 15), 0)
    pygame.draw.ellipse(screen, (147, 149, 186), (555, 175, 15, 15), 0)
    pygame.draw.ellipse(screen, (147, 149, 186), (585, 175, 15, 15), 0)

    if (curr2 == 0):
        pygame.draw.ellipse(screen, (255, 255, 255), (525, 175, 15, 15), 2)
        screen.blit(text.render("Pink Monster", False, (237, 238, 255)), (490, 515))
    if (curr2 == 1):
        pygame.draw.ellipse(screen, (255, 255, 255), (555, 175, 15, 15), 2)
        screen.blit(text.render("Owlet Monster", False, (237, 238, 255)), (485, 515))
    if (curr2 == 2):
        pygame.draw.ellipse(screen, (255, 255, 255), (585, 175, 15, 15), 2)
        screen.blit(text.render("Dude Monster", False, (237, 238, 255)), (490, 515))

    screen.blit(character_p1[curr1], (130, 220))
    screen.blit(character_p2[curr2], (460, 220))

def customizations_clicks(mode, mouse, curr1, curr2):
    # back button
    if mouse_tact(720, 40, 90, 40, mouse):
        return (mouse_click(720, 40, 90, 40, 1, mouse, mode), curr1, curr2)
    if mouse_tact(330, 180, 50, 40, mouse) and curr1 < 2:
        curr1 += 1
    if mouse_tact(130, 180, 50, 40, mouse) and curr1 > 0:
        curr1 -= 1
    if mouse_tact(660, 180, 50, 40, mouse) and curr2 < 2:
        curr2 += 1
    if mouse_tact(460, 180, 50, 40, mouse) and curr2 > 0:
        curr2 -= 1
    return (mode, curr1, curr2)

# gameover ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gameover(screen, winner, mouse):
    # background colour - dim purple
    screen.fill((75, 76, 117))
    path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
    title_font = pygame.font.Font(path, 100)
    title = title_font.render("Gameover", False, (237, 238, 255))
    end_font = pygame.font.Font(path, 30)
    end = end_font.render(f"{winner} has won the game!", False, (237, 238, 255))
    screen.blit(title, (100, 90))
    screen.blit(end, (100, 200))

    # exit button
    exit_button = Button(270, 400, 250, 40, 10, (171, 174, 222), 'exit')
    exit_button.create_button(screen, mouse)

def gameover_clicks(mode, mouse):
    if mouse_tact(270, 400, 250, 40, mouse):
        return mouse_click(270, 400, 250, 40, 707, mouse, mode)
    
# Buttons ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

# GIF ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Gif():
    x: float
    y: float
    w: float
    h: float
    speed: float
    frames: int
    images: list
    j: int

    def __init__(self, x, y, w, h, frames, png_type):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.images = []
        self.counter = 0
        self.j = 0
        for i in range(frames):
            im = pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"{png_type} {i}.png")), (100, 100))
            self.images.append(im)
        
    def show(self, screen, counter, x, y, player):
        im = self.images[self.j]
        if player == 2:
            im = pygame.transform.flip(self.images[self.j], True, False)
        screen.blit(im, (x, y))
        if counter % 10 == 0:
            self.j += 1
        if self.j == len(self.images):
            self.j = 0

# mouse helper functions
def mouse_tact(x, y, w, h, mouse) -> bool:
    if (x - w/2 <= mouse[0] <= x + w/2) and (y - h/2 <= mouse[1] <= y + h/2):
        return True
    return False

def mouse_click(x, y, w, h, newMode, mouse, mode) -> int:
    if (x - w/2 <= mouse[0] <= x + w/2) and (y - h/2 <= mouse[1] <= y + h/2):
        return newMode
    return mode