import pygame
from player import Player
import os

def game(screen, p1, p2, counter, gif, gif2, gif3, gifTh, gifTh2, gifTh3, p1_type, p2_type):
    # background colour - dim purple
    screen.fill((73, 109, 140))
    im_path = os.path.join(os.getcwd(), 'Assets', 'Background.jpg')
    screen.blit(pygame.transform.scale(pygame.image.load(im_path), (1200, 1000)), (-200, -200))

    pygame.font.init()
    path = os.path.join(os.getcwd(), 'Assets', 'TitleFont.ttf')
    title_font = pygame.font.Font(path, 20)
    title = title_font.render("Player 1 Health:", False, (237, 238, 255))
    screen.blit(title, (30, 20))

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

    title = title_font.render("Player 2 Health:", False, (237, 238, 255))
    screen.blit(title, (580, 20))

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

    if p1_type == 'pink':
        p1.show(screen, counter, gif, gifTh)
    if p1_type == 'owlet':
        p1.show(screen, counter, gif2, gifTh2)
    if p1_type == 'dude':
        p1.show(screen, counter, gif3, gifTh3)
    p1.act()
    if p2_type == 'pink':
        p2.show_flipped(screen, counter, gif, gifTh)
    if p2_type == 'owlet':
        p2.show_flipped(screen, counter, gif2, gifTh2)
    if p2_type == 'dude':
        p2.show_flipped(screen, counter, gif3, gifTh3)
    p2.act()
      