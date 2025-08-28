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

    def generate_sensors(self,n):
        angles = [(-SENSOR_FOV)/2 + i * (SENSOR_FOV/(n-1)) for i in range(n)
                  ]
        d_center = Vector2(self.pos + (DRONE_SIZE/2, DRONE_SIZE/2))

        self.sens_start_end = []

        for angle in angles:
            normalised_direction = normalise(self.direction)
            ray_direction = normalised_direction.rotate(angle)
            endpoint = d_center + ray_direction * SENSOR_LENGHT
            self.sens_start_end.append((d_center, endpoint))

    def draw_sensors(self, screen):
        for i in self.sens_start_end:
            pygame.draw.line(screen, COLOURS["GREEN"], i[0], i[1])
    
    def sens_dist(self,screen,obstacles):
        
        for i in self.sens_start_end:
            for obstacle in obstacles:
                hit_end = obstacle.clipline(i[0], i[1])
                if hit_end:
                    start, end = hit_end
                    pygame.draw.line(screen, COLOURS["BLUE"], start, end)

        

            



    


        

