import pygame
from pygame.math import Vector2
import numpy as np
from .config import DRONE_SIZE, COLOURS, SENSOR_FOV, SENSOR_LENGHT, SENSOR_COUNT
from .utils import normalise



class Drone:
    def __init__(self):

        self.x = 200
        self.y = 200
        self.speed = float(150)
        self.pos = Vector2(self.x, self.y)
        self.direction = Vector2(1, 0)
        self.sensor_list = []

    def move_drone(self, dt):
    
        self.pos += self.direction * self.speed * dt 

    def get_Rect(self):
        return pygame.Rect(int(self.pos.x), int(self.pos.y), DRONE_SIZE, DRONE_SIZE)

    def draw_drone(self, screen):
        drone_Rect = pygame.Rect(int(self.pos.x), int(self.pos.y), DRONE_SIZE, DRONE_SIZE)
        pygame.draw.rect(screen, COLOURS["BLACK"], drone_Rect)

    def generate_sensors(self,n, screen):
        angles = [(-SENSOR_FOV)/2 + i * (SENSOR_FOV/(n-1)) for i in range(n)
                  ]
        d_center = Vector2(self.pos + (DRONE_SIZE/2, DRONE_SIZE/2))

        for angle in angles:
            normalised_direction = normalise(self.direction)
            ray_direction = normalised_direction.rotate(angle)
            endpoint = d_center + ray_direction * SENSOR_LENGHT
            pygame.draw.line(screen, COLOURS["GREEN"], d_center, endpoint)

    


        

