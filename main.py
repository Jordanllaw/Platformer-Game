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
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    'XXXX                                XXXX',
    'XXXX                                XXXX',
    '                                        ',
    '                                        ',
    '       XX                      XX       ',
    '       XX                      XX       ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                 XXXXXX                 ',
    '              XX        XX              ',
    '                                        ',
    '          XX      XXXX      XX          ',
    '              XX  XXXX  XX              '
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
