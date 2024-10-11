import pygame
import os

class GameObject():

    x: int
    y: int
    dx: int
    dy: int
    image_path: str

    def __init__(self, x, y, dx, dy, image_path):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.image_path = image_path

    def show(self, screen, x, y, height, width):
        screen.blit(pygame.transform.scale(pygame.image.load(self.image_path), (height, width)), (x, y))

    def show_flipped(self, screen, x, y, height, width):
        screen.blit(pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.image_path), (width, height)), True, False), (x, y))

    def update_position(self):
        if (self.dx < 0 and self.x > 0) or (self.dx > 0 and self.x < 800):
            self.x += self.dx
        elif (self.dy < 0 and self.y > 0) or (self.dy > 0 and self.y < 600):
            self.y += self.dy

    def move(self, dx, dy):
        if (dx < 0 and self.x > 0) or (dx > 0 and self.x < 800):
            self.x += dx
        elif (dy < 0 and self.y > 0) or (dy > 0 and self.y < 600):
            self.y += dy

class Ground(GameObject):

    def __init__(self, x, y, dx, dy, image_path):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.image_path = image_path


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
    '        MMMXXXXXXXXXXXXXXXXXXMMM        ',
    '        XbbbbbbbbbbbbbbbbbbbbbbX        ',
    '      sbb                      bbs      ',
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
    'MMMM        ssbb        bbss        MMMM',
    'bbbb                                bbbb',
    '                                        ',
    '      MMMM        MMMM        MMMM      ',
    '      XXXX  MMMM  XXXX  MMMM  XXXX      '
]

ground_pieces = []
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
                ground_pieces.append(Ground(x, y, 0, 0, os.path.join(os.getcwd(), 'Assets', 'M.png')))
            elif square == 'w':
                screen.blit(s, (x, y), pygame.Rect(x, y, 20, 20))
            elif square != ' ':
                ground_pieces.append(Ground(x, y, 0, 0, os.path.join(os.getcwd(), 'Assets', f'{square}.png')))
                image_path = os.path.join(os.getcwd(), 'Assets', f'{square}.png')
                image = pygame.transform.scale(pygame.image.load(image_path), (20, 20))
                screen.blit(image, (x, y))

def game(screen):
    # background colour - dim purple
    screen.fill((75, 76, 117))
    setupWorld(screen)