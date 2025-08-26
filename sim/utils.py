import math
import pygame 
from pygame.math import Vector2 


def normalise(v):
    tots = v.x**2 + v.y**2
    normalised_vector = v / math.sqrt(tots)
    return normalised_vector