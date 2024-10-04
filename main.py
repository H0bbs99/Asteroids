# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    #Containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Set FPS
    clock = pygame.time.Clock()
    
    dt = 0

    #Starting Screen Display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    #initate containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)
    
    #inititate Player 
    user = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT /2)
    astroids = AsteroidField()



    # Game Loop
    while True:
        # Allows the "X" button to close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for stuff in updatable:
            stuff.update(dt)

        for astro in asteroids:
            if astro.collision(user):
                print("Game Over!")
                pygame.quit()
                return
            
        # Set Screen to Black and refresh
        screen.fill("Black")
        
        #FPS Timing
        dt = clock.tick(60)/1000

        #Draw and Update Player
        for stuff in drawable:
            stuff.draw(screen)


        

            

     #   user.draw(screen)
      #  user.update(dt)

        pygame.display.flip()


if __name__ == "__main__":
    main()