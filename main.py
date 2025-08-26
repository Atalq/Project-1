import sys, pygame
from pygame.math import Vector2
from sim import Drone, Obstacles, SCREEN_WIDTH, SCREEN_HEIGHT, DRONE_SIZE, COLOURS


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
    text = font1.render("Drone sim test", True, COLOURS["BLACK"])
    

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
        if key[pygame.K_r]:
            obs1.regenerate(10)
        

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
                
            




        text_speed = font2.render(f"Speed: {drone.speed}", True, COLOURS["BLACK"])
        # Screen initiation and update
        screen.fill(COLOURS["WHITE"])
        screen.blit(text, (400, 30))
        screen.blit(text_speed, (600, 40))
        drone.draw_drone(screen)
        obs1.draw_obss(screen)
        # HEADER: pygame.draw.line(screen, COLOURS["GREEN"], (drone.pos.x + 5, drone.pos.y + 5), (drone.pos.x + 5, drone.pos.y + 5) + drone.direction * 100)
        drone.generate_sensors(12, screen)
        pygame.display.flip()
        clock.tick(60)
   
    
    pygame.quit()

    

main()


