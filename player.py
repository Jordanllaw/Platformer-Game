import pygame
import os

class GameObject():
    x: float
    y: float
    im_path: str
    
    def __init__(self, x, y, im_path):
        self.x = x
        self.y = y
        self.im_path = im_path

    def show(self, screen, x, y):
        screen.blit(pygame.transform.scale(pygame.image.load(self.im_path), (100, 100)), (x, y))
    
    def show_flipped(self, screen, x, y):
        screen.blit(pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.im_path), (100, 100)), True, False), (x, y))
    
    def act(self):
        pass

class Rock(GameObject):

    def __init__(self, x, y, im_path=os.path.join(os.getcwd(), "Assets", "Rock2.png")):
        GameObject.__init__(self, x, y, im_path)
        self.im_path = im_path
        self.img = pygame.transform.scale(pygame.image.load(self.im_path), (20, 20))

    def summon(self, screen, player):
        screen.blit(self.img, (self.x, self.y))

    def rect(self):
        return pygame.Rect(self.x, self.y, 20, 20)

class Player(GameObject):
    akey, wkey, dkey, skey, left_key, up_key, right_key, down_key = False, False, False, False, False, False, False, False
    x: float
    y: float
    char_images: list
    char_type: str
    player: int
    action: str

    def __init__(self, x, y, char_type, player):
        if char_type == 'Pink Monster':
            GameObject.__init__(self, x, y, os.path.join(os.getcwd(), "Assets", "P1.png"))
        if char_type == 'Owlet Monster':
            GameObject.__init__(self, x, y, os.path.join(os.getcwd(), "Assets", "P2.png"))
        if char_type == 'Dude Monster':
            GameObject.__init__(self, x, y, os.path.join(os.getcwd(), "Assets", "P3.png"))
        self.char_type = char_type
        self.player = player
        self.health = 4
        self.death = False

    def rect(self):
        return pygame.Rect(self.x, self.y, 80, 100)

    def show(self, screen, counter, gif):
        # GameObject.show(self, screen, self.x, self.y)
        gif.show(screen, counter, self.x, self.y, 1)

    def show_flipped(self, screen, counter, gif):
        # GameObject.show_flipped(self, screen, self.x, self.y)
        gif.show(screen, counter, self.x, self.y, 2)

    def act(self):
        if self.player == 1:
            if self.dkey and self.x < 725:
                self.x += 3
            if self.akey and self.x > -25:
                self.x -= 3
            if self.wkey and self.y > -10:
                self.y -= 3
            if self.skey and self.y < 490:
                self.y += 3

        if self.player == 2:
            if self.right_key and self.x < 725:
                self.x += 3
            if self.left_key and self.x > -25:
                self.x -= 3
            if self.up_key and self.y > -10:
                self.y -= 3
            if self.down_key and self.y < 490:
                self.y += 3

    def attack(self, screen):
        rock_item = Rock(self.x, self.y)
        rock_item.summon(screen, self)
        return rock_item
    
    def take_hit(self):
        self.health -= 1
        if self.health == 0:
            self.death = True
          
