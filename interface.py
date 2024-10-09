# main
import pygame

def intro():
    pygame.draw.rect(screen, 'blue', pygame.Rect(200, 200, 100, 100))
    pygame.display.flip()

def settings():
    pass

def instructions():
    pass

def customizations():
    pass

def game():
    pass

def gameover():
    pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mode = 0
INTRO = 1
SETTINGS = 2
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

screen.fill((0, 0, 0))

running = True

while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

        if mode == INTRO:
            intro()
        elif mode == SETTINGS:
            settings()
        elif mode == INSTRUCTIONS:
            instructions()
        elif mode == CUSTOMIZATIONS:
            customizations()
        elif mode == GAME:
            game()
        elif mode == GAMEOVER:
            gameover()
        else:
            print("Error: Mode = " + str(mode))
