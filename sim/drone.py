import pygame
from pygame.math import Vector2
import numpy as np
import math
from .config import DRONE_SIZE, COLOURS, SENSOR_FOV, SENSOR_LENGHT, SENSOR_COUNT, TURN_RATE_DEG_PER_SEC, SCREEN_WIDTH, SCREEN_HEIGHT
from .utils import normalise, distance



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

    def _get_Rect(self):
        return pygame.Rect(int(self.pos.x), int(self.pos.y), DRONE_SIZE, DRONE_SIZE)

    def draw_drone(self, screen, H = False):
        drone_Rect = pygame.Rect(int(self.pos.x), int(self.pos.y), DRONE_SIZE, DRONE_SIZE)
        pygame.draw.rect(screen, COLOURS["BLACK"], drone_Rect)

        if H:
            pygame.draw.line(screen, COLOURS["RED"], self.pos + Vector2(5,5), self.pos + Vector2(5,5) + self.direction * 200)

    def sensors(self,screen,n, obstacles):
        # Generates sensors
        angles = [(-SENSOR_FOV)/2 + i * (SENSOR_FOV/(n-1)) for i in range(n)
                  ]
        d_center = Vector2(self.pos + (DRONE_SIZE/2, DRONE_SIZE/2))

        self.sens_start_end = []

        for angle in angles:
            normalised_direction = normalise(self.direction)
            ray_direction = normalised_direction.rotate(angle)
            endpoint = d_center + ray_direction * SENSOR_LENGHT
            self.sens_start_end.append((d_center, endpoint))
        
        # Manages what the sensors so during a collision with a Rect
        self.sensor_distance = []
        for i in self.sens_start_end:
            nearest_d = SENSOR_LENGHT
            nearest_hit = None
            for obstacle in obstacles:
                hit = obstacle.clipline(i[0], i[1])

                if hit:
                    clipped_start, clipped_end = hit
                    dist = distance(clipped_start, i[0])
                    if dist < nearest_d:
                        nearest_d = dist
                        nearest_hit = clipped_start
            
            if nearest_hit:
                pygame.draw.line(screen, COLOURS["GREEN"], i[0], nearest_hit, 1)
                pygame.draw.line(screen, COLOURS["BLUE"], nearest_hit, i[1], 3)
                self.sensor_distance.append(nearest_d)
            else:
                pygame.draw.line(screen, COLOURS["GREEN"], i[0], i[1])
                self.sensor_distance.append(SENSOR_LENGHT)

    def avoid(self, dt):
        smallest_distance, index = min((dist, idx) for idx, dist in enumerate(self.sensor_distance))
        turn_deg =  TURN_RATE_DEG_PER_SEC * dt
        gain = max(0, 1- smallest_distance / (0.75 * SENSOR_LENGHT))
        turn_deg *= gain

        if index < (SENSOR_COUNT/2) and smallest_distance < 0.75 * SENSOR_LENGHT:
            self.direction = self.direction.rotate(1 * turn_deg)
        elif index > (SENSOR_COUNT/2) and smallest_distance < 0.75 * SENSOR_LENGHT:
            self.direction = self.direction.rotate(-1 * turn_deg)
        elif index == SENSOR_COUNT/2 and smallest_distance < 0.5 * SENSOR_LENGHT:
            self.direction = self.direction.rotate(+15)
        elif index < (SENSOR_COUNT/2) or index > (SENSOR_COUNT/2) and smallest_distance > 0.85 * SENSOR_LENGHT:
            self.direction = normalise(self.direction)
        
    def mechanics(self, obstacles = None):
        key =  pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.direction = Vector2(1, 0)
        if key[pygame.K_LEFT]:
            self.direction = Vector2(-1, 0)
        if key[pygame.K_UP]:
            self.direction = Vector2(0, -1)
        if key[pygame.K_DOWN]:
            self.direction = Vector2(0, 1)
        if key[pygame.K_SPACE]:
            self.pos.x = 200
            self.pos.y = 200
            self.speed = 150
            self.direction = Vector2(0, 0)
        if key[pygame.K_w]:
            self.speed += 10
        if key[pygame.K_s]:
            self.speed -= 10
        
        # Boundry Conditions
        if self.pos.x >= SCREEN_WIDTH-10:
            self.direction = self.direction.rotate(180)
        elif self.pos.x <= 0:
            self.direction = self.direction.rotate(180)
        if self.pos.y >= SCREEN_HEIGHT - 10:
            self.direction = self.direction.rotate(180)
        elif self.pos.y <= 0:
            self.direction = self.direction.rotate(180)

        # Collision
        if obstacles:
            rects = self._get_Rect()
            hit_index = rects.collidelist(obstacles)
            if hit_index != -1:
                self.speed = 0
        


    


        

