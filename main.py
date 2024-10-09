# main
import pygame

# Game layout template
# 40 x 30
layout = [
    '                   pp                   ',
    '                   pp                   ',
    '                  XXXX                  ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '         XXwwwwwwwwwwwwwwwwwwXX         ',
    '       XXXXXXXXXXXXXXXXXXXXXXXXXX       ',
    '       XXXXXXXXXXXXXXXXXXXXXXXXXX       ',
    '     XXXX                      XXXX     ',
    '                                        ',
    'XXXX              XXXX              XXXX',
    'XXXX          XXXXXXXXXXXX          XXXX',
    '              XXXXXXXXXXXX              ',
    '                  XXXX                  ',
    '     XXXX                      XXXX     ',
    '     XXXX                      XXXX     ',
    '     XXXXXXX   ss      ss   XXXXXXX     ',
    '     XXXXXXX                XXXXXXX     ',
    'tt                 XX                 tt',
    'tt              XXXXXXXX              tt',
    'tt            XXXXXXXXXXXX            tt',
    'tt            XXXXXXXXXXXX            tt',
    'XXXX        XXXX        XXXX        XXXX',
    'XXXX        XXXX        XXXX        XXXX',
    '                                        ',
    '      XXXX        XXXX        XXXX      ',
    '      XXXX  XXXX  XXXX  XXXX  XXXX      '
]

def setupWorld(layout):
    tile_size = 20
    for row_index, row in enumerate(layout):
        for col_index, square in enumerate(row):
            x, y = col_index * tile_size, row_index * tile_size
            if square == 'X':
                pygame.draw.rect(screen, 'blue', pygame.Rect(x, y, 20, 20))
            if square == 'p':
                pygame.draw.rect(screen, 'red', pygame.Rect(x, y, 20, 20))
            if square == 's':
                pygame.draw.rect(screen, 'pink', pygame.Rect(x, y, 20, 20))
            if square == 't':
                pygame.draw.rect(screen, 'green', pygame.Rect(x, y, 20, 20))
            if square == 'w':
                pygame.draw.rect(screen, 'light blue', pygame.Rect(x, y, 20, 20))
    pygame.display.flip()

# initializing game start
pygame.init()
clock = pygame.time.Clock()

# initializing screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

screen.fill((0, 0, 0))
pygame.display.flip()

running = True

setupWorld(layout)

while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
