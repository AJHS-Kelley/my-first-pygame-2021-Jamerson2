# My first pygame, Jamerson Franklin, 11/30/21, 2:13pm, vo.3

import pygame, sys
from pygame.locals import *

# start pygame
pygame.init()

# setup the game window
windowsurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DOODOOBROWN = (125, 255, 25)