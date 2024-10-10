import pygame
import baseGame

class Player(baseGame.GameObject):

    x: int
    y: int
    dx: int
    dy: int
    image_path: str
    char_type: str
    health: int

    def __init__(self, x, y, dx, dy, image_path, char_type):
        self.char_type = char_type
        self.health = 3
        self.inventory = []
        self.idleleft = []
        for i in range(0, 4):
            self.idleleft.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", f"{char_type} Idle {i}")), True))
        self.idleright = []
        for i in range(0, 4):
            self.idleright.append(pygame.image.load(os.path.join("Assets", f"{char_type} Idle {i}")))
        self.attackleft = []
        for i in range(0, 4):
            self.attackleft.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", f"{char_type} Attack {i}")), True))
        self.attackright = []
        for i in range(0, 4):
            self.attackright.append(pygame.image.load(os.path.join("Assets", f"{char_type} Attack {i}")))
        self.runleft = []
        for i in range(0, 6):
            self.runleft.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", f"{char_type} Run {i}")), True))
        self.runright = []
        for i in range(0, 6):
            self.runright.append(pygame.image.load(os.path.join("Assets", f"{char_type} Run {i}")))
        self.walkleft = []
        for i in range(0, 6):
            self.walkleft.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", f"{char_type} Walk {i}")), True))
        self.walkright = []
        for i in range(0, 6):
            self.walkright.append(pygame.image.load(os.path.join("Assets", f"{char_type} Walk {i}")))
        self.jumpleft = []
        for i in range(0, 8):
            self.jumpleft.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", f"{char_type} Jump {i}")), True))
        self.jumpright = []
        for i in range(0, 8):
            self.jumpright.append(pygame.image.load(os.path.join("Assets", f"{char_type} Jump {i}")))

    def die(self, x, y):
        # animation
        # drop inventory stuff
        self.inventory = []
        self.health = 3

    def getHit(self, x, y):
        self.health -= 1
        if self.health == 0:
            self.die(x, y)

running = True

pygame.init()
clock = pygame.time.Clock()

# initializing screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

screen.fill('white')
pygame.display.flip()

while running: 
# for loop through the event queue   
    for event in pygame.event.get(): 

        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
