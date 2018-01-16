# Snake Game
import pygame
import sys
import random
import time

# Check for initializing errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print(
        "(!) Had {0} initializing errors, exiting..." . format(check_errors[1])
    )
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")
# (6, 0)

# Play Surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake Game')
# time.sleep(5)

# Colors
red = pygame.Color(255, 0, 0)  # Game Over
green = pygame.Color(0, 255, 0)  # Snake
black = pygame.Color(0, 0, 0)  # Score
white = pygame.Color(255, 255, 255)  # Background
brown = pygame.Color(165, 42, 42)  # Food

# FPS Controller
fspController = pygame.time.Clock()

# Important variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction


# Game Over Function
def gameOver():
    myFont = pygame.font.SysFont('source code pro', 72)
    GOSurface = myFont.render('Game Over!', True, red)
    GOrect = GOSurface.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOSurface, GOrect)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()  # pygame exit
    sys.exit()  # console exit


# Main Logic of The Game
