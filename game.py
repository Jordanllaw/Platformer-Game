import pygame
import player
import os

def setupWorld(screen):
    # background colour - dim purple
    screen.fill((75, 76, 117))

def game(screen, p1, p2, counter, gif):
    # background colour - dim purple
    screen.fill((75, 76, 117))
    setupWorld(screen)

    p1.show(screen, counter, gif)
    p1.act()
    p2.show_flipped(screen, counter, gif)
    p2.act()
      