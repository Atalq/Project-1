import pygame
import sys
from pygame.math import Vector2
import random


class DRONE:
    def __init__(self):

        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.speed = 1
        self.pos = Vector2(self.x, self.y)
        self.direction = (1, 0)

    def update():
        pass



    def draw_drone(self, screen):
        drone_rect = pygame.Rect(int(self.pos.x), int(self.pos.y), 10, 15)
        pygame.draw.rect(screen, BLACK, drone_rect)
        



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

drone = DRONE()

def main():
        # Set up pygame and screen  
    pygame.init()
    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)

        # set up font 
    font = pygame.font.SysFont('Calibri', 30, True, False)
    text = font.render("Drone sim test", True, BLACK)

        # Clock
    clock = pygame.time.Clock()

    running = True 
    while running:
        
        for event in pygame.event.get():
            # To close program when X pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Key combinations and movement correlation
            key =  pygame.key.get_pressed()
            
        
        
        screen.fill(WHITE)
        screen.blit(text, (300, 30))
        drone.draw_drone(screen)
        pygame.display.flip()
        clock.tick(60)
   
    
    pygame.quit()

    

main()


