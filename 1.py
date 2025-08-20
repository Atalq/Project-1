import pygame
import sys
from pygame.math import Vector2
import random


class Drone:
    def __init__(self):

        self.x = 200
        self.y = 200
        self.speed = 10
        self.pos = Vector2(self.x, self.y)
        self.direction = Vector2(1, 0)

    def move_drone(self):
    
        self.pos = Vector2(self.pos.x + self.speed * self.direction.x, self.pos.y + self.speed * self.direction.y)


    def draw_drone(self, screen):
        drone_rect = pygame.Rect(int(self.pos.x), int(self.pos.y), DRONE_SIZE, DRONE_SIZE)
        pygame.draw.rect(screen, BLACK, drone_rect)
        

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DRONE_SIZE = 10

def main():
        # Set up pygame 
    pygame.init()

    # drone object creation
    drone = Drone()

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
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 100)


    running = True 
    while running:
        
        for event in pygame.event.get():
            # To close program when X pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Initiate drone Movement
            if event.type == SCREEN_UPDATE:
                drone.move_drone()
                

            
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
                drone.speed = 10
                drone.direction = Vector2(0, 0)
            if key[pygame.K_w]:
                drone.speed += 1
            if key[pygame.K_s]:
                drone.speed -= 1

            # Edge (boundry) consitions
            if drone.pos.x >= 800-10:
                drone.direction = Vector2(-1, 0)
            elif drone.pos.x <= 0:
                drone.direction = Vector2(1, 0)
            if drone.pos.y >= 600-10:
                drone.direction = Vector2(0, -1)
            elif drone.pos.y <= 0:
                drone.direction = Vector2(0, 1)

        
        text_speed = font2.render(f"Speed: {drone.speed}", True, BLACK)
        # Screen initiation and update
        screen.fill(WHITE)
        screen.blit(text, (300, 30))
        screen.blit(text_speed, (600, 40))
        drone.draw_drone(screen)
        # Header code :::: pygame.draw.line(screen, (255,0,0), (drone.pos.x + 5, drone.pos.y + 5), (drone.pos.x + 5, drone.pos.y + 5) + drone.direction * 15)
        pygame.display.flip()
        clock.tick(60)
   
    
    pygame.quit()

    

main()


