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

class Player(GameObject):
    akey, wkey, dkey, skey, left_key, up_key, right_key, down_key = False, False, False, False, False, False, False, False
    x: float
    y: float
    char_images: list
    char_type: str
    player: int

    def __init__(self, x, y, char_type, player):
        if char_type == 'Pink Monster':
            GameObject.__init__(self, x, y, os.path.join(os.getcwd(), "Assets", "P1.png"))
        if char_type == 'Owlet Monster':
            GameObject.__init__(self, x, y, os.path.join(os.getcwd(), "Assets", "P2.png"))
        if char_type == 'Dude Monster':
            GameObject.__init__(self, x, y, os.path.join(os.getcwd(), "Assets", "P3.png"))
        self.char_type = char_type
        self.player = player

    def show(self, screen):
        GameObject.show(self, screen, self.x, self.y)

    def show_flipped(self, screen):
        GameObject.show_flipped(self, screen, self.x, self.y)

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


        
          
