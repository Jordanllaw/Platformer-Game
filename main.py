# main
import pygame
import os
import baseGame, interface, pickups, player
import interface, pickups, player, baseGame

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

screen.fill('white')

# Game layout template
# 40 x 30
layout = [
    '                   43                   ',
    '                   21                   ',
    '                  XXXX                  ',
    '                                        ',
    '           MMMwwwwwwwwwwwwMMM           ',
    '        sssbbbbbbbbbbbbbbbbbbsss        ',
    '                                        ',
    ' ssss                              ssss ',
    '           MMwwwwwwwwwwwwwwMM           ',
    '       MMMMXXXXXXXXXXXXXXXXXXMMMM       ',
    '       XXbbbbbbbbbbbbbbbbbbbbbbXX       ',
    '     ssbb                      bbss     ',
    'P                                      P',
    'MMMM              MMMM              MMMM',
    'bbbb          MMMMXXXXMMMM          bbbb',
    '              bbbbXXXXbbbb              ',
    '                  bbbb                  ',
    '     MMMM                      MMMM     ',
    '     XXXX                      XXXX     ',
    '     XXXXMMMM  ss      ss  MMMMXXXX     ',
    '     bbbbbbbb              bbbbbbbb     ',
    '                   MM                   ',
    '                MMMXXMMM                ',
    '              MMXXXXXXXXMM              ',
    '              XXbbbbbbbbXX              ',
    'MMMM        MMXX        XXMM        MMMM',
    'bbbb        bbbb        bbbb        bbbb',
    '                                        ',
    '      MMMM        MMMM        MMMM      ',
    '      XXXX  MMMM  XXXX  MMMM  XXXX      '
]

def setupWorld(layout):
    # setting game background
    bg_path = os.path.join(os.getcwd(), 'Assets', 'Platformer Background.png')
    bg = pygame.transform.scale(pygame.image.load(bg_path), (800, 600))
    screen.blit(bg, (0, 0))

    # setting transparency
    s = pygame.Surface((600, 800), pygame.SRCALPHA)
    s.fill((64, 81, 100, 200))
    tile_size = 20
    for row_index, row in enumerate(layout):
        for col_index, square in enumerate(row):
            x, y = col_index * tile_size, row_index * tile_size
            if square == 'X':
                pygame.draw.rect(screen, (32, 28, 44), pygame.Rect(x, y, 20, 20))
            elif square == 'w':
                screen.blit(s, (x, y), pygame.Rect(x, y, 20, 20))
            elif square != ' ':
                image_path = os.path.join(os.getcwd(), 'Assets', f'{square}.png')
                image = pygame.transform.scale(pygame.image.load(image_path), (20, 20))
                screen.blit(image, (x, y))

# mouse helper functions
def mouse_tact(x, y, w, h) -> bool:
    if (x - w/2 <= mouse[0] <= x + w/2) and (y - h/2 <= mouse[1] <= y + h/2):
        return True
    return False

def mouse_click(x, y, w, h, newMode) -> int:
    if (x - w/2 <= mouse[0] <= x + w/2) and (y - h/2 <= mouse[1] <= y + h/2):
        return newMode
    return mode

# setupWorld(layout)

running = True

while running: 
# for loop through the event queue   
    for event in pygame.event.get(): 
        print("FKLSJDFLKJKLSDJF")
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

        mouse = pygame.mouse.get_pos()

        if mode == INTRO:
            interface.intro()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode = interface.intro_clicks()
                if mode == 707:
                    running = False
        elif mode == SETTINGS:
            interface.settings()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode = interface.settings_clicks()
        elif mode == INSTRUCTIONS:
            interface.instructions()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode = interface.instructions_clicks()
        elif mode == CUSTOMIZATIONS:
            interface.customizations()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode = interface.customizations_clicks()
        elif mode == GAME:
            interface.game()
        elif mode == GAMEOVER:
            interface.gameover()
        else:
            print("Error: Mode = " + str(mode))
