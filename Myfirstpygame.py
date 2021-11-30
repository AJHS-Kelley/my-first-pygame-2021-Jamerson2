# My first pygame, Jamerson Franklin, 11/30/21, 2:13pm, vo.2

import pygame, sys
from pygame.locals import *

# start pygame
pygame.init()

# setup the game window
windowsurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')