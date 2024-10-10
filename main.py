# main
import pygame
import os
import baseGame, interface, pickups

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

running = True

while running: 
# for loop through the event queue   
    for event in pygame.event.get():
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

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

        elif mode == GAMEOVER:
            interface.gameover()

        else:
            print("Error: Mode = " + str(mode))
        pygame.display.flip()
