import pygame
from pygame.math import Vector2
from .config import DRONE_SIZE, COLOURS



class Drone:
    def __init__(self):

        self.x = 200
        self.y = 200
        self.speed = float(150)
        self.pos = Vector2(self.x, self.y)
        self.direction = Vector2(1, 0)
          
    def move_drone(self, dt):
    
        self.pos += self.direction * self.speed * dt 

    def get_Rect(self):
        return pygame.Rect(int(self.pos.x), int(self.pos.y), DRONE_SIZE, DRONE_SIZE)

    def draw_drone(self, screen):
        drone_Rect = pygame.Rect(int(self.pos.x), int(self.pos.y), DRONE_SIZE, DRONE_SIZE)
        pygame.draw.rect(screen, COLOURS["BLACK"], drone_Rect)
