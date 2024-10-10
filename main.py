# main
import pygame
import os
import baseGame.py, interface.py, pickups.py, player.py

# initializing game start
pygame.init()
clock = pygame.time.Clock()

# initializing screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

screen.fill('white')
pygame.display.flip()

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
    '                                        ',
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
    pygame.display.flip()

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

setupWorld(layout)
pygame.display.flip()

running = True

while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
    
