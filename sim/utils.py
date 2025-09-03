import math
import pygame 
from pygame.math import Vector2 


def normalise(v):
    tots = v.x**2 + v.y**2
    if tots == 0:
        return v
    normalised_vector = v / math.sqrt(tots)
    return normalised_vector


def distance(p1, p2):
    raw_dist_x = (p1[0] - p2[0])**2 
    raw_dist_y = (p1[1] - p2[1])**2
    
    dist =  math.sqrt(raw_dist_x + raw_dist_y)

    return dist


def centered_list(n):
    half = n//2
    return list(range(half, -half - 1, -1))
