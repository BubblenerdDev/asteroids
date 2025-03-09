import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from circleshape import CircleShape
from asteroidfield import AsteroidField
from shot import Shot
from circleshape import CircleShape
pygame.init()  

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Shot.containers = (shots,updatable,drawable)
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = updatable
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def main():
    print("Starting Asteroids!")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    running = True
    while running:
        dt = clock.tick(60) / 1000  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
        updatable.update(dt)  
        screen.fill("black")  
        for drawables in drawable:
            drawables.draw(screen)
        for asteroid in asteroids:
            if(player.collision(asteroid)):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):

                    shot.kill()
                    asteroid.split()
        pygame.display.flip()  
    pygame.quit()  

if __name__ == "__main__":
    main()

