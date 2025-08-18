import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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
    #Initial x, y and the velocity
    x, y = 100, 100
    vel = 10

    while running:
        for event in pygame.event.get():
            # To close program when X pressed
            if event.type == pygame.QUIT:
                running = False
            # Key combinations and movement correlation
            key =  pygame.key.get_pressed()
            if key[pygame.K_LEFT] and x > 0:
                x -= vel
            if key[pygame.K_RIGHT] and x < 800-10:
                x += vel
            if key[pygame.K_UP] and y > 0:
                y -= vel
            if key[pygame.K_DOWN] and y < 600-15:
                y += vel

        screen.fill(WHITE)
        screen.blit(text, (300, 30))
        pygame.draw.rect(screen, BLACK, [x, y, 10, 15])
        pygame.display.flip()
        clock.tick(30)
   
    
    pygame.quit()

    

main()


