# main
import pygame
import os
import math
import interface, game
import sys
from player import Player
from player import Dot
import random

mode = 0
INTRO = 1
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

p1 = Player(1, 220, 'Pink Monster', 1)
p2 = Player(700, 220, 'Dude Monster', 2)

circle_size = 6
num_circles = 7
dots = []
for i in range(num_circles):
    circle = {'x': random.randrange(circle_size, screen_width - circle_size), 
            'y': random.randrange(circle_size, screen_height - circle_size),
            'dx': random.randrange(-3, 3),
            'dy': random.randrange(-3, 3),
            'colour': (120, 27, 8)}
    dots.append(Dot(circle['x'], circle['y'], None, circle['dx'], circle['dy'], circle['colour']))

p1_rocks = []
p2_rocks = []

counter = 0
counter_p1_act = 0
counter_p2_act = 0

die_GIF_dude = interface.Gif(p1.x, p1.y, 100, 100, 8, 'Dude Monster Death')
run_GIF_dude = interface.Gif(p2.x, p2.y, 100, 100, 6, 'Dude Monster Run')
run_GIF_dude2 = interface.Gif(p2.x, p2.y, 150, 150, 6, 'Dude Monster Run')
run_GIF_pink = interface.Gif(p2.x, p2.y, 100, 100, 6, 'Pink Monster Run')
run_GIF_owlet = interface.Gif(p2.x, p2.y, 100, 100, 6, 'Owlet Monster Run')
throw_GIF_dude = interface.Gif(p2.x, p2.y, 100, 100, 4, 'Dude Monster Throw')
throw_GIF_pink = interface.Gif(p2.x, p2.y, 100, 100, 4, 'Pink Monster Throw')
throw_GIF_owlet = interface.Gif(p2.x, p2.y, 100, 100, 4, 'Owlet Monster Throw')

running = True

while running: 
    screen.fill('white')
    mouse = pygame.mouse.get_pos()  

    if mode == INTRO:
        interface.intro(screen, mouse, counter, run_GIF_dude2)

    elif mode == INSTRUCTIONS:
        interface.instructions(screen, mouse)

    elif mode == CUSTOMIZATIONS:
        interface.customizations(screen, mouse, interface.curr_char1, interface.curr_char2)

    elif mode == GAME:
        type1 = interface.customizations(screen, mouse, interface.curr_char1, interface.curr_char2)[0]
        type2 = interface.customizations(screen, mouse, interface.curr_char1, interface.curr_char2)[1]
        game.game(screen, p1, p2, counter, run_GIF_pink, run_GIF_owlet, run_GIF_dude, throw_GIF_pink, throw_GIF_owlet, throw_GIF_dude, type1, type2)
        for shape in dots[:]:
            shape.x += shape.dx
            shape.y += shape.dy

            if shape.x < 0 or shape.x > screen_width - circle_size:
                shape.dx *= -1
            if shape.y < 0 or shape.y > screen_height - circle_size:
                shape.dy *= -1

            if shape.rect().colliderect(p1.rect()):
                p1.take_hit()
                dots.remove(shape)
            if shape.rect().colliderect(p2.rect()):
                p2.take_hit()
                dots.remove(shape)

            pygame.draw.circle(screen, shape.colour, (shape.x, shape.y), circle_size)


    elif mode == GAMEOVER:
        if p1.death: 
            winner = 'Player Two'
        else:
            winner = 'Player One'
        interface.gameover(screen, winner, mouse, counter, die_GIF_dude)

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

    if p1.action == 'throw':
        counter_p1_act += 1
        if counter_p1_act == 40:
            counter_p1_act = 0
            p1.action = 'run'
    if p2.action == 'throw':
        counter_p2_act += 1
        if counter_p2_act == 40:
            counter_p2_act = 0
            p2.action = 'run'
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
                p1_rocks.append(p1.attack(screen, counter_p1_act))
            if event.key == pygame.K_LEFT:
                Player.left_key = True
            if event.key == pygame.K_UP:
                Player.up_key = True
            if event.key == pygame.K_RIGHT:
                Player.right_key = True
            if event.key == pygame.K_DOWN:
                Player.down_key = True
            if event.key == pygame.K_SPACE:
                p2_rocks.append(p2.attack(screen, counter_p2_act))

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

            elif mode == INSTRUCTIONS:
                mode = interface.instructions_clicks(mode, mouse)

            elif mode == CUSTOMIZATIONS:
                result = interface.customizations_clicks(mode, mouse, interface.curr_char1, interface.curr_char2)
                mode = result[0]
                interface.curr_char1 = result[1]
                interface.curr_char2 = result[2]
            
            elif mode == GAME:
                pass

            elif mode == GAMEOVER:
                mode = interface.gameover_clicks(mode, mouse)
                if mode == 707:
                    running = False
            else:
                print("Error: Mode = " + str(mode))
    pygame.display.update()
    clock.tick(60)
