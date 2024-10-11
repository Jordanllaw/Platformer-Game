import pygame
from baseGame import GameObject
import os

class Player(GameObject):

    x: int
    y: int
    dx: int
    dy: int
    char_type: str
    health: int
    isJump: bool
    left: bool
    right: bool
    og_ground: bool

    def __init__(self, x, y, dx, dy, char_type, screen, image_path):
        GameObject.__init__(self, x, y, dx, dy, image_path)
        self.screen = screen
        self.on_ground = False
        self.isJump = False
        self.left = False
        self.right = False
        self.char_type = char_type
        self.health = 3
        self.inventory = []
        self.idleleft = []
        for i in range(0, 4):
            self.idleleft.append(pygame.transform.flip(pygame.image.load(os.path.join(os.getcwd(), "Assets", f"{char_type} Idle {i}.png")), True, False))
        self.idleright = []
        for i in range(0, 4):
            self.idleright.append(pygame.image.load(os.path.join(os.getcwd(), "Assets", f"{char_type} Idle {i}.png")))
        self.attackleft = []
        for i in range(0, 4):
            self.attackleft.append(pygame.transform.flip(pygame.image.load(os.path.join(os.getcwd(), "Assets", f"{char_type} Attack {i}.png")), True, False))
        self.attackright = []
        for i in range(0, 4):
            self.attackright.append(pygame.image.load(os.path.join(os.getcwd(), "Assets", f"{char_type} Attack {i}.png")))
        self.runleft = []
        for i in range(0, 6):
            self.runleft.append(pygame.transform.flip(pygame.image.load(os.path.join(os.getcwd(), "Assets", f"{char_type} Run {i}.png")), True, False))
        self.runright = []
        for i in range(0, 6):
            self.runright.append(pygame.image.load(os.path.join(os.getcwd(), "Assets", f"{char_type} Run {i}.png")))
        self.walkleft = []
        for i in range(0, 6):
            self.walkleft.append(pygame.transform.flip(pygame.image.load(os.path.join(os.getcwd(), "Assets", f"{char_type} Walk {i}.png")), True, False))
        self.walkright = []
        for i in range(0, 6):
            self.walkright.append(pygame.image.load(os.path.join(os.getcwd(), "Assets", f"{char_type} Walk {i}.png")))
        self.jumpleft = []
        for i in range(0, 8):
            self.jumpleft.append(pygame.transform.flip(pygame.image.load(os.path.join(os.getcwd(), "Assets", f"{char_type} Jump {i}.png")), True, False))
        self.jumpright = []
        for i in range(0, 8):
            self.jumpright.append(pygame.image.load(os.path.join(os.getcwd(), "Assets", f"{char_type} Jump {i}.png")))
        self.death = []
        for i in range(0, 7):
            self.death.append(pygame.image.load(os.path.join(os.getcwd(), "Assets", f"{char_type} Death {i}.png")))

    def pickup(self, object: GameObject):
        self.inventory.append(object)

    def die(self):
        offset = 0
        for item in self.inventory:
            item.show(self.screen, self.x + offset, self.y, 20, 20)
            offset += 10
        self.inventory = []
        self.health = 3

    def getHit(self, x, y):
        self.health -= 1
        if self.health == 0:
            self.die(x, y)
            
