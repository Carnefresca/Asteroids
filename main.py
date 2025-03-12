from asteroidfield import *
from asteroid import *
from player import Player
from constants import *
import pygame

def main():
    pygame.init
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    AsteroidField.containers = (updateable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    Background = AsteroidField()
    Carne = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius= PLAYER_RADIUS)
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)
        screen.fill(0)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()