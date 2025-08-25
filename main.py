import pygame
import sys
from pygame.math import Vector2
import random


class Drone:
    def __init__(self):

        self.x = 200
        self.y = 200
        self.speed = 150
        self.pos = Vector2(self.x, self.y)
        self.direction = Vector2(1, 0)
          
    def move_drone(self, dt):
    
        self.pos += self.direction * self.speed * dt 


    def draw_drone(self, screen):
        drone_Rect = pygame.Rect(int(self.pos.x), int(self.pos.y), DRONE_SIZE, DRONE_SIZE)
        pygame.draw.rect(screen, BLACK, drone_Rect)

class Obstacle:

    def __init__(self, x, y, w, h):
        self.pos = Vector2(x, y)
        self.w = int(w)
        self.h = int(h)
        self.colour = RED
        self.Rect = pygame.Rect(int(self.pos.x), int(self.pos.y), self.w, self.h)

    def draw_obstacle(self, screen):
        pygame.draw.rect(screen, self.colour, self.Rect)
        
class Obstacles:

    def __init__(self,n, seed=None):
        
        if seed != None:
            random.seed(seed)
        self.colour  = RED
        self.screen_w = SCREEN_WIDTH
        self.screen_h = SCREEN_HEIGHT
        self.margin = 50
        self.min_size = 15
        self.max_size = 50


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
        


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
DRONE_SIZE = 10

def main():
        # Set up pygame 
    pygame.init()

    # drone object creation
    drone = Drone()
    obs1 = Obstacles(10)

        # Screen set up
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)

        # set up font 
    font1 = pygame.font.SysFont('Calibri', 30, True, False)
    font2 = pygame.font.SysFont('Calibri', 18, True, False)
    text = font1.render("Drone sim test", True, BLACK)
    

        # Clock
    clock = pygame.time.Clock()

        # Timer for the detection and implementation of the movement fo the drone 
    

    running = True 
    while running:
        
        for event in pygame.event.get():
            # To close program when X pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            
            
                

            
            # Key Combinations for each mechanic
            key =  pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
                drone.direction = Vector2(1, 0)
            if key[pygame.K_LEFT]:
                drone.direction = Vector2(-1, 0)
            if key[pygame.K_UP]:
                drone.direction = Vector2(0, -1)
            if key[pygame.K_DOWN]:
                drone.direction = Vector2(0, 1)
            if key[pygame.K_SPACE]:
                drone.pos.x = 200
                drone.pos.y = 200
                drone.speed = 150
                drone.direction = Vector2(0, 0)
            if key[pygame.K_w]:
                drone.speed += 10
            if key[pygame.K_s]:
                drone.speed -= 10

            # Edge (boundry) conditions
        if drone.pos.x >= SCREEN_WIDTH-10:
            drone.direction = Vector2(-1, 0)
        elif drone.pos.x <= 0:
            drone.direction = Vector2(1, 0)
        if drone.pos.y >= SCREEN_HEIGHT - 10:
            drone.direction = Vector2(0, -1)
        elif drone.pos.y <= 0:
            drone.direction = Vector2(0, 1)

            # Collisions 
        dt = clock.tick(60)/ 1000
        drone.move_drone(dt)   

        drone_rect = pygame.Rect(int(drone.pos.x), int(drone.pos.y), DRONE_SIZE, DRONE_SIZE)
        hit_index = drone_rect.collidelist(obs1.get_rects())
        if hit_index != -1:
            drone.speed = 0
                
            




        text_speed = font2.render(f"Speed: {drone.speed}", True, BLACK)
        # Screen initiation and update
        screen.fill(WHITE)
        screen.blit(text, (300, 30))
        screen.blit(text_speed, (600, 40))
        drone.draw_drone(screen)
        obs1.draw_obss(screen)
        pygame.draw.line(screen, (0,255,0), (drone.pos.x + 5, drone.pos.y + 5), (drone.pos.x + 5, drone.pos.y + 5) + drone.direction * 100)
        pygame.display.flip()
        clock.tick(60)
   
    
    pygame.quit()

    

main()


