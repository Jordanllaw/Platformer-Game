import pygame
import os

class GameObject():

    def __init__(self, x, y, dx, dy, image_path):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.path = image_path

    def show(self, screen, x, y, height, width):
        screen.blit(pygame.transform.scale(pygame.image.load(self.path), (height, width)), (x, y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


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

def setupWorld(screen):
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

def game(screen):
    # background colour - dim purple
    screen.fill((75, 76, 117))
    setupWorld(screen)