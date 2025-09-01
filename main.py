import sys, pygame
from pygame.math import Vector2
from sim import Drone, Obstacles, SCREEN_WIDTH, SCREEN_HEIGHT, DRONE_SIZE, COLOURS, SENSOR_COUNT, OBSTACLE_COUNT


def main():
        # Set up pygame 
    pygame.init()

    # drone and obstacle object creation
    drone = Drone()
    obs1 = Obstacles(OBSTACLE_COUNT)

        # Screen set up
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)

        # set up font 
    font1 = pygame.font.SysFont('Calibri', 30, True, False)
    font2 = pygame.font.SysFont('Calibri', 18, True, False)
    text = font1.render("Drone sim test", True, COLOURS["BLACK"])
    

        # Clock
    clock = pygame.time.Clock()

    running = True 
    while running:
        
        for event in pygame.event.get():
            # To close program when X pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

        # Key Combinations for each mechanic !!! Added the obstacle list as Rect
        drone.mechanics(obs1.get_rects())

        key =  pygame.key.get_pressed()
        if key[pygame.K_r]:
            obs1.regenerate(OBSTACLE_COUNT)

        # Move Drone 
        dt = clock.tick(60)/ 1000
        drone.move_drone(dt)   
               
            
        #HUD
        text_speed = font2.render(f"Speed: {drone.speed}", True, COLOURS["BLACK"])


        # Screen initiation and update
        screen.fill(COLOURS["WHITE"])
        screen.blit(text, (400, 30))
        screen.blit(text_speed, (600, 40))
        drone.draw_drone(screen)
        obs1.draw_obss(screen)
        drone.sensors(screen, SENSOR_COUNT, obs1.Rects)
        drone.avoid(dt)
        pygame.display.flip()
        clock.tick(60)
   
    
    pygame.quit()

    

main()


