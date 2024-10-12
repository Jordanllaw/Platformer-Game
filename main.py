# main
import pygame
import os
import math
import interface, game
from player import Player

mode = 0
INTRO = 1
SETTINGS = 2
INSTRUCTIONS = 3
CUSTOMIZATIONS = 4
GAME = 5
GAMEOVER = 6

mode = INTRO

# initializing game start
pygame.init()
clock = pygame.time.Clock()

# initializing screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

p1 = Player(50, 220, 'Pink Monster', 1)
p2 = Player(700, 220, 'Dude Monster', 2)
test = interface.Gif(500, 300, 150, 150, 8, 'Dude Monster Death')

p1_rocks = []
p2_rocks = []

running = True
<<<<<<< HEAD
counter = 0
=======
game.game(screen, p1, p2)
>>>>>>> 312b84aa68c77f37216e38888b471c408a8becd4

while running: 
    screen.fill('white')
    mouse = pygame.mouse.get_pos()

    if mode == INTRO:
        interface.intro(screen, mouse, counter, test)

    elif mode == SETTINGS:
        interface.settings(screen, mouse)

    elif mode == INSTRUCTIONS:
        interface.instructions(screen, mouse)

    elif mode == CUSTOMIZATIONS:
        interface.customizations(screen, mouse, interface.curr_char1, interface.curr_char2)

    elif mode == GAME:
        game.game(screen, p1, p2)

    elif mode == GAMEOVER:
        interface.gameover()

    else:
        print("Error: Mode = " + str(mode))

<<<<<<< HEAD
    counter += 1
=======
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

    if p1.death or p2.death:
        mode = GAMEOVER

>>>>>>> 312b84aa68c77f37216e38888b471c408a8becd4
# for loop through the event queue   
    for event in pygame.event.get():
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

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
            else:
                print("Error: Mode = " + str(mode))
    pygame.display.update()
    clock.tick(60)
