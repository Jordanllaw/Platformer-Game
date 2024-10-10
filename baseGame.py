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
