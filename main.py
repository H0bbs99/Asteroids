# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *

def main():
    pygame.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # Set FPS
    clock = pygame.time.Clock()
    
    dt = 0

    #Starting Screen Display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game Loop
    while True:
        # Allows the "X" button to close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Set Screen to Black and refresh
        screen.fill("Black")
        pygame.display.flip()

        #FPS Timing
        dt = pygame.time.Clock.tick(clock, 60)/1000


if __name__ == "__main__":
    main()