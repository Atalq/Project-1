import pygame
import sys
from pygame.math import Vector2
import random


class DRONE:
    def __init__(self):

        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.speed = 5
        self.pos = Vector2(self.x, self.y)
        self.direction = Vector2(1, 0)

    def move_drone(self):
        
        self.pos = Vector2(self.pos.x + self.speed * self.direction.x, self.pos.y + self.speed * self.direction.y)


    def draw_drone(self, screen):
        drone_rect = pygame.Rect(int(self.pos.x), int(self.pos.y), 10, 10)
        pygame.draw.rect(screen, BLACK, drone_rect)
        



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)



def main():
        # Set up pygame 
    pygame.init()

    # drone object creation
    drone = DRONE()

        # Screen set up
    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)

        # set up font 
    font = pygame.font.SysFont('Calibri', 30, True, False)
    text = font.render("Drone sim test", True, BLACK)

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

            if event.type == SCREEN_UPDATE:
                drone.move_drone()

            
        
        
        screen.fill(WHITE)
        screen.blit(text, (300, 30))
        drone.draw_drone(screen)
        pygame.display.flip()
        clock.tick(60)
   
    
    pygame.quit()

    

main()


