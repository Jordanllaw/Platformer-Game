# main
import pygame
import os
import math
import interface, pickups
from player import Player
from baseGame import GameObject
import baseGame

mode = 0
INTRO = 1
SETTINGS = 2
INSTRUCTIONS = 3
CUSTOMIZATIONS = 4
GAME = 5
GAMEOVER = 6

mode = INTRO

def check_collision(ob1: GameObject, ob2: GameObject):
    distance = math.sqrt((math.pow(ob1.x - ob2, 2)) + (math.pow(ob1.y - ob2.y, 2)))
    if distance <= 20:
        return True
    else:
        return False

# initializing game start
pygame.init()
clock = pygame.time.Clock()

# initializing screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

screen.fill('white')

p1 = Player(0, 220, 0, 0, 'Pink Monster', screen, os.path.join(os.getcwd(), "Assets", "P1.png"))
p2 = Player(760, 220, 0, 0, 'Dude Monster', screen, os.path.join(os.getcwd(), "Assets", "P3.png"))

running = True

while running: 
# for loop through the event queue   
    for event in pygame.event.get():
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                p2.dx = -5
            if event.type == pygame.K_RIGHT:
                p2.dx = 5
            if event.key == pygame.K_a:
                p1.dx = -5
            if event.key == pygame.K_d:
                p1.dx = 5
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                p2.dx = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                p1.dx = 0
        
        p1.update_position()
        p2.update_position()

        mouse = pygame.mouse.get_pos()

        if mode == INTRO:
            interface.intro(screen, mouse)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode = interface.intro_clicks(mode, mouse)
                if mode == 707:
                    running = False

        elif mode == SETTINGS:
            interface.settings(screen, mouse)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode = interface.settings_clicks(mode, mouse)

        elif mode == INSTRUCTIONS:
            interface.instructions(screen, mouse)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode = interface.instructions_clicks(mode, mouse)

        elif mode == CUSTOMIZATIONS:
            interface.customizations(screen, mouse, interface.curr_char1, interface.curr_char2)
            if event.type == pygame.MOUSEBUTTONDOWN:
                result = interface.customizations_clicks(mode, mouse, interface.curr_char1, interface.curr_char2)
                mode = result[0]
                interface.curr_char1 = result[1]
                interface.curr_char2 = result[2]

        elif mode == GAME:
            baseGame.game(screen)
            p1.show(screen, p1.x, p1.y, 40, 40)
            p2.show_flipped(screen, p2.x, p2.y, 40, 40)

        elif mode == GAMEOVER:
            interface.gameover()

        else:
            print("Error: Mode = " + str(mode))
        pygame.display.flip()
