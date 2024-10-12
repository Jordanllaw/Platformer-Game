# main
import pygame
import os
import math
import interface, game
import sys
from player import Player

mode = 0
INTRO = 1
SETTINGS = 2
INSTRUCTIONS = 3
CUSTOMIZATIONS = 4
GAME = 5
GAMEOVER = 6

mode = GAMEOVER

# initializing game start
pygame.init()
clock = pygame.time.Clock()

# initializing screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

p1 = Player(50, 220, 'Pink Monster', 1)
p2 = Player(700, 220, 'Dude Monster', 2)

p1_rocks = []
p2_rocks = []

counter = 0

die_GIF_dude = interface.Gif(p1.x, p1.y, 100, 100, 8, 'Dude Monster Death')
hurt_GIF_dude = interface.Gif(p2.x, p2.y, 100, 100, 4, 'Dude Monster Hurt')
run_GIF_dude = interface.Gif(p2.x, p2.y, 100, 100, 6, 'Dude Monster Run')

running = True

while running: 
    screen.fill('white')
    mouse = pygame.mouse.get_pos()

    if mode == INTRO:
        interface.intro(screen, mouse, counter, hurt_GIF_dude)

    elif mode == SETTINGS:
        interface.settings(screen, mouse)

    elif mode == INSTRUCTIONS:
        interface.instructions(screen, mouse)

    elif mode == CUSTOMIZATIONS:
        interface.customizations(screen, mouse, interface.curr_char1, interface.curr_char2)

    elif mode == GAME:
        game.game(screen, p1, p2, counter, run_GIF_dude)

    elif mode == GAMEOVER:
        if p1.death: 
            winner = 'Player Two'
        else:
            winner = 'Player One'
        interface.gameover(screen, winner, mouse)

    else:
        print("Error: Mode = " + str(mode))

    for obj in p1_rocks[:]:
            obj.x += 5
            screen.blit(obj.img, (obj.x, obj.y))
            if -20 >= obj.x >= 800:
                p1_rocks.remove(obj)
            if obj.rect().colliderect(p2.rect()):
                p2.take_hit()
                p1_rocks.remove(obj)

    for obj in p2_rocks[:]:
        obj.x -= 5
        screen.blit(obj.img, (obj.x, obj.y))
        if -20 >= obj.x >= 800:
            p2_rocks.remove(obj)
        if obj.rect().colliderect(p1.rect()):
            p1.take_hit()
            p2_rocks.remove(obj)

    counter += 1

    if p1.death or p2.death:
        p1_rocks = []
        p2_rocks = []
        mode = GAMEOVER

# for loop through the event queue   
    for event in pygame.event.get():
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Player.akey = True
            if event.key == pygame.K_w:
                Player.wkey = True
            if event.key == pygame.K_d:
                Player.dkey = True
            if event.key == pygame.K_s:
                Player.skey = True
            if event.key == pygame.K_q:
                p1_rocks.append(p1.attack(screen))
            if event.key == pygame.K_LEFT:
                Player.left_key = True
            if event.key == pygame.K_UP:
                Player.up_key = True
            if event.key == pygame.K_RIGHT:
                Player.right_key = True
            if event.key == pygame.K_DOWN:
                Player.down_key = True
            if event.key == pygame.K_SPACE:
                p2_rocks.append(p2.attack(screen))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                Player.akey = False
            if event.key == pygame.K_w:
                Player.wkey = False
            if event.key == pygame.K_d:
                Player.dkey = False
            if event.key == pygame.K_s:
                Player.skey = False
            if event.key == pygame.K_LEFT:
                Player.left_key = False
            if event.key == pygame.K_UP:
                Player.up_key = False
            if event.key == pygame.K_RIGHT:
                Player.right_key = False
            if event.key == pygame.K_DOWN:
                Player.down_key = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mode == INTRO:
                mode = interface.intro_clicks(mode, mouse)
                if mode == 707:
                    running = False

            elif mode == SETTINGS:
                mode = interface.settings_clicks(mode, mouse)

            elif mode == INSTRUCTIONS:
                mode = interface.instructions_clicks(mode, mouse)

            elif mode == CUSTOMIZATIONS:
                result = interface.customizations_clicks(mode, mouse, interface.curr_char1, interface.curr_char2)
                mode = result[0]
                interface.curr_char1 = result[1]
                interface.curr_char2 = result[2]

            elif mode == GAMEOVER:
                mode = interface.gameover_clicks(mode, mouse)
                if mode == 707:
                    running = False
            else:
                print("Error: Mode = " + str(mode))
    pygame.display.update()
    clock.tick(60)
