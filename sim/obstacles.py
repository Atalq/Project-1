import pygame
from pygame.math import Vector2
from .config import SCREEN_HEIGHT,SCREEN_WIDTH, COLOURS, OBSTACLE_MAX_SIZE, OBSTACLE_MIN_SIZE
import random



class Obstacle:

    def __init__(self, x, y, w, h):
        self.pos = Vector2(x, y)
        self.w = int(w)
        self.h = int(h)
        self.colour = COLOURS["RED"]
        self.Rect = pygame.Rect(int(self.pos.x), int(self.pos.y), self.w, self.h)

    def draw_obstacle(self, screen):
        pygame.draw.rect(screen, self.colour, self.Rect)
        



class Obstacles:

    def __init__(self,n, seed=None):
        
        if seed != None:
            random.seed(seed)
        self.colour  = COLOURS["RED"]
        self.screen_w = SCREEN_WIDTH
        self.screen_h = SCREEN_HEIGHT
        self.margin = OBSTACLE_MAX_SIZE
        self.min_size = OBSTACLE_MIN_SIZE
        self.max_size = OBSTACLE_MAX_SIZE


        self.obsl = []
        self.Rects = []
        self._generate(n)

    def _generate(self, n):
        self.obsl.clear()
        self.Rects.clear()

        for i in range(n):
            w = random.randint(self.min_size, self.max_size)
            h = random.randint(self.min_size, self.max_size)
            x = random.randint(self.margin, self.screen_w - self.margin - w)
            y = random.randint(self.margin, self.screen_h - self.margin - h)

            ob = Obstacle(x, y, w, h)
            self.obsl.append(ob)
            self.Rects.append(ob.Rect)
        

    def regenerate(self, n):
        self._generate(n)


    def draw_obss(self, screen):
        for obstacle in self.obsl:
            obstacle.draw_obstacle(screen)

    def get_rects(self):
        return self.Rects
        