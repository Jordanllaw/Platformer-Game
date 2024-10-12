import pygame
from player import Player
import os

def game(screen, p1, p2, counter, gif):
    # background colour - dim purple
    screen.fill((73, 109, 140))

    # health for p1
    health_p3 = pygame.Rect(25, 45, 210, 40)
    pygame.draw.rect(screen, (55, 56, 59), health_p3, 0, 10)
    if p1.health == 4:
        health_p1 = pygame.Rect(30, 50, 200, 30)
    if p1.health == 3:
        health_p1 = pygame.Rect(30, 50, 150, 30)
    if p1.health == 2:
        health_p1 = pygame.Rect(30, 50, 100, 30)
    if p1.health == 1:
        health_p1 = pygame.Rect(30, 50, 50, 30)
    pygame.draw.rect(screen, (116, 196, 112), health_p1, 0, 10)

    # health for p2
    health_p3 = pygame.Rect(565, 45, 210, 40)
    pygame.draw.rect(screen, (55, 56, 59), health_p3, 0, 10)
    if p2.health == 4:
        health_p2 = pygame.Rect(570, 50, 200, 30)
    if p2.health == 3:
        health_p2 = pygame.Rect(570, 50, 150, 30)
    if p2.health == 2:
        health_p2 = pygame.Rect(570, 50, 100, 30)
    if p2.health == 1:
        health_p2 = pygame.Rect(570, 50, 50, 30)
    pygame.draw.rect(screen, (116, 196, 112), health_p2, 0, 10)

    p1.show(screen, counter, gif)
    p1.act()
    p2.show_flipped(screen, counter, gif)
    p2.act()
      