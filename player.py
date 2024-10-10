import pygame

class Player():

    health: int

    def __init__(self):
        self.health = 3
        self.inventory = []
        self.idle = []
        self.attack = []
        self.runleft = []
        self.runright = []

    def die(self, x, y):
        # animation
        # drop inventory stuff
        self.inventory = []
        self.health = 3

    def getHit(self, x, y):
        self.health -= 1
        if self.health == 0:
            self.die(x, y)